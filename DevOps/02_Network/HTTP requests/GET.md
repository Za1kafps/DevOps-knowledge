# GET

`GET` — HTTP-метод для получения ресурса.

Обычно `GET` не должен менять состояние на сервере.

Примеры:

```text
GET /users
GET /users/42
GET /health
GET /metrics
```

Связано с [[HTTP]], [[curl]], [[Response HTTP States]].

---

# Проверка

```bash
curl -v https://example.com/api/users
```

С query parameters:

```bash
curl -v 'https://example.com/api/users?limit=10&page=2'
```

С Authorization:

```bash
curl -v https://example.com/api/profile \
  -H "Authorization: Bearer TOKEN"
```

---

# Кэширование

GET часто кэшируется браузером, CDN или reverse proxy.

На поведение влияют headers:

```text
Cache-Control
ETag
If-None-Match
Last-Modified
If-Modified-Since
```

Если “данные старые”, проверь, нет ли cache layer между клиентом и backend.

---

# Частые ошибки

## 404

Path не существует или Host попал не в тот virtual host.

## 401/403

Не передан token или нет прав.

## 405

Endpoint существует, но GET для него не разрешён.

---

# Связанные заметки

- [[HTTP requests]]
- [[HTTP]]
- [[curl]]
