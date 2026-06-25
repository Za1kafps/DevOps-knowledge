# Horizontal Pod Autoscaler

`HPA` автоматически меняет replicas у Deployment/StatefulSet по метрикам.

---

# Проверка

```bash
kubectl get hpa -A
kubectl describe hpa <name> -n <ns>
kubectl top pods -n <ns>
```

Для CPU/memory HPA нужен Metrics Server.

---

# Пример

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

---

# Частые ошибки

## Нет requests

CPU utilization считается относительно requests.

## Scaling по CPU не отражает bottleneck

Для queue workers часто лучше queue lag/custom metrics.

## Cluster не масштабируется

HPA увеличил replicas, но Pods Pending из-за нехватки nodes.

---

# Связанные заметки

- [[Autoscaling]]
- [[Metrics Server]]
- [[Resources Requests and Limits]]
- [[Pod Pending]]
