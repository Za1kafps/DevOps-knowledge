# ZeroTrust

`Zero Trust` — модель, где сеть сама по себе не считается доверенной.

Доступ выдаётся по identity, context и policy.

---

# Принципы

```text
verify explicitly
least privilege
assume breach
strong identity
device/user context
continuous evaluation
```

---

# В DevOps

```text
доступ к admin panels через identity-aware proxy
SSH через bastion/SSO
service-to-service mTLS
short-lived credentials
network segmentation
audit logs
```

---

# Частые ошибки

## Просто VPN называют ZeroTrust

VPN даёт network access, но не всегда даёт granular identity-based access.

## Нет device/user posture

Любой token с любого устройства получает доступ.

---

# Связанные заметки

- [[IAM]]
- [[Audit Logs]]
- [[Service Mesh]]
- [[SSH Hardening]]
