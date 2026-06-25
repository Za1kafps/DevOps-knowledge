# Manual Approvals

`Manual Approval` — ручное подтверждение перед опасным этапом pipeline.

Approval нужен не “для бюрократии”, а когда автоматике не хватает контекста:

```text
production deploy
опасная migration
change freeze
security exception
дорогая инфраструктурная операция
```

---

# Где ставить approval

Хорошие места:

```text
перед production deploy
перед destructive migration
перед rollout на 100%
перед terraform apply
```

Плохое место:

```text
перед каждым dev deploy без причины
```

Так approval становится шумом.

---

# Что должен видеть approver

```text
commit range
artifact/image digest
environment
diff конфигурации
результаты tests/scans
release notes
rollback plan
```

Если approver нажимает кнопку вслепую, approval не добавляет безопасности.

---

# Частые ошибки

## Approval есть, информации нет

Нужно улучшать release summary.

## Все могут approve production

Нужны protected environments и роли.

## Approval обходится ручным deploy

Тогда pipeline не является source of truth.

---

# Связанные заметки

- [[Continuous Delivery]]
- [[Release Strategy]]
- [[Pipeline Rules]]
- [[Rollback]]
