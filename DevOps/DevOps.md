# DevOps

DevOps — центральная область базы, но она не должна ссылаться на каждый инструмент подряд.

Правильная структура:

```text
DevOps
  -> область
    -> подотрасль
      -> инструмент / практика
        -> команды / диагностика / инциденты
```

Если каждая заметка ссылается прямо на DevOps, граф превращается в шум.

---

# Основные области DevOps

- [[Linux]] — ОС, процессы, systemd, права, filesystem, диагностика
- [[Network]] — IPv4/IPv6, DNS, TCP/UDP, routing, NAT, firewall, TLS, HTTP
- [[Containers]] — Docker, images, registry, compose, runtime security
- [[CI-CD]] — CI, delivery, deployment, GitOps, pipeline tools, rollback
- [[Kubernetes]] — workloads, services, ingress, probes, CNI, storage, RBAC
- [[Databases]] — PostgreSQL, Redis, MinIO, Ceph, backup/restore
- [[Infrastructure]] — серверы, SSH, Nginx, Terraform, Ansible, Cloudflare, Vault
- [[Observability]] — metrics, logs, traces, alerts, dashboards, SLO
- [[Security]] — secrets, hardening, WAF, supply chain, Kubernetes security
- [[Reliability and High Availability]] — HA, failover, DR, RTO/RPO, capacity
- [[Security DevSecOps]] — IAM, security gates in CI/CD, supply chain, policy automation
- [[Troubleshooting]] — runbook-и, симптомы, проверки, incident flow
- [[Programming for DevOps]] — Bash, Python, Go, YAML, CLI automation
- [[Practice Tasks]] — инциденты, лабораторные сценарии и проверка навыков

---

# Где находится GitOps

GitOps не отдельная верхнеуровневая область DevOps.

GitOps — это подход к [[Continuous Delivery]]:

```text
Git repository = desired state
controller watches Git/registry
controller reconciles cluster to desired state
drift is detected and corrected
```

Поэтому дерево такое:

```text
DevOps
  -> CI-CD
    -> Continuous Delivery
      -> GitOps
        -> FluxCD
        -> Argo CD
        -> Helm
        -> Kustomize
```

CI всё ещё нужен: он собирает, тестирует и публикует artifact/image.

GitOps начинается после этого: он доставляет уже проверенное состояние в окружение.

---

# Как добавлять новые знания

1. Найди правильную область.
2. Если это инструмент, положи его внутрь области или подотрасли.
3. В дочерней заметке ссылайся на родителя и ближайшие соседние темы.
4. Runbook-и держи в [[Troubleshooting]], но связывай с конкретной поломкой.
5. Не добавляй ссылку на [[DevOps]] в каждую заметку.
