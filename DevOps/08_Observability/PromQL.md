# PromQL

`PromQL` — query language Prometheus.

PromQL нужен для dashboards, alerts и ad-hoc диагностики.

---

# Базовые функции

Counter rate:

```promql
rate(http_requests_total[5m])
```

Increase за окно:

```promql
increase(http_requests_total[1h])
```

Gauge:

```promql
node_memory_MemAvailable_bytes
```

Aggregation:

```promql
sum by (job) (rate(http_requests_total[5m]))
```

---

# Error rate

```promql
sum(rate(http_requests_total{code=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
```

Лучше добавлять группировку:

```promql
sum by (service) (rate(http_requests_total{code=~"5.."}[5m]))
/
sum by (service) (rate(http_requests_total[5m]))
```

---

# Latency histogram

p95:

```promql
histogram_quantile(
  0.95,
  sum by (le, service) (rate(http_request_duration_seconds_bucket[5m]))
)
```

Важно: histogram buckets должны быть нормальными для твоих latency.

---

# Частые ошибки

## rate без window

`rate(metric)` невозможно, нужен range vector:

```promql
rate(metric[5m])
```

## avg latency вместо percentile

Average скрывает tail latency.

## Деление без matching labels

PromQL vector matching может дать пустой или неверный результат.

## high cardinality labels

Запросы становятся медленными, storage растёт.

---

# Связанные заметки

- [[Prometheus]]
- [[Alerting Rules]]
- [[SLO]]
- [[Metrics]]
