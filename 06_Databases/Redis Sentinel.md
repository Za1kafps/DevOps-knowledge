# Redis Sentinel

`Redis Sentinel` обеспечивает monitoring и automatic failover для Redis primary/replica схемы.

---

# Что делает Sentinel

```text
следит за primary
определяет failure
выбирает replica для promotion
перенастраивает replicas
даёт clients актуальный primary address
```

---

# Проверка

```bash
redis-cli -p 26379 sentinel masters
redis-cli -p 26379 sentinel replicas mymaster
redis-cli -p 26379 sentinel get-master-addr-by-name mymaster
```

---

# Важные понятия

```text
quorum
down-after-milliseconds
failover-timeout
parallel-syncs
```

Quorum нужен, чтобы несколько Sentinel согласились, что primary недоступен.

---

# Частые проблемы

## Client не умеет Sentinel

После failover приложение продолжает ходить на старый primary.

## Split brain

Network partition и неверные настройки могут привести к двум primary.

## Данные теряются при async replication

Redis replication асинхронная.

---

# Связанные заметки

- [[Redis]]
- [[Failover]]
- [[High Availability]]
