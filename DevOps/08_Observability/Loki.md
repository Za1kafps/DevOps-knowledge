# Loki

`Loki` — система хранения и запроса logs от Grafana Labs.

В отличие от Elasticsearch-подхода, Loki индексирует labels, а не полный текст log line.

---

# Как работает

```text
Promtail/agent collects logs
adds labels
sends to Loki
Loki stores chunks
Grafana queries with LogQL
```

---

# Labels

Хорошие labels:

```text
cluster
namespace
pod
container
app
environment
```

Плохие labels:

```text
request_id
user_id
trace_id
raw path with IDs
```

High cardinality labels ломают Loki.

---

# LogQL

Примеры:

```logql
{namespace="prod", app="api"}
{app="api"} |= "error"
{app="api"} | json | level="error"
```

Rate:

```logql
sum(rate({app="api"} |= "error" [5m]))
```

---

# Частые проблемы

## Логи не приходят

Проверить agent, labels, network, tenant, auth.

## Запросы медленные

Слишком широкий selector или плохие labels.

## Нет correlation с metrics/traces

Добавляй trace_id/request_id в log body, но не как Loki label.

---

# Связанные заметки

- [[Logs]]
- [[Grafana]]
- [[Tracing]]
- [[Incident Response Flow]]
