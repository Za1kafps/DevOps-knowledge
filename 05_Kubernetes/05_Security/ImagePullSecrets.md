# ImagePullSecrets

`ImagePullSecrets` дают kubelet credentials для private container registry.

---

# Создать secret

```bash
kubectl create secret docker-registry regcred \
  --docker-server=registry.example.com \
  --docker-username=user \
  --docker-password=token \
  -n app
```

---

# Использовать в Pod

```yaml
spec:
  imagePullSecrets:
    - name: regcred
```

Или привязать к ServiceAccount:

```bash
kubectl patch serviceaccount default -n app \
  -p '{"imagePullSecrets":[{"name":"regcred"}]}'
```

---

# Диагностика

```bash
kubectl describe pod pod-name -n app
kubectl get secret regcred -n app
```

Ошибки:

```text
pull access denied
unauthorized
manifest unknown
no matching manifest
```

---

# Связанные заметки

- [[ImagePullBackOff]]
- [[Container Registry]]
- [[GHCR]]
- [[GitLab Container Registry]]
