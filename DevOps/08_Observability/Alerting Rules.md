# Alerting Rules

`Alerting Rules` — правила Prometheus, которые превращают PromQL выражения в alerts.

Alert должен звать человека только когда нужно действие.

---

# Пример

```yaml
groups:
  - name: app.rules
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{code=~"5.."}[5m]))
          /
          sum(rate(http_requests_total[5m])) > 0.05
        for: 10m
        labels:
          severity: page
        annotations:
          summary: "High 5xx error rate"
          runbook: "https://wiki/runbooks/high-error-rate"
```

---

# `for`

`for: 10m` означает, что условие должно держаться 10 минут.

Это защищает от коротких spikes.

---

# Severity

Пример:

```text
page     будить сейчас
ticket   создать задачу
info     не будить, только сигнал
```

Если всё page — ничего не page.

---

# Хорошие alerts

```text
симптомные, а не только причинные
связаны с impact
имеют runbook
имеют owner
не шумят на коротких spikes
учитывают traffic minimum
```

---

# Частые ошибки

## Alert на CPU без impact

Высокий CPU может быть нормальной нагрузкой.

## Нет `for`

Alert flapping.

## Нет labels для routing

Alertmanager не знает, куда отправлять.

---

# Связанные заметки

- [[Prometheus]]
- [[PromQL]]
- [[Alertmanager]]
- [[SLO]]
