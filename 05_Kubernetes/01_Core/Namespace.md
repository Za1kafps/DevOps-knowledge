# Namespace

`Namespace` — логическое разделение ресурсов Kubernetes внутри cluster.

Namespace не является полной security boundary, но помогает разделять:

```text
environments
teams
applications
RBAC
quotas
NetworkPolicy scope
```

---

# Команды

```bash
kubectl get ns
kubectl create namespace app
kubectl get all -n app
kubectl config set-context --current --namespace=app
```

---

# Что namespace не изолирует сам

Без дополнительных политик namespace не запрещает:

```text
network traffic между namespace
node-level impact
cluster-wide RBAC ошибки
shared CRDs/controllers
```

Для изоляции нужны RBAC, NetworkPolicy, ResourceQuota, Pod Security Admission.

---

# Частые ошибки

## Всё в default

Сложнее RBAC, cleanup, quotas и ownership.

## Namespace удаляется с ресурсами

Удаление namespace удаляет namespaced resources внутри.

## Нет quotas

Одна команда может занять весь cluster.

---

# Связанные заметки

- [[RBAC]]
- [[NetworkPolicy]]
- [[Kubernetes Security]]
- [[Resources Requests and Limits]]
