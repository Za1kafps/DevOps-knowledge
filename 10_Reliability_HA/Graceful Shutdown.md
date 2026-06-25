# Graceful Shutdown

`Graceful Shutdown` — корректное завершение приложения без обрыва активных запросов и потери работы.

Особенно важно для Kubernetes rolling updates, autoscaling и node maintenance.

---

# Как выглядит

```text
process получает SIGTERM
перестаёт принимать новые requests
readiness становится false
дожидается активных requests/jobs
закрывает connections
flush logs/metrics
завершается до timeout
```

---

# Kubernetes

Kubernetes отправляет SIGTERM, ждёт `terminationGracePeriodSeconds`, потом SIGKILL.

```yaml
terminationGracePeriodSeconds: 30
```

PreStop hook может дать время убрать Pod из traffic:

```yaml
lifecycle:
  preStop:
    exec:
      command: ["sh", "-c", "sleep 5"]
```

Но лучше, чтобы приложение само правильно обрабатывало SIGTERM.

---

# Что важно

```text
readiness падает перед завершением
HTTP server shutdown с timeout
background workers stop pulling new jobs
in-flight jobs либо завершаются, либо возвращаются в queue
DB connections закрываются
```

---

# Частые ошибки

## SIGTERM игнорируется

Kubernetes ждёт и убивает SIGKILL.

## Readiness остаётся true

Load balancer продолжает слать traffic в завершающийся Pod.

## Jobs теряются

Worker взял задачу, получил SIGTERM и не вернул её в queue.

---

# Связанные заметки

- [[Deployment]]
- [[Rolling Update]]
- [[Readiness Probe]]
- [[Job and CronJob]]
