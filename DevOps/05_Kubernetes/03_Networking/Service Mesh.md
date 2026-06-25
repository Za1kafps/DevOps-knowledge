# Service Mesh

`Service Mesh` управляет service-to-service traffic внутри cluster.

Обычно использует sidecar или node/proxy dataplane.

---

# Что даёт

```text
mTLS между сервисами
traffic splitting
retries/timeouts
circuit breaking
observability
policy
```

---

# Когда нужен

Нужен, если много сервисов и требуется единый контроль east-west traffic.

Не нужен “просто потому что Kubernetes”: mesh добавляет complexity, latency и operational cost.

---

# Частые проблемы

```text
sidecar injection сломал Pod
mTLS policy блокирует traffic
retry storm
сложно debug-ить 503/timeout
resource overhead
```

---

# Связанные заметки

- [[Kubernetes Networking]]
- [[ZeroTrust]]
- [[TLS]]
- [[Observability]]
