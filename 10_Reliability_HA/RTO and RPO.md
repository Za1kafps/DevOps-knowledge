# RTO and RPO

`RTO` и `RPO` — две главные цифры disaster recovery.

```text
RTO = Recovery Time Objective
RPO = Recovery Point Objective
```

---

# RTO

RTO отвечает:

```text
за сколько времени сервис должен восстановиться?
```

Пример:

```text
RTO 30 минут
```

Значит после аварии сервис должен быть восстановлен максимум за 30 минут.

---

# RPO

RPO отвечает:

```text
сколько данных можно потерять?
```

Пример:

```text
RPO 5 минут
```

Значит допустимая потеря данных — не больше 5 минут.

---

# Как RPO связан с backup

Если backup раз в сутки, RPO не может быть 5 минут.

Для маленького RPO нужны:

```text
WAL archiving
replication
continuous backup
event streaming
```

---

# Как RTO связан с restore

Если restore базы занимает 4 часа, RTO не может быть 30 минут.

Нужно измерять restore time на реальных объёмах.

---

# Частые ошибки

## RTO/RPO не записаны

Тогда во время аварии все спорят ожиданиями.

## Цели не проверялись

На бумаге RTO 15 минут, restore drill занимает 2 часа.

## Один RTO для всех систем

Billing и staging wiki не требуют одинакового уровня.

---

# Связанные заметки

- [[Disaster Recovery]]
- [[Database Backups]]
- [[Database Restore Drill]]
- [[SLO]]
