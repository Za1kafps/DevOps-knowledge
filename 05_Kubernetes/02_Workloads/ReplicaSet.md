# ReplicaSet

`ReplicaSet` поддерживает заданное количество Pods.

Обычно ReplicaSet создаётся и управляется [[Deployment]], напрямую его редко создают руками.

---

# Что делает

```text
следит за selector
считает matching Pods
создаёт недостающие Pods
удаляет лишние Pods
```

---

# Проверка

```bash
kubectl get rs -n <ns>
kubectl describe rs <name> -n <ns>
kubectl get pods -n <ns> --show-labels
```

---

# Важное

Deployment rollout создаёт новый ReplicaSet для новой версии Pod template.

История ReplicaSet помогает понять, какие версии участвовали в rollout.

---

# Частые ошибки

## Selector пересёкся с чужими Pods

ReplicaSet может начать управлять не теми Pods.

## Старые ReplicaSets занимают внимание

Обычно их оставляют для rollout history, но actual traffic идёт через текущие Ready Pods.

---

# Связанные заметки

- [[Deployment]]
- [[Pod]]
- [[Rolling Update]]
