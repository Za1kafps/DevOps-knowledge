# RBAC

`RBAC` — Role-Based Access Control в Kubernetes.

RBAC отвечает на вопрос:

```text
может ли этот user/serviceaccount выполнить verb над resource в namespace/cluster?
```

---

# Основные сущности

```text
Role           права внутри namespace
ClusterRole    права на cluster-scope или reusable role
RoleBinding    привязка Role/ClusterRole в namespace
ClusterRoleBinding привязка на весь cluster
ServiceAccount identity для Pods/controllers
```

---

# Verbs

Частые verbs:

```text
get
list
watch
create
update
patch
delete
```

`list/watch secrets` почти всегда очень чувствительное право.

---

# Проверка прав

Для себя:

```bash
kubectl auth can-i get pods -n app
kubectl auth can-i create deployments -n app
```

Для ServiceAccount:

```bash
kubectl auth can-i get secrets \
  --as system:serviceaccount:app:backend \
  -n app
```

---

# Пример Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: app
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
```

---

# Частые ошибки

## ClusterRoleBinding вместо RoleBinding

Права случайно выданы на весь cluster.

## `*` в resources/verbs

Удобно, но опасно. Использовать только осознанно.

## ServiceAccount default

Pod запущен с default ServiceAccount, которому кто-то выдал лишние права.

---

# Связанные заметки

- [[ServiceAccount]]
- [[Secrets]]
- [[Kubernetes Security]]
- [[API Server]]
