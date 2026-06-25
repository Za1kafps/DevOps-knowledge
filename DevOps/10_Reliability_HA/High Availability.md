# High Availability

`High Availability` — способность системы оставаться доступной при отказе отдельных компонентов.

HA достигается не одной настройкой, а комбинацией:

```text
redundancy
load balancing
health checks
failover
replication
failure domain isolation
automation
```

---

# Failure domains

Failure domain — область, которая может отказать целиком:

```text
process
node
rack
zone
region
cloud provider
```

Если все replicas на одной node, это не HA.

---

# Stateless services

Для stateless:

```text
несколько replicas
readiness probes
load balancer
rolling updates
PDB
anti-affinity/topology spread
```

---

# Stateful services

Для stateful:

```text
replication
quorum
backups
restore drills
failover procedure
split-brain protection
```

Stateful HA сложнее, чем replicas приложения.

---

# Проверка

Хороший вопрос:

```text
что конкретно произойдёт, если выключить этот node?
```

Проверяется через game day/chaos drill, а не через diagram.

---

# Связанные заметки

- [[SPOF]]
- [[Failover]]
- [[Replication]]
- [[PodDisruptionBudget]]
- [[Load Balancing]]
