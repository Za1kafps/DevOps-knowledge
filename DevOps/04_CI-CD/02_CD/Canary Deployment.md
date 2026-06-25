# Canary Deployment

`Canary deployment` — стратегия, где новая версия получает небольшую долю traffic.

Цель — проверить новую версию на реальных пользователях с маленьким blast radius.

---

# Как работает

```text
stable version -> 99% traffic
canary version -> 1% traffic

если метрики нормальные:
1% -> 5% -> 25% -> 50% -> 100%
```

---

# Что нужно для canary

```text
traffic splitting
метрики error rate/latency
логи по version
быстрый rollback
alerts
достаточный traffic volume
```

Без observability canary бессмысленен: ты не поймёшь, стало хуже или нет.

---

# Где реализуют

```text
ingress controller
service mesh
API gateway
load balancer
progressive delivery tools
```

В Kubernetes часто используют Argo Rollouts, Flagger, service mesh или ingress-specific annotations.

---

# Что смотреть

```text
5xx rate
p95/p99 latency
business errors
CPU/memory
restarts
queue lag
database errors
```

---

# Частые ошибки

## Canary без метрик

Traffic разделили, но решение принимается глазами по логам.

## Нет sticky/session стратегии

Пользователь прыгает между версиями и ловит странное поведение.

## Несовместимые версии

Stable и canary одновременно работают с разными expectations к DB/API.

---

# Связанные заметки

- [[Deployment Strategies]]
- [[Observability]]
- [[SLO]]
- [[Load Balancing]]
- [[Rollback]]
