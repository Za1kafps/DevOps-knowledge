# Infrastructure

[[Infrastructure]] — область DevOps про базовый слой, на котором живут приложения.

Сюда входят:

```text
servers
network perimeter
reverse proxy
TLS certificates
IaC
configuration management
secrets storage
backups
edge/CDN/WAF
```

---

# Основные ветки

- [[Linux Server Setup]]
- [[SSH Hardening]]
- [[UFW]]
- [[Fail2ban]]
- [[Nginx]]
- [[Reverse Proxy]]
- [[TLS Certificates]]
- [[cert-manager]]
- [[Terraform]]
- [[Ansible]]
- [[Vault]]
- [[Cloudflare]]
- [[Backups]]

---

# Production baseline

Минимальный server baseline:

```text
SSH keys, no password root login
firewall default deny inbound
security updates
time sync
logs
metrics
backup agent/job
least privilege users
TLS certificates monitored
documented restore path
```

---

# IaC правило

То, что можно описать кодом, должно быть описано кодом:

```text
cloud networks
VMs
DNS
load balancers
IAM
security groups
Kubernetes addons
```

Ручные изменения без фиксации в коде создают drift.

---

# Диагностика сервера

```bash
uptime
df -h
free -m
ss -lntp
journalctl -p err -b
systemctl --failed
```

Сеть:

```bash
ip addr
ip route
dig example.com
curl -v https://example.com
```

---

# Связанные заметки

- [[Linux]]
- [[Network]]
- [[Security]]
- [[Observability]]
- [[Reliability and High Availability]]
