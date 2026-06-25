# Readiness Probe

`Readiness Probe` говорит Kubernetes, готов ли Pod принимать traffic.

Если readiness падает, Pod остаётся Running, но убирается из Service endpoints.

---

# Пример

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
  timeoutSeconds: 2
  failureThreshold: 3
```

---

# Что проверять

Readiness может проверять:

```text
приложение загрузило config
HTTP server принимает requests
critical dependency доступна
migrations завершены
worker готов брать jobs
```

Но probe не должна быть слишком тяжёлой.

---

# Диагностика

```bash
kubectl describe pod <pod> -n <ns>
kubectl get endpoints -n <ns>
kubectl get endpointslice -n <ns>
```

Ищи events:

```text
Readiness probe failed
```

---

# Частые ошибки

## Readiness всегда 200

Service отправляет traffic в неготовое приложение.

## Readiness проверяет слишком много

Краткий сбой dependency убирает все Pods из traffic.

## Нет readiness при rollout

Kubernetes считает Pod доступным раньше, чем приложение реально готово.

---

# Связанные заметки

- [[Kubernetes Probes]]
- [[Kubernetes Service]]
- [[Deployment]]
- [[Kubernetes Service No Endpoints]]
