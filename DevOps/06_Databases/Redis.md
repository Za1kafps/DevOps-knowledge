# Redis

`Redis` — in-memory data store.

Используется как:

```text
cache
session storage
rate limiter
queue/broker
distributed locks
leaderboard/counters
```

Redis быстрый, но из-за memory-first модели требует аккуратного отношения к persistence, eviction и replication.

---

# Проверка

```bash
redis-cli ping
redis-cli info
redis-cli info memory
redis-cli info stats
redis-cli info replication
```

Latency:

```bash
redis-cli --latency
redis-cli slowlog get 10
```

---

# Persistence

Основные варианты:

```text
RDB snapshot
AOF append-only file
RDB + AOF
no persistence
```

Смотри [[Redis Persistence]].

Если Redis используется только как cache, потеря данных может быть допустима.

Если Redis хранит sessions/queue, потеря уже может быть инцидентом.

---

# Memory и eviction

Проверить:

```bash
redis-cli info memory
redis-cli config get maxmemory
redis-cli config get maxmemory-policy
```

Eviction policy определяет, что Redis удалит при нехватке memory.

Опасно не знать policy в production.

---

# Replication

```bash
redis-cli info replication
```

Смотреть:

```text
role
connected_slaves
master_link_status
slave_repl_offset
master_repl_offset
```

Для HA смотри [[Redis Sentinel]] или [[Redis Cluster]].

---

# Частые проблемы

## Redis unavailable

Проверить process, port, auth, network, memory, logs.

## OOM command not allowed

Достигнут maxmemory, policy не позволяет удалить ключи.

## Slow commands

`KEYS *`, большие Lua scripts, большие values, blocking operations.

## Evicted keys

Cache может быть норм, sessions — нет.

---

# Связанные заметки

- [[Redis Persistence]]
- [[Redis Sentinel]]
- [[Redis Cluster]]
- [[Redis unavailable]]
- [[Rate Limiting]]
