# Linux High CPU

Linux High CPU разбирают от host к process/thread.

---

# Команды

```bash
uptime
top
htop
mpstat -P ALL 1
pidstat 1
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -20
```

Thread-level:

```bash
top -H -p <pid>
```

---

# Что отличать

```text
user CPU
system CPU
iowait
steal
load average
```

Высокий load не всегда CPU: это могут быть процессы в ожидании IO.

---

# Частые причины

```text
traffic spike
bad release
infinite loop
expensive query
log/regex processing
crypto/compression
container noisy neighbor
```

---

# Связанные заметки

- [[High CPU]]
- [[Load average]]
- [[Linux Processes]]
