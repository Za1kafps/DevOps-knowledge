# Grafana

`Grafana` — инструмент для dashboards, exploration и alert visualization.

Grafana не хранит все данные сама. Она подключается к data sources:

```text
Prometheus
Loki
Tempo/Jaeger
PostgreSQL
Cloud monitoring
```

---

# Хороший dashboard

Dashboard должен отвечать на конкретный вопрос.

Для сервиса:

```text
traffic
error rate
latency p50/p95/p99
saturation
deploy version
dependency errors
```

Для node:

```text
CPU
memory
disk
network
filesystem
load
```

---

# Переменные

Полезные variables:

```text
cluster
namespace
service
pod
environment
```

Не делай dashboard, где нужно руками редактировать PromQL.

---

# Частые ошибки

## Dashboard как wall of graphs

Много графиков без вопроса не помогает в incident.

## Нет links

Из metrics полезно переходить в logs/traces/runbook.

## Среднее вместо percentiles

Average latency скрывает p95/p99.

---

# Связанные заметки

- [[Prometheus]]
- [[PromQL]]
- [[Loki]]
- [[SLO]]
- [[Alertmanager]]
