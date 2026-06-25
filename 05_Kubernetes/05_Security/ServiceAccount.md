# ServiceAccount

`ServiceAccount` — identity для Pod внутри Kubernetes.

Pod использует ServiceAccount token, чтобы обращаться к Kubernetes API или внешним системам через workload identity.

---

# Проверка

```bash
kubectl get serviceaccount -n app
kubectl describe serviceaccount backend -n app
kubectl auth can-i get pods --as system:serviceaccount:app:backend -n app
```

---

# В Pod

```yaml
spec:
  serviceAccountName: backend
```

Если не указать, используется `default`.

---

# Безопасность

```text
не выдавать лишние RBAC права default ServiceAccount
создавать отдельный ServiceAccount на приложение
не монтировать token, если он не нужен
использовать short-lived projected tokens
```

Отключить automount:

```yaml
automountServiceAccountToken: false
```

---

# Связанные заметки

- [[RBAC]]
- [[Kubernetes Security]]
- [[Secrets]]
