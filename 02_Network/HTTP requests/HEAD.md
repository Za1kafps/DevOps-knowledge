# HEAD

`HEAD` — HTTP-метод, который запрашивает headers без response body.

Он похож на [[GET]], но сервер должен вернуть только заголовки.

---

# Зачем нужен

HEAD используют, чтобы проверить:

```text
ресурс существует или нет
Content-Length
Content-Type
Last-Modified
ETag
redirect location
доступность endpoint без скачивания body
```

---

# Проверка

```bash
curl -I https://example.com/file.zip
```

То же явно:

```bash
curl -X HEAD -I https://example.com/file.zip
```

Проверить редиректы:

```bash
curl -IL https://example.com
```

---

# Где ломается

Не все приложения корректно реализуют HEAD.

Возможны ситуации:

```text
GET работает, HEAD даёт 405
HEAD возвращает другие headers
proxy обрабатывает HEAD иначе
```

Если healthcheck использует HEAD, убедись, что приложение его поддерживает.

---

# Связанные заметки

- [[HTTP requests]]
- [[GET]]
- [[curl]]
- [[HTTP]]
