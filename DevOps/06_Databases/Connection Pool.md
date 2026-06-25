# Connection Pool

`Connection Pool` переиспользует соединения с БД вместо создания нового connection на каждый запрос.

---

# Зачем нужен

PostgreSQL connection дорогой.

Без pooling:

```text
много Pod replicas
каждая держит pool
max_connections заканчивается
DB тратит memory на idle clients
```

---

# Где бывает pool

```text
в приложении
PgBouncer
managed DB proxy
JDBC/HikariCP
SQLAlchemy pool
```

---

# Что считать

```text
replicas * pool_size <= допустимые DB connections
```

Если 20 Pods и pool по 20, это уже 400 возможных connections.

---

# Симптомы проблем

```text
too many connections
connection timeout
idle in transaction
DB memory pressure
slow acquire connection
```

---

# Связанные заметки

- [[PgBouncer]]
- [[PostgreSQL]]
- [[PostgreSQL Too Many Connections]]
- [[Capacity Planning]]
