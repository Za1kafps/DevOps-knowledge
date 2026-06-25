# Reliability and High Availability

[[Reliability and High Availability]] — область про то, как система продолжает работать при сбоях и как быстро восстанавливается.

Reliability — не “поставить 3 replicas”. Это свойства системы:

```text
failure tolerance
graceful degradation
fast recovery
capacity headroom
observability
tested rollback/restore
```

---

# Основные ветки

- [[High Availability]]
- [[SPOF]]
- [[RTO and RPO]]
- [[Disaster Recovery]]
- [[Failover]]
- [[Replication]]
- [[Healthchecks]]
- [[Graceful Shutdown]]
- [[Autoscaling]]
- [[Capacity Planning]]
- [[Rate Limiting]]

---

# Главные вопросы

```text
что будет, если упадёт один instance?
что будет, если упадёт node?
что будет, если потеряем zone?
сколько данных можно потерять?
за сколько надо восстановиться?
как понять, что система деградирует?
как откатить изменение?
```

---

# Reliability layers

```text
application: timeouts, retries, graceful shutdown
runtime: resources, probes, autoscaling
data: backups, replication, restore drills
network: load balancing, DNS, failover
ops: alerts, runbooks, incident process
```

---

# Частые ошибки

## HA без state

Три replicas приложения не спасают, если одна БД без backup.

## Autoscaling без limits/capacity

HPA может хотеть больше Pods, но cluster не имеет ресурсов.

## Backup без restore

Нет доказательства, что восстановление возможно.

---

# Связанные заметки

- [[Observability]]
- [[Databases]]
- [[Kubernetes]]
- [[Incident Response Flow]]
- [[SLO]]
