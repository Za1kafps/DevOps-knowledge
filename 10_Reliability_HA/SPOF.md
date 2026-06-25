# SPOF

`SPOF` — Single Point of Failure.

Это компонент, отказ которого ломает всю систему или критичный путь.

---

# Примеры

```text
одна БД без replica/backup
один load balancer
одна VM с приложением
один DNS provider
один NAT gateway
один CI runner для production deploy
один человек с доступом
```

---

# Как искать SPOF

Пройти путь запроса:

```text
DNS -> LB -> proxy -> app -> DB -> cache -> external API
```

Для каждого узла спросить:

```text
что будет, если он исчезнет?
есть ли failover?
сколько займёт recovery?
потеряем ли данные?
```

---

# Не все SPOF одинаковы

Иногда SPOF допустим, если:

```text
низкий impact
быстрый restore
дешевле принять риск
есть backup/manual workaround
```

Но риск должен быть записан.

---

# Связанные заметки

- [[High Availability]]
- [[Disaster Recovery]]
- [[RTO and RPO]]
- [[Failover]]
