# Metrics

`Metrics` — числовые измерения состояния системы во времени.

Метрика отвечает на вопрос “сколько?”:

```text
сколько requests/sec
какой error rate
какая latency
сколько memory used
сколько disk free
```

---

# Типы метрик

```text
counter    только растёт
gauge      значение растёт и падает
histogram  распределение по buckets
summary    client-side quantiles
```

Counter используют с `rate()`:

```promql
rate(http_requests_total[5m])
```

Gauge читают напрямую:

```promql
node_memory_MemAvailable_bytes
```

---

# Labels

Labels дают разрезы:

```text
service="api"
method="GET"
code="500"
namespace="prod"
```

Опасно добавлять high-cardinality labels:

```text
user_id
request_id
raw_url
email
```

---

# RED и USE

Для сервисов:

```text
Rate
Errors
Duration
```

Для ресурсов:

```text
Utilization
Saturation
Errors
```

---

# Связанные заметки

- [[Prometheus]]
- [[PromQL]]
- [[SLO]]
- [[Alerting Rules]]
