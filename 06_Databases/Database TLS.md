# Database TLS

`Database TLS` шифрует connection между client и database.

Нужно для traffic через недоверенные сети, compliance и защиты credentials/data in transit.

---

# Что проверять

```text
TLS включён на server
client требует TLS
certificate chain валидна
hostname проверяется
старые TLS versions отключены
```

---

# PostgreSQL

Проверить SSL:

```sql
select ssl, version, cipher
from pg_stat_ssl
where pid = pg_backend_pid();
```

Подключение:

```bash
psql "host=db.example.com dbname=app sslmode=verify-full"
```

`sslmode=require` шифрует, но не проверяет hostname как `verify-full`.

---

# Частые проблемы

```text
self-signed CA не доверен client
certificate expired
hostname mismatch
sslmode disabled/prefer
intermediate certificate missing
```

---

# Связанные заметки

- [[TLS]]
- [[PostgreSQL]]
- [[Secrets Management]]
