# Prometheus

`Prometheus` — time series database и monitoring system.

Он собирает metrics через pull-модель: сам ходит на targets и scrape-ит `/metrics`.

---

# Как работает

```text
targets expose /metrics
Prometheus scrapes targets
samples stored as time series
PromQL queries data
rules create alerts/recording series
Alertmanager sends notifications
Grafana visualizes
```

---

# Target

Проверить targets:

```text
Status -> Targets в UI
```

Через API:

```bash
curl http://prometheus:9090/api/v1/targets
```

---

# Метрика

Формат:

```text
http_requests_total{method="GET",code="200"} 12345
```

Имя + labels = time series.

Осторожно с labels: high cardinality убивает Prometheus.

---

# Типы метрик

```text
counter    только растёт
gauge      может расти/падать
histogram  buckets для latency/size
summary    client-side quantiles
```

Для latency в Prometheus чаще используют histogram.

---

# Prometheus в Kubernetes

Обычно ставят через kube-prometheus-stack/Prometheus Operator.

Появляются CRD:

```text
ServiceMonitor
PodMonitor
PrometheusRule
AlertmanagerConfig
```

---

# Частые проблемы

## target down

Проверить endpoint, DNS, NetworkPolicy, ServiceMonitor labels.

## много cardinality

Labels типа `user_id`, `request_id`, `path` с raw IDs создают слишком много series.

## Prometheus disk full

Проверить retention, ingestion rate, cardinality.

---

# Связанные заметки

- [[PromQL]]
- [[Alerting Rules]]
- [[Alertmanager]]
- [[Grafana]]
- [[Metrics]]
