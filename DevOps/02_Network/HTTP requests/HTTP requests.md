# HTTP requests

HTTP request — сообщение клиента к серверу.

Оно состоит из:

```text
method
path
headers
body
```

Пример:

```text
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer token

{"name":"Ivan"}
```

Методы:

- [[GET]]
- [[POST]]
- [[PUT]]
- [[PATCH]]
- [[DELETE]]
- [[HEAD]]
- [[OPTIONS]]
- [[CONNECT]]
- [[TRACE]]

---

# Что важно в DevOps

Для диагностики API важно проверять не только URL.

Нужно сравнить:

```text
method
Host header
path
query parameters
Content-Type
Authorization
body
proxy headers
```

Один и тот же endpoint может отвечать по-разному на `GET` и `POST`, с разным `Host` или без нужного token.

---

# Проверка

GET:

```bash
curl -v https://example.com/api/users
```

POST JSON:

```bash
curl -v -X POST https://example.com/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Ivan"}'
```

Проверить method allowed:

```bash
curl -i -X OPTIONS https://example.com/api/users
```

---

# Связанные заметки

- [[HTTP]]
- [[curl]]
- [[Response HTTP States]]
