# Linux Errno Codes

Errno codes — числовые ошибки системных вызовов Linux.

---

# Частые

```text
EACCES        permission denied
ENOENT        no such file or directory
EADDRINUSE    address already in use
ECONNREFUSED  connection refused
ETIMEDOUT     connection timed out
ENOSPC        no space left on device
ENOMEM        out of memory
EPIPE         broken pipe
```

---

# Где смотреть

```bash
man errno
strace -f -p <pid>
strace -f command
```

---

# Пример

`EADDRINUSE` при bind:

```bash
ss -lntp | grep ':8080'
```

`ENOSPC`:

```bash
df -h
df -i
```

---

# Связанные заметки

- [[DevOps/01_Linux/strace|strace]]
- [[Linux]]
- [[Troubleshooting]]
