# POST

`POST` — HTTP-метод для отправки данных на сервер.

Обычно используется для создания ресурса или запуска действия.

Примеры:

```text
POST /users
POST /login
POST /payments/charge
POST /webhook
```

---

# POST JSON

```bash
curl -v -X POST https://example.com/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Ivan"}'
```

Если указать `-d`, curl сам использует POST, даже без `-X POST`.

---

# Content-Type

Backend обычно парсит body по `Content-Type`.

JSON:

```text
Content-Type: application/json
```

Form:

```text
Content-Type: application/x-www-form-urlencoded
```

Upload:

```text
multipart/form-data
```

Если `Content-Type` неверный, можно получить `400` или `415`.

---

# Idempotency

POST обычно не idempotent.

Повтор одного и того же POST может создать два заказа, два платежа или два job.

Для опасных операций используют idempotency key:

```text
Idempotency-Key: <uuid>
```

---

# Частые ошибки

## 400

Невалидный JSON, нет обязательного поля, неправильный format.

## 401/403

Нет auth или нет прав на действие.

## 413

Body больше лимита proxy или приложения.

## 415

Неверный `Content-Type`.

---

# Связанные заметки

- [[HTTP requests]]
- [[HTTP]]
- [[curl]]
- [[Response HTTP States]]
