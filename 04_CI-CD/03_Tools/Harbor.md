# Harbor

`Harbor` — self-hosted enterprise container registry.

Harbor используют, когда нужен свой registry с RBAC, projects, vulnerability scanning, replication и retention policies.

---

# Что умеет

```text
container image registry
OCI artifacts
projects/RBAC
robot accounts
vulnerability scanning
image signing integrations
replication
retention policies
proxy cache
```

---

# Robot accounts

Для CI лучше создавать robot account с минимальными правами:

```text
push в project/app
pull где нужно
без admin прав
```

---

# Push

```bash
docker login harbor.example.com
docker tag app:1.0 harbor.example.com/project/app:1.0
docker push harbor.example.com/project/app:1.0
```

---

# Частые проблемы

## x509 unknown authority

Runner/node не доверяет TLS certificate Harbor.

## denied

Нет прав у robot/user.

## storage full

Нужны retention и garbage collection.

---

# Связанные заметки

- [[Container Registry]]
- [[Image Security]]
- [[Supply Chain Security]]
- [[TLS Certificates]]
