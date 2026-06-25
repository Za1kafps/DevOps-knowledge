# Capacity Planning

`Capacity Planning` — планирование ресурсов до того, как они закончатся.

Нужно понимать:

```text
текущую нагрузку
рост
лимиты системы
headroom
стоимость
время добавления capacity
```

---

# Что планировать

```text
CPU
memory
disk
IOPS
network
database connections
queue throughput
Kubernetes nodes
IP addresses
object storage
```

---

# Headroom

Headroom — запас до лимита.

Пример:

```text
normal load 40%
peak load 70%
emergency headroom 30%
```

Без headroom autoscaling и failover могут не сработать.

---

# Проверки

```text
что будет при x2 traffic?
что будет при потере одной zone?
сколько места останется через 30 дней?
сколько connections откроют все replicas?
```

---

# Частые ошибки

## Считать только average

Нужно смотреть peak и p95/p99.

## Игнорировать лимиты зависимостей

App масштабируется, БД нет.

## Нет прогноза disk growth

Disk full остаётся одним из самых тупых и частых инцидентов.

---

# Связанные заметки

- [[Autoscaling]]
- [[Metrics]]
- [[Database Monitoring]]
- [[SLO]]
