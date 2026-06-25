# Alertmanager

`Alertmanager` принимает alerts от Prometheus и решает, куда их отправить.

Он отвечает за:

```text
grouping
routing
deduplication
silences
inhibition
notifications
```

---

# Routing

Alerts маршрутизируются по labels:

```text
severity
team
service
environment
```

Пример логики:

```text
severity=page -> PagerDuty
severity=ticket -> issue tracker
environment=dev -> Slack only
```

---

# Silences

Silence временно подавляет alerts.

Использовать для maintenance, но не как способ “починить” шумный alert.

---

# Inhibition

Inhibition подавляет вторичные alerts.

Пример:

```text
если NodeDown, не слать 50 PodDown с этой node
```

---

# Частые ошибки

## Нет labels для routing

Все alerts летят всем.

## Silence без срока

Alert исчезает навсегда.

## Нет grouping

Один инцидент создаёт сотни notifications.

---

# Связанные заметки

- [[Prometheus]]
- [[Alerting Rules]]
- [[Incident Response Flow]]
