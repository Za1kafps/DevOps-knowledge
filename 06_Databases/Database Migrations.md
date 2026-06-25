# Database Migrations

`Database Migration` — управляемое изменение schema/data.

Миграции опасны тем, что код можно откатить быстро, а данные — не всегда.

---

# Главный принцип

Production migrations должны быть backward-compatible.

Безопасный паттерн:

```text
expand
deploy compatible code
backfill
switch reads/writes
contract
```

---

# Пример опасного изменения

Плохо:

```sql
alter table users rename column name to full_name;
```

Старый код сразу сломается.

Лучше:

```text
1. add full_name
2. write both name and full_name
3. backfill
4. read full_name
5. later drop name
```

---

# Locks

DDL может брать locks и блокировать production queries.

Перед миграцией проверять:

```sql
select pid, locktype, relation::regclass, mode, granted
from pg_locks
where not granted;
```

Долгие транзакции:

```sql
select pid, now() - xact_start as age, state, query
from pg_stat_activity
where xact_start is not null
order by age desc;
```

---

# Indexes

В PostgreSQL для больших таблиц:

```sql
create index concurrently idx_users_email on users(email);
```

Обычный `create index` может блокировать writes.

`CONCURRENTLY` дольше и имеет ограничения, но безопаснее для production.

---

# Rollback

Не каждая миграция откатываема.

Перед apply нужно знать:

```text
можно ли откатить код
можно ли откатить schema
потеряются ли данные
сколько займёт rollback
```

---

# Частые ошибки

## Migration запускается на старте каждого Pod

При нескольких replicas миграции могут стартовать параллельно.

Лучше отдельный Job/step с locking.

## Нет timeout

Migration висит и держит lock.

## Down migration разрушает данные

Автоматический rollback может сделать хуже.

---

# Связанные заметки

- [[PostgreSQL]]
- [[Transactions]]
- [[Indexes]]
- [[Release Strategy]]
- [[Rollback]]
