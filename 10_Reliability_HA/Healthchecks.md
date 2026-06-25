# Healthchecks

`Healthcheck` — проверка состояния сервиса.

Healthcheck должен отвечать не “процесс существует?”, а “можно ли безопасно отправлять сюда traffic?”.

---

# Виды

## Liveness

Процесс жив или завис.

Если liveness падает, runtime может перезапустить процесс.

---

## Readiness

Сервис готов принимать traffic.

Если readiness падает, traffic надо убрать.

---

## Startup

Сервис ещё стартует и не должен быть убит liveness.

---

# Что проверять

Для readiness:

```text
app initialized
critical dependencies reachable
thread/event loop alive
minimum config loaded
```

Для liveness:

```text
process not deadlocked
main loop responsive
```

Не надо в liveness жёстко проверять внешнюю БД, иначе DB incident превратится в restart storm.

---

# HTTP endpoints

Обычно:

```text
/live
/ready
/health
```

Лучше разделять `/live` и `/ready`.

---

# Частые ошибки

## Healthcheck всегда 200

Он ничего не проверяет.

## Healthcheck слишком тяжёлый

Проверка сама нагружает систему.

## Нет timeout

Healthcheck зависает вместе с сервисом.

---

# Связанные заметки

- [[Kubernetes Probes]]
- [[Readiness Probe]]
- [[Liveness Probe]]
- [[Load Balancing]]
