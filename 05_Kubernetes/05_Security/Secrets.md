# Secrets

`Kubernetes Secret` хранит чувствительные значения как Kubernetes object.

Важно: `data` в Secret — base64, не encryption.

---

# Пример

```bash
kubectl create secret generic app-secret \
  --from-literal=DATABASE_URL='postgres://...' \
  -n app
```

Посмотреть:

```bash
kubectl get secret app-secret -n app -o yaml
```

---

# Использование

Env:

```yaml
envFrom:
  - secretRef:
      name: app-secret
```

Volume:

```yaml
volumes:
  - name: secret
    secret:
      secretName: app-secret
```

---

# Production

```text
encryption at rest
RBAC ограничивает get/list secrets
не хранить plaintext в Git
rotation
external secret manager
audit access
```

---

# Связанные заметки

- [[Secrets Management]]
- [[SOPS]]
- [[Sealed Secrets]]
- [[RBAC]]
