# HTTP

`HTTP` — прикладной протокол запросов и ответов.

Через HTTP работают сайты, REST API, webhooks, healthchecks, ingress, reverse proxy и большинство интеграций между сервисами.

HTTP находится поверх транспорта: обычно [[TCP]], а для HTTPS ещё и [[TLS]].

```text
DNS -> TCP -> TLS -> HTTP -> application
```

---

# Как выглядит HTTP

Клиент отправляет request:

```text
GET /api/users HTTP/1.1
Host: example.com
Accept: application/json
```

Сервер возвращает response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{"ok":true}
```

---

# HTTP stateless

HTTP сам по себе не хранит состояние между запросами.

Сессии делают поверх HTTP:

```text
Cookie
Authorization header
JWT
server-side session storage
```

Поэтому два одинаковых HTTP-запроса могут получить разные ответы, если отличаются cookies, token, headers или backend state.

---

# Методы

Основные методы лежат отдельно:

- [[GET]]
- [[POST]]
- [[PUT]]
- [[PATCH]]
- [[DELETE]]
- [[HEAD]]
- [[OPTIONS]]
- [[CONNECT]]
- [[TRACE]]

Важная идея:

```text
GET читает
POST создаёт действие или ресурс
PUT заменяет ресурс
PATCH частично меняет ресурс
DELETE удаляет
```

Но реальное поведение задаёт приложение. Метод — договорённость API, а не магия.

---

# Заголовки

Частые headers:

```text
Host
User-Agent
Accept
Content-Type
Authorization
Cookie
Cache-Control
X-Forwarded-For
X-Forwarded-Proto
```

Для DevOps особенно важны:

```text
Host                 virtual host / ingress routing
X-Forwarded-For      реальный client IP за proxy
X-Forwarded-Proto    был ли исходный запрос https
Authorization        API auth
Content-Type         как backend парсит body
```

---

# HTTP status codes

Смотри [[Response HTTP States]].

Коротко:

```text
2xx success
3xx redirect
4xx client-side problem
5xx server-side problem
```

Для эксплуатации важно не просто “500 плохо”, а где он возник:

```text
application
reverse proxy
ingress controller
load balancer
upstream timeout
auth gateway
```

---

# Проверка curl

Обычный запрос:

```bash
curl -v http://example.com
```

Только headers:

```bash
curl -I http://example.com
```

Показать status code:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://example.com
```

Отправить Host вручную:

```bash
curl -v -H "Host: example.com" http://1.2.3.4
```

---

# HTTP/1.1, HTTP/2, HTTP/3

HTTP/1.1 обычно работает поверх TCP и использует текстовый формат.

HTTP/2 использует binary framing и multiplexing внутри одного соединения.

HTTP/3 работает поверх QUIC, а QUIC использует [[UDP]].

В DevOps это важно для load balancer, ingress, observability и TLS termination.

---

# Частые проблемы

## 404

Не найден route/path/virtual host.

Проверить:

```bash
curl -v -H "Host: example.com" http://ip/path
```

---

## 502

Proxy не смог получить нормальный ответ от upstream.

Смотреть:

```text
nginx/ingress logs
upstream endpoints
port mismatch
application logs
```

---

## 504

Gateway timeout.

Смотреть:

```text
backend latency
proxy_read_timeout
load balancer timeout
database latency
```

---

# Связанные заметки

- [[Network]]
- [[curl]]
- [[HTTPS and TLS]]
- [[Response HTTP States]]
- [[Load Balancing]]
- [[Ingress]]
- [[Nginx]]
