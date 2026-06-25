# TRACE

`TRACE` — HTTP-метод для диагностического echo-запроса.

Сервер возвращает запрос обратно клиенту.

В production TRACE почти всегда должен быть выключен.

---

# Почему TRACE опасен

Исторически TRACE связывали с атаками Cross-Site Tracing.

Даже если риск зависит от окружения, включённый TRACE редко нужен обычному приложению и может раскрывать headers.

---

# Проверка

```bash
curl -i -X TRACE https://example.com
```

Желательное поведение:

```text
405 Method Not Allowed
или 403 Forbidden
```

Нежелательно:

```text
200 OK и тело с отражёнными headers
```

---

# Где отключать

```text
nginx
apache
application framework
API gateway
load balancer / WAF
```

---

# Связанные заметки

- [[HTTP requests]]
- [[HTTP]]
- [[Security]]
