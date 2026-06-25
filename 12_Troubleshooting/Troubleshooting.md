# Troubleshooting

[[Troubleshooting]] — область runbook-ов и диагностики по симптомам.

Правило: сначала факты, потом гипотезы.

```text
симптом -> слой -> команды -> вывод -> следующее действие
```

---

# Базовый порядок

## 1. Зафиксировать симптом

```text
что именно не работает?
когда началось?
кого затронуло?
это полный outage или деградация?
что изменилось?
```

---

## 2. Определить слой

```text
DNS
network
TLS
HTTP/proxy
application
database
Kubernetes
CI/CD
storage
```

---

## 3. Собрать факты

Linux:

```bash
systemctl status service
journalctl -u service -n 200
ss -lntp
df -h
free -m
```

Network:

```bash
dig domain.com
curl -v https://domain.com
tcpdump -i any port 443
```

Kubernetes:

```bash
kubectl get pods -A
kubectl describe pod pod -n ns
kubectl get events -n ns --sort-by=.lastTimestamp
```

---

# Runbooks

- [[Incident Response Flow]]
- [[DNS Failure]]
- [[Ingress 502]]
- [[Nginx 502]]
- [[ImagePullBackOff]]
- [[Kubernetes CrashLoopBackOff]]
- [[Pod Pending]]
- [[PVC Pending]]
- [[OOMKilled]]
- [[PostgreSQL Too Many Connections]]
- [[PostgreSQL connection refused]]
- [[Redis unavailable]]
- [[TLS certificate expired]]
- [[Docker Build Failed]]
- [[Docker Container Cannot Connect]]
- [[GitLab CI Deploy Target DNS Error]]

---

# Частые ошибки диагностики

## Прыгать сразу к fix

Без фактов легко чинить не тот слой.

## Не проверять последние изменения

Большинство инцидентов начинается после deploy/config change/infra change.

## Не записывать выводы

Если причина не попала в runbook, команда повторит расследование позже.

---

# Связанные заметки

- [[Observability]]
- [[Incident Response Flow]]
- [[Linux]]
- [[Network]]
- [[Kubernetes]]
