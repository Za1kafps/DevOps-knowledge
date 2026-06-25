# PostgreSQL connection refused

`connection refused` означает, что TCP endpoint ответил отказом: на host:port никто не слушает или соединение отвергнуто.

---

# Проверка

```bash
pg_isready -h db.example.com -p 5432
nc -vz db.example.com 5432
ss -lntp | grep 5432
```

PostgreSQL:

```sql
show listen_addresses;
show port;
```

---

# Частые причины

```text
Postgres service down
listen_addresses только localhost
wrong port
container port не опубликован
Kubernetes Service targetPort wrong
firewall/security group reject
```

---

# Связанные заметки

- [[PostgreSQL]]
- [[Firewall]]
- [[Kubernetes Service]]
- [[Docker Network]]
