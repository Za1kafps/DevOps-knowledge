# Network

[[Network]] — область DevOps про то, как пакеты доходят от клиента до сервиса и обратно.

Сеть в production нужна не “чтобы был интернет”, а чтобы понимать путь запроса:

```text
client
  -> DNS
  -> routing
  -> firewall / security group
  -> load balancer
  -> reverse proxy / ingress
  -> application
  -> response back
```

Если сервис “не работает”, сеть проверяют слоями: имя, адрес, маршрут, порт, TLS, HTTP, приложение.

---

# Главные ветки

## Адресация

- [[IPv4]]
- [[IPv6]]
- [[Subnetting and CIDR]]

Адресация отвечает на вопрос: какой IP у узла и в какой сети он находится.

---

## Доставка пакетов

- [[Routing]]
- [[NAT]]
- [[MTU]]
- [[VPN]]

Эти темы отвечают на вопрос: куда пакет пойдёт, изменится ли его адрес и сможет ли он пройти по пути без фрагментации.

---

## Транспорт

- [[TCP]]
- [[UDP]]

TCP нужен там, где важна доставка и порядок: HTTP, SSH, PostgreSQL, Redis.

UDP нужен там, где важна простота и низкая задержка: DNS, QUIC, VPN, streaming.

---

## Прикладной уровень

- [[DNS]]
- [[HTTP]]
- [[HTTPS and TLS]]
- [[TLS]]
- [[Response HTTP States]]
- [[HTTP requests]]

Это уровень, который чаще всего виден в `curl`, браузере, API gateway, Ingress и reverse proxy.

---

## Диагностика

- [[curl]]
- [[tcpdump]]
- [[ss]]
- [[Firewall]]
- [[Load Balancing]]

Диагностика сети почти всегда начинается с простого вопроса:

```text
имя резолвится?
IP reachable?
порт открыт?
TLS проходит?
HTTP отвечает?
ответ идёт от нужного backend?
```

---

# Базовый порядок проверки

## 1. Проверить DNS

```bash
dig example.com
dig @1.1.1.1 example.com
```

Если по IP работает, а по домену нет — сначала смотри [[DNS]].

---

## 2. Проверить маршрут

```bash
ip route
ip route get 1.1.1.1
traceroute example.com
```

Если пакет уходит не через тот интерфейс или gateway — это [[Routing]].

---

## 3. Проверить порт

```bash
ss -lntp
nc -vz example.com 443
```

Если порт не слушается локально — проблема в сервисе.

Если локально слушается, но снаружи закрыт — смотри [[Firewall]], security groups, [[NAT]] и [[Load Balancing]].

---

## 4. Проверить HTTP/TLS

```bash
curl -v https://example.com
openssl s_client -connect example.com:443 -servername example.com
```

`curl -v` показывает DNS, TCP connect, TLS handshake, HTTP request и HTTP response.

---

## 5. Посмотреть пакеты

```bash
sudo tcpdump -i any host 1.2.3.4
sudo tcpdump -i any port 443
```

Если `curl` говорит “timeout”, а `tcpdump` показывает SYN без SYN-ACK — ответ не возвращается или порт фильтруется.

---

# Частые симптомы

## `Could not resolve host`

Проблема на уровне [[DNS]].

Проверить:

```bash
dig domain.com
cat /etc/resolv.conf
resolvectl status
```

---

## `Connection refused`

Хост доступен, но на порту никто не слушает или сервис отклонил соединение.

Проверить:

```bash
ss -lntp
systemctl status nginx
docker ps
```

---

## `Connection timed out`

Пакет не получил ответ.

Частые причины:

```text
firewall drop
security group
неверный route
backend недоступен
NAT сломан
load balancer смотрит не туда
```

---

## `SSL certificate problem`

Проблема на уровне [[TLS]].

Проверить:

```bash
curl -vk https://example.com
openssl s_client -connect example.com:443 -servername example.com
```

---

# Что важно DevOps-инженеру

Сеть надо понимать не как абстрактную OSI-модель, а как цепочку фактов:

```text
домен -> IP -> route -> firewall -> socket -> TLS -> HTTP -> app logs
```

Каждый слой должен подтверждаться командой. Если нет факта, это гипотеза.
