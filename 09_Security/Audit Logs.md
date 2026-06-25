# Audit Logs

`Audit Logs` отвечают на вопросы:

```text
кто
что
когда
откуда
с каким результатом
```

Без audit logs incident response превращается в догадки.

---

# Где нужны audit logs

```text
cloud IAM
Kubernetes API
CI/CD actions
Git repository
Vault/secrets
SSH/sudo
database admin actions
WAF/security events
```

---

# Kubernetes audit

Kubernetes API audit показывает requests к API Server.

Полезно искать:

```text
create clusterrolebinding
get secrets
exec into pod
delete resources
patch deployments
```

---

# Linux auth logs

Debian/Ubuntu:

```bash
tail -f /var/log/auth.log
journalctl _COMM=sudo
```

RHEL-like:

```bash
tail -f /var/log/secure
```

---

# Что важно

```text
centralized storage
retention
tamper resistance
time sync
searchable fields
access control
alerts on critical actions
```

---

# Частые ошибки

## Logs только на host

Атакующий может удалить локальные logs.

## Нет времени/таймзоны

Без NTP и нормальных timestamps расследование сложнее.

## Audit есть, alert нет

Критичные действия замечают слишком поздно.

---

# Связанные заметки

- [[Security]]
- [[Incident Response Flow]]
- [[Kubernetes Security]]
- [[Vault]]
- [[OS Hardening]]
