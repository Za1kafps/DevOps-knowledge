# Tracing

`Tracing` показывает путь одного запроса через несколько сервисов.

Metrics говорят “есть проблема”, logs дают события, traces помогают понять, где именно запрос потратил время.

---

# Основные понятия

```text
trace  весь путь запроса
span   отдельная операция внутри trace
trace_id общий ID запроса
span_id ID операции
parent span связь между span
```

---

# Где полезно

```text
microservices
API gateway -> service -> database
очереди и async processing
поиск latency bottleneck
dependency timeout
```

---

# Что добавлять в spans

```text
service name
operation name
duration
status/error
http method/status
db statement type без sensitive data
peer service
```

---

# Частые ошибки

## Нет propagation

Trace обрывается между сервисами.

Нужно передавать trace context headers.

## Слишком много spans

Tracing сам начинает стоить дорого.

## Sensitive data в attributes

Не класть tokens/passwords/PII.

---

# Связанные заметки

- [[Logs]]
- [[Metrics]]
- [[Grafana]]
- [[SLO]]
