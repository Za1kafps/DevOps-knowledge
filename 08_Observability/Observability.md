# Observability

[[Observability]] — область DevOps про понимание состояния системы по её внешним сигналам.

Три базовых сигнала:

```text
metrics
logs
traces
```

Но цель не “поставить Grafana”. Цель — быстро ответить:

```text
что сломалось?
когда началось?
кого затронуло?
какой слой виноват?
улучшается или деградирует?
```

---

# Основные ветки

- [[Metrics]]
- [[Logs]]
- [[Tracing]]
- [[Prometheus]]
- [[PromQL]]
- [[Alertmanager]]
- [[Alerting Rules]]
- [[Grafana]]
- [[Loki]]
- [[SLO]]
- [[node_exporter]]
- [[blackbox_exporter]]

---

# Golden signals

Для сервиса обычно смотрят:

```text
latency
traffic
errors
saturation
```

Для инфраструктуры:

```text
CPU
memory
disk
network
filesystem
load
process health
```

---

# Хороший alert

Alert должен быть actionable.

Плохой alert:

```text
CPU > 80%
```

Лучше:

```text
API error rate > 5% for 10m and traffic > minimum
```

Alert должен иметь:

```text
impact
threshold
duration
runbook
owner
severity
```

---

# Связанные заметки

- [[SLO]]
- [[Incident Response Flow]]
- [[Prometheus]]
- [[Grafana]]
- [[Loki]]
