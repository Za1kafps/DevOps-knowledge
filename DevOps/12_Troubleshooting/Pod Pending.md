# Pod Pending

`Pod Pending` означает, что Pod ещё не запущен на node.

Чаще всего проблема в scheduling или volume.

---

# Проверка

```bash
kubectl describe pod pod-name -n app
kubectl get events -n app --sort-by=.lastTimestamp
kubectl get nodes
```

Ищи:

```text
FailedScheduling
Insufficient cpu
Insufficient memory
node(s) had taint
pod has unbound immediate PersistentVolumeClaims
```

---

# Частые причины

```text
не хватает CPU/memory requests
nodeSelector/affinity не подходит
taints без tolerations
PVC Pending
image pull ещё не начался
quota/limitrange
```

---

# Что делать

```text
уменьшить requests если они завышены
добавить capacity/nodes
исправить affinity/tolerations
починить PVC/StorageClass
проверить ResourceQuota
```

---

# Связанные заметки

- [[Resources Requests and Limits]]
- [[PVC Pending]]
- [[Kubernetes Events]]
- [[Autoscaling]]
