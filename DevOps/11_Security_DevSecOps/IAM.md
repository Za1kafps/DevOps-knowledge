# IAM

`IAM` — Identity and Access Management.

IAM отвечает за то, кто может выполнить действие над ресурсом.

В DevOps IAM встречается в cloud, Kubernetes, CI/CD, Git, registry, Vault и databases.

---

# Основные понятия

```text
identity     user/service account/workload identity
authentication кто ты
authorization что тебе можно
policy       набор разрешений
role         набор прав
principal    субъект доступа
resource      объект доступа
condition     ограничение
```

---

# Least privilege

Права должны быть минимальными:

```text
только нужные actions
только нужные resources
только нужные environments
только нужное время
```

Плохо:

```text
admin на весь cloud account для CI deploy
```

Лучше:

```text
role только на deploy конкретного service в конкретный environment
```

---

# Human vs workload identity

Люди:

```text
SSO
MFA
groups
break-glass
audit
```

Workloads:

```text
service accounts
short-lived tokens
OIDC federation
rotation
no shared personal credentials
```

---

# CI/CD

Для deploy лучше:

```text
OIDC -> temporary cloud credentials
environment protection
branch/tag conditions
audit trail
```

Смотри [[OIDC in CI-CD]].

---

# Частые ошибки

## Shared admin user

Нельзя нормально расследовать действия.

## Long-lived access keys

Ключи забывают ротировать, они утекают в CI/logs/laptops.

## Wildcard policies

`*:*` удобно до первого инцидента.

---

# Связанные заметки

- [[Security]]
- [[OIDC in CI-CD]]
- [[RBAC]]
- [[Vault]]
- [[Audit Logs]]
