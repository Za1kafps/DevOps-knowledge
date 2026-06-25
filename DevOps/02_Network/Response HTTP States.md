# Response HTTP States

HTTP status code — код ответа сервера на HTTP-запрос.

Он показывает результат обработки запроса, но сам по себе не всегда говорит, где проблема.

Пример:

```text
HTTP/1.1 200 OK
HTTP/1.1 404 Not Found
HTTP/1.1 502 Bad Gateway
```

Связано с [[HTTP]], [[curl]], [[Load Balancing]], [[Nginx]], [[Ingress]].

---

# Группы кодов

## 1xx

Информационные ответы.

В обычной диагностике встречаются редко.

---

## 2xx

Успешная обработка.

Частые:

```text
200 OK
201 Created
202 Accepted
204 No Content
```

`204` означает успешный ответ без body.

---

## 3xx

Редиректы.

Частые:

```text
301 Moved Permanently
302 Found
307 Temporary Redirect
308 Permanent Redirect
```

Проверить цепочку редиректов:

```bash
curl -IL https://example.com
```

Если приложение за proxy бесконечно редиректит HTTP <-> HTTPS, проверь `X-Forwarded-Proto`.

---

## 4xx

Ошибка на стороне клиента или запроса.

Частые:

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
408 Request Timeout
409 Conflict
413 Payload Too Large
415 Unsupported Media Type
429 Too Many Requests
```

Важно: 4xx может генерировать не только приложение, но и proxy, WAF, auth gateway, ingress.

---

## 5xx

Ошибка на стороне сервера или промежуточного компонента.

Частые:

```text
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

5xx всегда разбирают по цепочке:

```text
client -> LB -> ingress/nginx -> app -> database/external dependency
```

---

# Диагностика через curl

Показать только код:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
```

Показать код и время:

```bash
curl -s -o /dev/null -w "code=%{http_code} total=%{time_total}\n" https://example.com
```

Показать headers:

```bash
curl -I https://example.com
```

Следовать редиректам:

```bash
curl -L -v https://example.com
```

---

# Как читать частые ошибки

## 400 Bad Request

Запрос невалиден.

Проверить:

```text
Content-Type
body format
required headers
request size
proxy limits
```

---

## 401 Unauthorized

Нет валидной аутентификации.

Проверить:

```text
Authorization header
Bearer token
Cookie
OIDC/session
```

---

## 403 Forbidden

Пользователь или клиент известен, но доступ запрещён.

Частые источники:

```text
RBAC
WAF
IP allowlist
S3 bucket policy
application permissions
```

---

## 404 Not Found

Нет такого route/resource или запрос попал не в тот virtual host.

Проверить:

```bash
curl -v -H "Host: example.com" http://ip/path
```

---

## 413 Payload Too Large

Body больше лимита.

Смотреть лимиты:

```text
nginx client_max_body_size
ingress annotations
application upload limit
load balancer limits
```

---

## 429 Too Many Requests

Rate limit.

Смотреть:

```text
client IP
Authorization identity
proxy rate limit
application rate limiter
Retry-After header
```

---

## 502 Bad Gateway

Proxy получил плохой ответ от upstream или не смог подключиться.

Смотреть:

```text
upstream host/port
service endpoints
application crash
protocol mismatch HTTP/HTTPS
```

---

## 503 Service Unavailable

Сервис временно недоступен.

Часто:

```text
нет healthy backend
maintenance
readiness failed
overload
```

---

## 504 Gateway Timeout

Proxy ждал backend дольше timeout.

Смотреть:

```text
application latency
database latency
proxy timeout
load balancer timeout
external API dependency
```

---

# Связанные заметки

- [[HTTP]]
- [[curl]]
- [[Load Balancing]]
- [[Ingress 502]]
- [[Nginx 502]]
- [[HTTP Status Codes]]
