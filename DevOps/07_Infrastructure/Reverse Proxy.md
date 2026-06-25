# Reverse Proxy

`Reverse Proxy` принимает запросы от клиентов и пересылает их backend-сервисам.

Клиент видит proxy как сервер, а реальные backend скрыты за ним.

```text
client -> reverse proxy -> backend
```

---

# Зачем нужен

```text
TLS termination
routing by host/path
load balancing
auth gateway
rate limiting
compression
static files
request/response headers
centralized logs
```

---

# Важные headers

```text
Host
X-Real-IP
X-Forwarded-For
X-Forwarded-Proto
Forwarded
```

Если приложение за proxy генерирует redirect на HTTP вместо HTTPS, часто не передан или не учтён `X-Forwarded-Proto`.

---

# L4 vs L7

L4 proxy работает с TCP/UDP.

L7 proxy понимает HTTP:

```text
Host
Path
Headers
Cookies
Status codes
```

Nginx/Ingress/API Gateway чаще нужны как L7.

---

# Диагностика

Проверить backend напрямую:

```bash
curl -v http://127.0.0.1:8080/health
```

Проверить proxy:

```bash
curl -v https://app.example.com/health
```

Проверить Host:

```bash
curl -v -H "Host: app.example.com" http://1.2.3.4/
```

---

# Связанные заметки

- [[Nginx]]
- [[Load Balancing]]
- [[HTTP]]
- [[HTTPS and TLS]]
- [[WAF]]
