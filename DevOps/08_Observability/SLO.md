# SLO

`SLO` — Service Level Objective, целевой уровень надёжности сервиса.

SLO нужен, чтобы говорить о reliability численно, а не “кажется, сервис норм”.

---

# Термины

```text
SLI  что измеряем
SLO  какой target хотим
SLA  внешний договор/обязательство
error budget сколько ошибок можно потратить
```

Пример:

```text
SLI: доля успешных HTTP requests
SLO: 99.9% successful requests за 30 дней
```

---

# Error budget

Если SLO 99.9%, допустимая ошибка:

```text
0.1% за окно
```

Error budget помогает принимать решения:

```text
можно ли ускорять releases
надо ли остановить risky changes
нужно ли инвестировать в reliability
```

---

# Хороший SLI

SLI должен быть близок к user experience.

Для API:

```text
availability = successful requests / total valid requests
latency = процент requests быстрее threshold
```

Для queue:

```text
processing delay
failed jobs rate
queue lag
```

---

# Alerting по SLO

Лучше alert-ить не просто на факт нарушения, а на burn rate error budget.

Идея:

```text
если error budget сгорает слишком быстро, page
если медленно деградирует, ticket
```

---

# Частые ошибки

## SLO на внутреннюю метрику

CPU не SLO. CPU может быть причиной, но user impact измеряется иначе.

## 100% SLO

Обычно невозможно и слишком дорого.

## Нет ownership

SLO без владельца не меняет поведение команды.

---

# Связанные заметки

- [[Observability]]
- [[Prometheus]]
- [[Alerting Rules]]
- [[Reliability and High Availability]]
