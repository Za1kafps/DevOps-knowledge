# Blue Green Deployment

`Blue-green deployment` — стратегия, где есть две версии окружения.

```text
blue   текущая active
green  новая candidate
```

Traffic переключается с blue на green после проверки.

---

# Как работает

```text
1. blue обслуживает пользователей
2. green разворачивается рядом
3. green проверяется smoke/e2e/health
4. load balancer переключает traffic на green
5. blue некоторое время держат для rollback
```

---

# Плюсы

```text
быстрый rollback
новую версию можно проверить до traffic
понятная модель
```

---

# Минусы

```text
нужно держать двойные ресурсы
сложнее с stateful services
DB migrations должны быть совместимы
есть риск split-brain traffic
```

---

# Где переключается traffic

```text
load balancer
ingress
service selector
DNS
API gateway
service mesh
```

DNS-переключение хуже для быстрого rollback из-за TTL/cache.

---

# Частые ошибки

## Green проверили без реального traffic path

Health endpoint работает, но реальный route через LB/Ingress нет.

## DB migration несовместима с blue

После переключения назад старая версия не может работать с новой schema.

## Blue удалили сразу

Rollback стал долгим.

---

# Связанные заметки

- [[Deployment Strategies]]
- [[Load Balancing]]
- [[Rollback]]
- [[Database Migrations]]
