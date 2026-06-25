# OPTIONS

`OPTIONS` — HTTP-метод для запроса возможностей сервера или endpoint.

Чаще всего DevOps сталкивается с OPTIONS из-за CORS preflight.

---

# CORS preflight

Браузер отправляет OPTIONS перед “непростым” cross-origin запросом.

Пример:

```text
OPTIONS /api/users
Origin: https://frontend.example.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Authorization, Content-Type
```

Сервер должен ответить CORS headers:

```text
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Access-Control-Allow-Headers
```

---

# Проверка

```bash
curl -i -X OPTIONS https://api.example.com/users \
  -H "Origin: https://frontend.example.com" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Authorization, Content-Type"
```

---

# Частые проблемы

## OPTIONS режется auth middleware

Preflight приходит без обычной авторизации, а backend требует token и отдаёт 401.

Для CORS preflight часто нужно разрешить OPTIONS до auth.

---

## Нет нужного header

Frontend отправляет `Authorization`, а backend не отдаёт:

```text
Access-Control-Allow-Headers: Authorization
```

Браузер заблокирует запрос до фактического POST/GET.

---

## Работает в curl, не работает в браузере

`curl` не применяет CORS policy.

CORS — ограничение браузера, а не сервера как TCP endpoint.

---

# Связанные заметки

- [[HTTP requests]]
- [[HTTP]]
- [[curl]]
