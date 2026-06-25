# High CPU

High CPU — симптом, а не root cause.

Нужно понять, какой process/container/thread потребляет CPU и почему.

---

# Linux

```bash
top
htop
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head
pidstat 1
```

---

# Kubernetes

```bash
kubectl top pods -A
kubectl top nodes
kubectl describe pod <pod> -n <ns>
```

---

# Частые причины

```text
traffic spike
busy loop
GC pressure
crypto/compression
bad query
retry storm
log flood
no CPU limits/requests
```

---

# Связанные заметки

- [[Linux High CPU]]
- [[Resources Requests and Limits]]
- [[Capacity Planning]]
