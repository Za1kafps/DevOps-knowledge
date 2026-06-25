# Security

[[Security]] в DevOps — это защита supply chain, runtime, доступа, секретов, сети и audit trail.

Security не должна быть отдельной “проверкой в конце”. Она встраивается в:

```text
design
CI
container build
deployment
runtime
monitoring
incident response
```

---

# Основные ветки

- [[Secrets Management]]
- [[OS Hardening]]
- [[Kubernetes Security]]
- [[Supply Chain Security]]
- [[WAF]]
- [[Cloudflare WAF]]
- [[ZeroTrust]]
- [[Audit Logs]]
- [[IAM]]

---

# Базовые принципы

```text
least privilege
defense in depth
secure defaults
short-lived credentials
auditability
patch management
segmentation
backup and recovery
```

---

# Что защищать

```text
source code
CI/CD credentials
container images
registries
Kubernetes API
secrets
databases
public endpoints
admin access
logs/audit events
```

---

# Практический baseline

```text
MFA для админов
SSH только по ключам
CI secrets protected
images scanned
production deploy через approvals/policies
Kubernetes RBAC минимальный
NetworkPolicy для sensitive namespaces
WAF/rate limits на public endpoints
audit logs включены
backup restore проверен
```

---

# Частые ошибки

## Один admin token на всё

Невозможно нормально ограничить, ротировать и расследовать.

## Secrets в Git

Даже private repo не место для plaintext secrets.

## Security scans без triage

Отчёт есть, решений нет.

## Нет audit logs

После инцидента непонятно, кто что сделал.

---

# Связанные заметки

- [[CI-CD]]
- [[Containers]]
- [[Kubernetes]]
- [[Infrastructure]]
- [[Incident Response Flow]]
