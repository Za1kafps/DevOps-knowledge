# Autoscaling

`Autoscaling` — автоматическое изменение capacity под нагрузку.

Autoscaling не лечит плохую архитектуру, но помогает переживать изменяющийся traffic.

---

# Виды

```text
horizontal scaling  больше instances/pods
vertical scaling    больше CPU/memory на instance
cluster scaling     больше nodes
```

В Kubernetes:

```text
HPA
VPA
Cluster Autoscaler / Karpenter
```

---

# HPA

HPA меняет replicas по метрикам:

```bash
kubectl get hpa -A
kubectl describe hpa app -n app
```

HPA требует requests для CPU/memory based scaling.

---

# Важные ограничения

```text
startup time
cooldown/stabilization
resource requests
node capacity
database capacity
queue lag
rate limits
```

Если bottleneck в БД, больше Pods могут сделать хуже.

---

# Частые ошибки

## Scaling по CPU только

Для worker-ов часто лучше queue lag.

## Нет cluster capacity

HPA хочет 20 Pods, но nodes не хватает.

## Медленный startup

Pods появляются после того, как spike уже прошёл.

---

# Связанные заметки

- [[Horizontal Pod Autoscaler]]
- [[Capacity Planning]]
- [[Resources Requests and Limits]]
- [[Rate Limiting]]
