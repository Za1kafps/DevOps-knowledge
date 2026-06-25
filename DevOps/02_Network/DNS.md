# DNS

`DNS` — система, которая переводит доменные имена в адреса и служебные записи.

Пример:

```text
example.com -> 93.184.216.34
```

Для DevOps DNS важен не как “телефонная книга интернета”, а как первый слой почти любого инцидента:

```text
домен не резолвится
резолвится не туда
часть пользователей видит старый IP
Ingress работает, но Host не совпадает
почта не проходит SPF/DKIM/DMARC
сертификат выпущен не на тот домен
```

DNS связан с [[HTTP]], [[HTTPS and TLS]], [[Load Balancing]], [[Ingress]], [[Cloudflare]] и [[CoreDNS]].

---

# Как проходит DNS-запрос

Упрощённая цепочка:

```text
application/browser
  -> OS cache
  -> resolver из /etc/resolv.conf
  -> root DNS
  -> TLD DNS
  -> authoritative DNS
  -> answer
```

На практике resolver часто кэширует ответ, поэтому до authoritative DNS запрос доходит не каждый раз.

---

# Recursive и authoritative

`Recursive resolver` ищет ответ за клиента.

Примеры:

```text
1.1.1.1
8.8.8.8
systemd-resolved
DNS resolver провайдера
```

`Authoritative DNS` хранит настоящие записи зоны.

Пример:

```text
ns1.cloudflare.com отвечает за example.com
```

---

# Основные записи

## A

Домен указывает на IPv4:

```text
example.com A 1.2.3.4
```

---

## AAAA

Домен указывает на IPv6:

```text
example.com AAAA 2a00:1450:4001:82a::200e
```

Если AAAA есть, часть клиентов будет пробовать IPv6.

---

## CNAME

Псевдоним:

```text
www.example.com CNAME example.com
```

Нельзя ставить CNAME на zone apex в классическом DNS:

```text
example.com CNAME other.example.net
```

Многие DNS-провайдеры дают похожее поведение через ALIAS/ANAME/flattening.

---

## NS

DNS-серверы зоны:

```text
example.com NS ns1.provider.net
```

Если NS указаны неверно у регистратора, изменения в панели DNS не будут иметь смысла.

---

## MX

Почтовые серверы домена:

```text
example.com MX 10 mail.example.com
```

---

## TXT

Текстовые записи.

Часто используются для:

```text
SPF
DKIM
DMARC
domain verification
ACME DNS-01 challenge
```

---

## PTR

Reverse DNS:

```text
1.2.3.4 -> mail.example.com
```

Важен для почты и некоторых allowlist-процессов.

---

# TTL

`TTL` — сколько секунд DNS-ответ можно держать в кэше.

Пример:

```text
TTL 300 = кэшировать 5 минут
```

Перед миграцией IP часто уменьшают TTL заранее:

```text
за 24-48 часов снизить TTL
переключить запись
после стабилизации вернуть TTL выше
```

Если TTL был 86400, часть клиентов может видеть старый ответ до суток.

---

# Команды

Обычная проверка:

```bash
dig example.com
```

Проверить конкретный тип:

```bash
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com TXT
dig example.com NS
```

Проверить через конкретный resolver:

```bash
dig @1.1.1.1 example.com
dig @8.8.8.8 example.com
```

Показать только ответ:

```bash
dig +short example.com
```

Посмотреть authoritative path:

```bash
dig +trace example.com
```

Проверить reverse DNS:

```bash
dig -x 1.2.3.4
```

---

# DNS на Linux

Посмотреть resolver:

```bash
cat /etc/resolv.conf
```

Если используется systemd-resolved:

```bash
resolvectl status
resolvectl query example.com
```

Сбросить cache:

```bash
sudo resolvectl flush-caches
```

---

# DNS в Kubernetes

В Kubernetes обычно DNS обслуживает [[CoreDNS]].

Проверить из pod:

```bash
kubectl exec -it pod-name -- nslookup kubernetes.default.svc.cluster.local
kubectl exec -it pod-name -- cat /etc/resolv.conf
```

Типичный service DNS:

```text
service.namespace.svc.cluster.local
```

Если pod не резолвит service, смотри:

```text
CoreDNS pods
Service/Endpoints
NetworkPolicy
node DNS
```

---

# Частые проблемы

## По IP работает, по домену нет

Почти точно DNS или Host/SNI.

Проверить:

```bash
dig domain.com
curl -v http://domain.com
curl -v -H "Host: domain.com" http://ip
```

---

## У одних работает, у других нет

Причины:

```text
разный DNS cache
разные recursive resolvers
GeoDNS/CDN
IPv6 AAAA сломан
старый TTL
split-horizon DNS
```

---

## DNS указывает на старый IP

Проверить authoritative DNS:

```bash
dig @ns1.provider.net example.com A
```

Если authoritative отдаёт новый IP, а public resolver старый — жди TTL или чисти cache там, где можешь.

---

## CNAME цепочка сломана

Проверить:

```bash
dig www.example.com CNAME
dig target.example.net A
```

---

# Связанные заметки

- [[Network]]
- [[IPv4]]
- [[IPv6]]
- [[HTTP]]
- [[HTTPS and TLS]]
- [[Load Balancing]]
- [[CoreDNS]]
- [[Cloudflare]]
