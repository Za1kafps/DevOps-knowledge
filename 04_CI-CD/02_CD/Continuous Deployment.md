# Continuous Deployment

`Continuous Deployment` — практика, где каждое изменение после успешных проверок автоматически попадает в production.

Это не просто job `deploy`.

Для continuous deployment нужны:

```text
надёжные tests
маленькие changes
автоматический rollback или быстрый manual rollback
observability
feature flags
progressive delivery
понятный ownership
```

---

# Отличие от Continuous Delivery

[[Continuous Delivery]]:

```text
artifact всегда готов к release
production deploy может ждать manual approval
```

Continuous Deployment:

```text
successful pipeline сам запускает production deploy
```

---

# Когда это уместно

Хорошо подходит:

```text
web services
маленькие изменения
сильная test suite
быстрый rollback
canary/blue-green
хорошие метрики и alerts
```

Плохо подходит без дополнительных процессов:

```text
опасные DB migrations
регулируемые среды
ручные QA gates
большие batch releases
низкое доверие к тестам
```

---

# Минимальный контроль

Перед автоматическим prod deploy должны быть:

```text
unit/integration tests
security checks по критичным правилам
image scan
immutable image tag/digest
rollout status check
smoke test
alerts на error rate/latency
rollback command
```

---

# Частые ошибки

## Автодеплой без rollback

Это не mature continuous deployment, а автоматизированный риск.

## Тесты слабые

Если CI почти ничего не проверяет, production становится тестовым окружением.

## Нет feature flags

Любое изменение поведения требует deploy/rollback, хотя можно было включать фичу отдельно.

---

# Связанные заметки

- [[Continuous Delivery]]
- [[Deployment Strategies]]
- [[Canary Deployment]]
- [[Blue Green Deployment]]
- [[Rollback]]
- [[Observability]]
