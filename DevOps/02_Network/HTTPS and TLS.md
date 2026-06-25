# HTTPS and TLS

`HTTPS` — это [[HTTP]] поверх [[TLS]].

Он даёт шифрование, проверку подлинности сервера и защиту от подмены трафика.

Цепочка выглядит так:

```text
DNS -> TCP connect 443 -> TLS handshake -> HTTP request -> HTTP response
```

---

# Что проверяет клиент

Когда клиент открывает `https://example.com`, он проверяет:

```text
сертификат выдан доверенным CA
сертификат не истёк
домен есть в SAN сертификата
цепочка сертификатов полная
сервер владеет private key
TLS version/ciphers подходят клиенту
```

Если что-то не так, `curl` или браузер покажет TLS-ошибку до HTTP-запроса.

---

# SNI

`SNI` — Server Name Indication.

Клиент передаёт hostname во время TLS handshake, чтобы сервер выбрал правильный сертификат.

Это нужно, когда на одном IP много HTTPS-доменов.

Проверка:

```bash
openssl s_client -connect 1.2.3.4:443 -servername example.com
```

Без `-servername` сервер может отдать default certificate.

---

# TLS termination

TLS может завершаться на разных слоях:

```text
load balancer
ingress controller
nginx
application
service mesh sidecar
```

После termination трафик дальше может идти:

```text
HTTP внутри private network
HTTPS re-encrypt до backend
mutual TLS
```

Это архитектурное решение, а не “всегда правильно только так”.

---

# Проверка curl

Подробно:

```bash
curl -v https://example.com
```

Игнорировать проверку сертификата:

```bash
curl -vk https://example.com
```

Это полезно для диагностики, но не должно быть нормой в production.

Проверить конкретный IP под доменом:

```bash
curl -vk --resolve example.com:443:1.2.3.4 https://example.com
```

---

# Проверка openssl

```bash
openssl s_client -connect example.com:443 -servername example.com
```

Посмотреть даты сертификата:

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -dates
```

Посмотреть subject и SAN:

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -subject -issuer -ext subjectAltName
```

---

# Частые ошибки

## Certificate has expired

Сертификат истёк.

Проверить:

```bash
openssl x509 -noout -dates -in cert.pem
```

---

## Name mismatch

Домен не совпадает с SAN сертификата.

Пример:

```text
открываем api.example.com
сертификат только для www.example.com
```

---

## Incomplete chain

Сервер не отдаёт intermediate certificate.

У части клиентов может работать, у части нет.

---

## Wrong certificate behind load balancer

DNS ведёт на новый LB, а сертификат установлен старый или default.

Проверять через:

```bash
curl -vk --resolve domain:443:ip https://domain
```

---

# Связанные заметки

- [[HTTP]]
- [[TLS]]
- [[DNS]]
- [[Load Balancing]]
- [[Ingress]]
- [[cert-manager]]
- [[TLS Certificates]]
