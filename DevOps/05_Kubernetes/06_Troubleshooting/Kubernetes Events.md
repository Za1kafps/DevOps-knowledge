# Kubernetes Events

`Kubernetes Events` — короткие сообщения о важных изменениях и ошибках resources.

Events часто быстрее показывают причину, чем logs.

---

# Команды

По namespace:

```bash
kubectl get events -n app --sort-by=.lastTimestamp
```

По всему cluster:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Через describe:

```bash
kubectl describe pod pod-name -n app
```

---

# Что искать

```text
FailedScheduling
FailedMount
FailedPull
BackOff
Unhealthy
Killing
FailedCreate
```

---

# Ограничения

Events живут недолго и могут агрегироваться.

Для долгого хранения нужны event exporter/logging.

---

# Связанные заметки

- [[Pod Pending]]
- [[PVC Pending]]
- [[ImagePullBackOff]]
- [[Kubernetes CrashLoopBackOff]]
