# PodDisruptionBudget

`PodDisruptionBudget` ограничивает добровольные disruption.

Он защищает приложение от ситуации, когда maintenance/upgrade одновременно выселит слишком много Pods.

---

# Пример

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: app
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: app
```

---

# Что считается voluntary disruption

```text
kubectl drain
cluster autoscaler node removal
node upgrade
maintenance
```

PDB не спасает от hard failure node.

---

# Проверка

```bash
kubectl get pdb -A
kubectl describe pdb app -n app
```

---

# Частые ошибки

## PDB блокирует drain

`minAvailable` слишком строгий или replicas мало.

## PDB есть при одной replica

Он может заблокировать maintenance, но HA всё равно нет.

---

# Связанные заметки

- [[High Availability]]
- [[Deployment]]
- [[Graceful Shutdown]]
