# Deployment Strategies

`Deployment Strategies` — способы выкатить новую версию приложения с контролем риска.

Стратегия нужна, потому что “заменить всё сразу” часто опасно.

---

# Основные стратегии

- [[Rolling Update]]
- [[Blue Green Deployment]]
- [[Canary Deployment]]
- [[Preview Environments]]

# Rolling update

Постепенная замена pod/instance.

Плюсы:

```text
просто
экономит ресурсы
поддерживается Kubernetes Deployment
```

Минусы:

```text
old и new версии работают одновременно
rollback не мгновенный
нужна backward compatibility
```

Проверка:

```bash
kubectl rollout status deploy/app -n production
kubectl rollout history deploy/app -n production
```

---

# Blue-green

Есть две среды:

```text
blue  старая active
green новая idle/candidate
```

После проверки traffic переключается на green.

Смотри [[Blue Green Deployment]].

---

# Canary

Новая версия получает малую долю traffic.

Пример:

```text
1% -> 5% -> 25% -> 50% -> 100%
```

Смотри [[Canary Deployment]].

---

# Что выбрать

Rolling update:

```text
обычный stateless service
совместимые версии
нет сложного traffic control
```

Blue-green:

```text
нужен быстрый rollback
можно держать две среды
важна предварительная проверка
```

Canary:

```text
есть метрики качества
можно маршрутизировать traffic
нужно снижать blast radius
```

---

# Связанные заметки

- [[Continuous Delivery]]
- [[Release Strategy]]
- [[Rollback]]
- [[Kubernetes Probes]]
- [[Load Balancing]]
