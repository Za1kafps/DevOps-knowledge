# Startup Probe

`Startup Probe` проверяет, успело ли приложение стартовать.

Пока startupProbe не успешна, kubelet не применяет liveness/readiness failures к container.

---

# Когда нужна

```text
долгий cold start
JVM прогрев
миграции/инициализация
большой cache warmup
старое приложение с непредсказуемым стартом
```

---

# Пример

```yaml
startupProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 5
  failureThreshold: 30
```

Это даёт до 150 секунд на старт.

---

# Частые ошибки

## Компенсируют startup через liveness initialDelay

StartupProbe гибче: после старта liveness может быть строгой.

## Слишком маленький failureThreshold

Приложение убивается до завершения нормального старта.

---

# Связанные заметки

- [[Kubernetes Probes]]
- [[Liveness Probe]]
- [[Readiness Probe]]
