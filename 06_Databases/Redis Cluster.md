# Redis Cluster

`Redis Cluster` шардирует данные между несколькими Redis nodes.

Он нужен для horizontal scaling и распределения keyspace.

---

# Как работает

Redis Cluster делит keyspace на hash slots:

```text
0..16383
```

Каждый primary отвечает за часть slots, replicas используются для отказоустойчивости.

---

# Проверка

```bash
redis-cli -c -h node1 cluster info
redis-cli -c -h node1 cluster nodes
redis-cli -c -h node1 cluster slots
```

---

# Важные ограничения

```text
multi-key операции требуют keys в одном hash slot
client должен поддерживать cluster redirects
resharding требует аккуратности
replication async
```

Hash tag:

```text
user:{123}:profile
user:{123}:sessions
```

---

# Связанные заметки

- [[Redis]]
- [[Redis Sentinel]]
- [[High Availability]]
- [[Capacity Planning]]
