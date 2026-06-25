# Liveness Probe

`Liveness Probe` проверяет, жив ли container.

Если liveness падает несколько раз подряд, kubelet перезапускает container.

---

# Пример

```yaml
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
  timeoutSeconds: 2
  failureThreshold: 3
```

---

# Что проверять

Liveness должна отвечать на вопрос:

```text
процесс завис так, что restart поможет?
```

Обычно не надо проверять внешние dependencies вроде PostgreSQL. Если DB недоступна, restart приложения не чинит DB.

---

# Диагностика

```bash
kubectl describe pod <pod> -n <ns>
kubectl logs <pod> -n <ns> --previous
```

Events:

```text
Liveness probe failed
Killing container
Back-off restarting failed container
```

---

# Частые ошибки

## Liveness слишком агрессивная

Под нагрузкой приложение отвечает медленнее, probe падает, kubelet перезапускает container и усиливает инцидент.

## Liveness = readiness

Не готов принимать traffic не значит “надо убить процесс”.

## Нет startupProbe

Долгий старт приложения воспринимается как deadlock.

---

# Связанные заметки

- [[Kubernetes Probes]]
- [[Startup Probe]]
- [[Kubernetes CrashLoopBackOff]]
- [[Healthchecks]]
