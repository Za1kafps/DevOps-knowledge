# Redis unavailable

Redis unavailable — приложение не может подключиться к Redis или Redis не отвечает.

---

# Проверка

```bash
redis-cli -h redis -p 6379 ping
redis-cli -h redis info
nc -vz redis 6379
```

На сервере:

```bash
systemctl status redis
journalctl -u redis -n 100
ss -lntp | grep 6379
```

---

# Частые причины

```text
Redis down
wrong host/port
auth required
maxmemory/OOM
protected-mode/bind
network/firewall
Sentinel failover client не понял
```

---

# Связанные заметки

- [[Redis]]
- [[Redis Sentinel]]
- [[Firewall]]
- [[Connection Pool]]
