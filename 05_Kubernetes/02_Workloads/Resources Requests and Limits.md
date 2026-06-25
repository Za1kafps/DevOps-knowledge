# Resources Requests and Limits

`requests` и `limits` управляют CPU/memory ресурсами containers.

Это одна из самых важных тем Kubernetes production.

---

# Requests

`requests` — сколько ресурсов Kubernetes резервирует для scheduling.

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
```

Scheduler использует requests, чтобы выбрать node.

Если requests завышены, cluster выглядит заполненным.

Если requests занижены, node может быть перегружена.

---

# Limits

`limits` — верхняя граница использования.

```yaml
resources:
  limits:
    memory: 256Mi
```

Memory limit жёсткий: при превышении container может получить OOMKilled.

CPU limit обычно throttling, а не kill.

---

# CPU

```text
100m = 0.1 CPU
500m = 0.5 CPU
1000m = 1 CPU
```

CPU request влияет на scheduling.

CPU limit может вызвать throttling и latency spikes.

---

# Memory

Memory request влияет на scheduling.

Memory limit защищает node, но если он слишком низкий, приложение будет падать с OOMKilled.

Проверять:

```bash
kubectl top pod -n app
kubectl describe pod pod-name -n app
```

---

# QoS classes

Kubernetes назначает QoS:

```text
Guaranteed
Burstable
BestEffort
```

`BestEffort` Pods первыми кандидаты на eviction при pressure.

---

# Частые ошибки

## Нет requests

Scheduler не понимает реальную потребность, node перегружается.

## CPU limit на latency-sensitive сервисе

Throttling может давать p99 spikes.

## Memory limit равен среднему потреблению

Нужен запас на peaks, GC, cache, startup.

---

# Связанные заметки

- [[Pod]]
- [[Deployment]]
- [[OOMKilled]]
- [[Capacity Planning]]
- [[Autoscaling]]
