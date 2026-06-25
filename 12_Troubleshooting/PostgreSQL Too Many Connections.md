# PostgreSQL Too Many Connections

`too many connections` означает, что PostgreSQL достиг `max_connections`.

---

# Проверка

```sql
show max_connections;

select state, count(*)
from pg_stat_activity
group by state;

select usename, application_name, client_addr, state, count(*)
from pg_stat_activity
group by usename, application_name, client_addr, state
order by count desc;
```

---

# Частые причины

```text
нет PgBouncer
слишком большой pool в приложении
connection leak
много idle connections
idle in transaction
слишком много replicas
```

---

# Быстрые меры

```text
уменьшить app pool size
включить PgBouncer
убить явно зависшие sessions осторожно
scale down noisy service
найти leak
```

Убить session:

```sql
select pg_terminate_backend(pid)
from pg_stat_activity
where state = 'idle'
  and now() - state_change > interval '1 hour';
```

---

# Связанные заметки

- [[PostgreSQL]]
- [[PgBouncer]]
- [[Connection Pool]]
- [[Database Monitoring]]
