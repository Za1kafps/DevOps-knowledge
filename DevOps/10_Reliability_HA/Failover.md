# Failover

`Failover` — переключение traffic/role на резервный компонент при отказе primary.

---

# Где бывает

```text
database primary -> replica
load balancer active -> standby
DNS to secondary region
Redis primary -> replica via Sentinel
Kubernetes reschedules Pods to another node
```

---

# Что важно

```text
detection
decision
promotion
traffic switch
fencing old primary
data consistency
rollback/failback
```

---

# Split-brain

Split-brain — ситуация, когда две стороны считают себя primary.

Для stateful systems это может привести к потере или конфликту данных.

Нужны quorum/fencing/clear ownership.

---

# Проверка failover

Failover должен быть протестирован drill-ом:

```text
сколько занял
были ли потеряны данные
как клиенты переподключились
что было с DNS/cache
```

---

# Связанные заметки

- [[High Availability]]
- [[Replication]]
- [[RTO and RPO]]
- [[Disaster Recovery]]
