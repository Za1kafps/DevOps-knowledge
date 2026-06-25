# Redis Persistence

Redis хранит данные в memory, но может сохранять их на диск.

Persistence режим должен соответствовать роли Redis.

---

# RDB

RDB — snapshot через интервалы.

Плюсы:

```text
компактный файл
быстрый restart
хорош для backup snapshots
```

Минусы:

```text
можно потерять данные после последнего snapshot
fork может быть дорогим
```

---

# AOF

AOF — append-only log команд.

Плюсы:

```text
меньше потеря данных
лучше durability
```

Минусы:

```text
файл больше
нужен rewrite
может влиять на latency
```

---

# Проверка

```bash
redis-cli config get save
redis-cli config get appendonly
redis-cli info persistence
```

---

# Частые ошибки

## Redis как queue без persistence

Restart теряет jobs.

## AOF включён, но диск медленный

Latency растёт.

## Нет backup RDB/AOF

Persistence не заменяет backup.

---

# Связанные заметки

- [[Redis]]
- [[Backup Strategy]]
- [[Disaster Recovery]]
