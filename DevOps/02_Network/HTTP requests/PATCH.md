# PATCH

`PATCH` — HTTP-метод для частичного изменения ресурса.

Пример:

```text
PATCH /users/42
```

В отличие от [[PUT]], PATCH не обязан отправлять весь ресурс целиком.

---

# Пример

```bash
curl -v -X PATCH https://example.com/api/users/42 \
  -H "Content-Type: application/json" \
  -d '{"role":"admin"}'
```

---

# Форматы PATCH

На практике встречаются разные договорённости.

Обычный partial JSON:

```json
{"role":"admin"}
```

JSON Patch:

```json
[
  {"op":"replace","path":"/role","value":"admin"}
]
```

Merge Patch:

```json
{"role":"admin"}
```

Важно смотреть API-документацию: один и тот же PATCH может означать разные форматы body.

---

# Idempotency

PATCH может быть idempotent, а может не быть.

Пример idempotent:

```text
set role=admin
```

Пример не idempotent:

```text
increment balance by 10
```

---

# Частые ошибки

## 400

Неверный patch format.

## 404

Ресурс не найден.

## 409

Конфликт версии ресурса.

## 415

Неверный `Content-Type`.

---

# Связанные заметки

- [[HTTP requests]]
- [[PUT]]
- [[POST]]
- [[HTTP]]
