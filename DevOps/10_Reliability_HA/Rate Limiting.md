# Rate Limiting

`Rate Limiting` ограничивает количество запросов или действий за период.

Он защищает систему от:

```text
abuse
brute force
traffic spikes
дорогих endpoints
noisy clients
dependency overload
```

---

# Где ставить

```text
edge/CDN
WAF
API gateway
reverse proxy
application
queue consumer
database-facing layer
```

Чем ближе к edge, тем дешевле отбрасывать плохой traffic.

---

# Ключи лимита

```text
IP
user id
API token
tenant
route
method
```

IP-only лимит часто плох для NAT/corporate networks.

---

# Алгоритмы

```text
fixed window
sliding window
token bucket
leaky bucket
concurrency limit
```

Token bucket хорошо переносит короткие bursts.

---

# HTTP ответы

Обычно:

```text
429 Too Many Requests
Retry-After: 60
```

---

# Частые ошибки

## Один лимит на всех

VIP tenant и test client получают одинаковый budget.

## Нет observability

Непонятно, кого и почему режет limiter.

## Лимит после дорогой работы

Если запрос уже сходил в БД, limiter слишком поздно.

---

# Связанные заметки

- [[WAF]]
- [[Nginx]]
- [[Redis]]
- [[SLO]]
- [[HTTP Status Codes]]
