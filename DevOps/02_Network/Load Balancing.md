# Load Balancing

`Load Balancing` — распределение входящего трафика между несколькими backend.

Балансировщик нужен не только для “размазать нагрузку”, но и для:

```text
high availability
health checks
TLS termination
zero-downtime deploy
traffic shifting
single entrypoint
```

Связано с [[HTTP]], [[TCP]], [[HTTPS and TLS]], [[Nginx]], [[Ingress]], [[Kubernetes Service]].

---

# Где стоит балансировщик

Типичная цепочка:

```text
client
  -> DNS
  -> cloud load balancer
  -> ingress / nginx
  -> service
  -> pod / app instance
```

Балансировщик может работать на разных уровнях.

---

# L4 balancing

L4 балансирует TCP/UDP соединения.

Он видит:

```text
source IP
destination IP
source port
destination port
protocol
```

Но не понимает HTTP path и headers.

Примеры:

```text
TCP 443 -> backend:443
UDP 51820 -> backend:51820
```

---

# L7 balancing

L7 балансирует HTTP/gRPC.

Он может смотреть на:

```text
Host
Path
Headers
Cookies
HTTP method
```

Пример:

```text
api.example.com/users -> users backend
api.example.com/payments -> payments backend
```

---

# Алгоритмы

Частые алгоритмы:

```text
round robin
least connections
random
weighted
ip hash
consistent hash
```

Выбор зависит от приложения.

Если приложение stateful и хранит сессию локально, может понадобиться sticky sessions. Лучше, когда состояние вынесено во внешнее хранилище.

---

# Health checks

Балансировщик должен убирать мёртвые backend.

Примеры проверок:

```text
TCP connect
HTTP GET /health
HTTP GET /ready
gRPC health check
```

Важно различать:

```text
liveness  процесс жив
readiness готов принимать трафик
```

В Kubernetes это связано с [[Readiness Probe]] и [[Liveness Probe]].

---

# TLS termination

TLS может завершаться на балансировщике:

```text
client -> HTTPS -> LB -> HTTP -> backend
```

Или прокидываться дальше:

```text
client -> HTTPS -> LB -> HTTPS -> backend
```

Второй вариант нужен, если требуется шифрование внутри сети или mTLS.

---

# Диагностика

Проверить DNS:

```bash
dig app.example.com
```

Проверить конкретный backend:

```bash
curl -v http://10.0.1.10:8080/health
```

Проверить Host routing:

```bash
curl -v -H "Host: app.example.com" http://1.2.3.4/
```

Проверить TLS на IP:

```bash
curl -vk --resolve app.example.com:443:1.2.3.4 https://app.example.com/
```

---

# Частые проблемы

## 502 Bad Gateway

LB/proxy не смог получить корректный ответ от backend.

Смотреть:

```text
backend port
health check
upstream protocol
application logs
```

---

## 503 Service Unavailable

Нет доступных backend или все health checks failed.

---

## 504 Gateway Timeout

Backend не ответил за timeout.

Смотреть latency приложения, БД и timeout settings на всех proxy.

---

# Связанные заметки

- [[HTTP]]
- [[HTTPS and TLS]]
- [[Nginx]]
- [[Ingress]]
- [[Kubernetes Service]]
- [[Deployment Strategies]]
