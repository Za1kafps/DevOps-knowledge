# Kubernetes Probes

Kubernetes probes помогают kubelet понять состояние container.

Основные probes:

- [[Startup Probe]]
- [[Readiness Probe]]
- [[Liveness Probe]]

---

# Startup Probe

Проверяет, что приложение стартовало.

Пока startupProbe не прошла, liveness/readiness не мешают.

Полезна для приложений с долгим cold start.

---

# Readiness Probe

Проверяет, можно ли отправлять traffic в Pod.

Если readiness падает, Pod убирается из Service endpoints.

---

# Liveness Probe

Проверяет, жив ли процесс.

Если liveness падает несколько раз, kubelet перезапускает container.

---

# Типы probes

HTTP:

```yaml
httpGet:
  path: /ready
  port: 8080
```

TCP:

```yaml
tcpSocket:
  port: 5432
```

Exec:

```yaml
exec:
  command: ["sh", "-c", "test -f /tmp/ready"]
```

---

# Частые ошибки

## Liveness проверяет dependency

Если DB недоступна, liveness убивает приложение и создаёт restart storm.

Dependency обычно проверяют в readiness, не liveness.

## Одинаковая readiness и liveness

Это часто неправильно. “Не готов принимать traffic” не равно “надо перезапустить”.

## Слишком маленькие timeouts

Под нагрузкой probes начинают падать и сами создают инцидент.

---

# Связанные заметки

- [[Startup Probe]]
- [[Readiness Probe]]
- [[Liveness Probe]]
- [[Kubernetes Service]]
- [[Kubernetes CrashLoopBackOff]]
