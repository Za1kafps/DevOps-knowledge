# Transactions

`Transaction` — группа операций БД, которая выполняется как единое логическое действие.

Классические свойства — ACID:

```text
Atomicity
Consistency
Isolation
Durability
```

---

# PostgreSQL

```sql
begin;
update accounts set balance = balance - 100 where id = 1;
update accounts set balance = balance + 100 where id = 2;
commit;
```

Откат:

```sql
rollback;
```

---

# Isolation

Уровни:

```text
read committed
repeatable read
serializable
```

Чем выше isolation, тем меньше anomalies, но выше цена конфликтов/locks.

---

# Частые проблемы

```text
idle in transaction
долгие locks
deadlocks
transaction слишком большая
migration держит lock
```

Проверить долгие транзакции:

```sql
select pid, now() - xact_start as age, state, query
from pg_stat_activity
where xact_start is not null
order by age desc;
```

---

# Связанные заметки

- [[PostgreSQL]]
- [[Database Migrations]]
- [[Indexes]]
