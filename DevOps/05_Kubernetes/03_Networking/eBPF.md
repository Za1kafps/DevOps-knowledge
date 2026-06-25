# eBPF

`eBPF` — механизм Linux kernel для безопасного запуска программ в kernel hooks.

В Kubernetes eBPF часто используют для networking, observability и security.

---

# Где встречается

```text
Cilium dataplane
service load balancing
network policy enforcement
packet tracing
runtime security
```

---

# Почему полезно

```text
меньше iptables complexity
быстрый dataplane
видимость network flows
гибкие policy hooks
```

---

# Ограничения

```text
зависимость от kernel version/features
сложнее debug
нужно понимать конкретный CNI/tool
```

---

# Связанные заметки

- [[Cilium]]
- [[CNI]]
- [[Kubernetes Networking]]
- [[Security]]
