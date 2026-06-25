# HTTP Status Codes

HTTP status code помогает понять слой ошибки, но не заменяет логи.

---

# Быстрая карта

```text
2xx success
3xx redirect
4xx client/request/auth problem
5xx server/proxy/upstream problem
```

---

# Проверка

```bash
curl -i https://example.com
curl -s -o /dev/null -w "%{http_code} %{time_total}\n" https://example.com
curl -IL https://example.com
```

---

# Частые

```text
401 no/invalid auth
403 forbidden/WAF/RBAC
404 route/resource not found
413 body too large
429 rate limit
502 bad gateway/upstream
503 no healthy backend
504 gateway timeout
```

---

# Связанные заметки

- [[Response HTTP States]]
- [[curl]]
- [[Nginx 502]]
- [[Ingress 502]]
