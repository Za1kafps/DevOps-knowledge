# Cassandra

`Cassandra` — distributed wide-column database для больших write-heavy workloads.

---

# Что важно DevOps

```text
replication factor
consistency level
repair
compaction
tombstones
disk usage
node replacement
```

---

# Команды

```bash
nodetool status
nodetool info
nodetool tpstats
nodetool compactionstats
nodetool netstats
```

---

# Частые проблемы

```text
unbalanced ring
repair не запускается
много tombstones
disk full
high read latency
wrong consistency level
```

---

# Связанные заметки

- [[Databases]]
- [[Replication]]
- [[Capacity Planning]]
