# Rolling Update

`Rolling Update` — стратегия деплоя, где старая версия постепенно заменяется новой.

Вместо “остановить всё и запустить новое” система обновляет часть instances за раз.

В Kubernetes это стандартная стратегия для [[Deployment]].

---

# Как работает

```text
old pods: app-v1 app-v1 app-v1

step 1: app-v2 app-v1 app-v1
step 2: app-v2 app-v2 app-v1
step 3: app-v2 app-v2 app-v2
```

Во время rollout старая и новая версии могут работать одновременно.

---

# Kubernetes параметры

В Deployment:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 0
```

`maxSurge` — сколько extra pods можно создать сверх desired replicas.

`maxUnavailable` — сколько pods можно сделать недоступными во время rollout.

---

# Команды

Проверить rollout:

```bash
kubectl rollout status deploy/app -n production
```

История:

```bash
kubectl rollout history deploy/app -n production
```

Откат:

```bash
kubectl rollout undo deploy/app -n production
```

---

# Что обязательно

Rolling update требует:

```text
readiness probe
graceful shutdown
backward-compatible API
совместимые DB migrations
достаточно replicas
resources requests/limits
```

Без readiness probe Kubernetes может отправить traffic в pod, который ещё не готов.

---

# Частые проблемы

## Одна replica

Rolling update с одной replica может дать downtime, если `maxUnavailable` настроен неосторожно.

## Несовместимые версии

Old и new работают одновременно, поэтому API/DB/schema должны быть совместимы.

## Нет graceful shutdown

Pod получает SIGTERM, но приложение резко обрывает активные requests.

---

# Связанные заметки

- [[Deployment Strategies]]
- [[Continuous Delivery]]
- [[Rollback]]
- [[Readiness Probe]]
- [[Graceful Shutdown]]
