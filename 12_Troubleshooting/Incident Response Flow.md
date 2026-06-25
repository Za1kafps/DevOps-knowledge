# Incident Response Flow

`Incident Response Flow` — порядок действий во время инцидента.

Цель — быстро снизить impact, не потерять факты и не устроить хаос.

---

# 1. Triage

Ответить:

```text
что сломалось?
когда началось?
сколько пользователей затронуто?
это outage или degradation?
какой severity?
```

---

# 2. Назначить роли

```text
incident commander
technical lead
communications
scribe
```

В маленькой команде один человек может совмещать роли, но ownership должен быть явным.

---

# 3. Стабилизировать

Сначала уменьшить impact:

```text
rollback
disable feature flag
scale up
route traffic away
restore config
rate limit
failover
```

Root cause можно искать глубже после стабилизации.

---

# 4. Собрать timeline

Фиксировать:

```text
время начала
alerts
deploys
config changes
симптомы
команды
решения
время восстановления
```

---

# 5. Postmortem

Postmortem должен давать actions:

```text
что произошло
почему detection не была раньше
почему impact был таким
что изменим в коде/инфре/process
какие runbooks обновить
```

Без blame. Но без размазывания ответственности.

---

# Частые ошибки

## Все одновременно чинят

Нужна координация.

## Нет communication

Пользователи и соседние команды не понимают status.

## Root cause ищут до rollback

Если impact высокий, сначала стабилизация.

---

# Связанные заметки

- [[Troubleshooting]]
- [[Rollback]]
- [[Observability]]
- [[Audit Logs]]
- [[Disaster Recovery]]
