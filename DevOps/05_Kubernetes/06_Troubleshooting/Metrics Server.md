# Metrics Server

`Metrics Server` собирает resource metrics CPU/memory для Kubernetes API.

Он нужен для:

```text
kubectl top
Horizontal Pod Autoscaler по CPU/memory
```

---

# Проверка

```bash
kubectl top nodes
kubectl top pods -A
kubectl -n kube-system get deploy metrics-server
kubectl -n kube-system logs deploy/metrics-server
```

---

# Частые проблемы

```text
metrics API not available
kubelet TLS/certificate issue
network до kubelet 10250
metrics-server не имеет RBAC
node metrics missing
```

---

# Связанные заметки

- [[Horizontal Pod Autoscaler]]
- [[Resources Requests and Limits]]
- [[Kubernetes Events]]
