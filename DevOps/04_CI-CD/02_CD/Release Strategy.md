# Release Strategy

`Release Strategy` — правила, по которым изменения попадают к пользователям.

Deploy и release — не одно и то же.

```text
deploy  новая версия установлена в окружение
release новая возможность доступна пользователям
```

Feature flags позволяют задеплоить код, но включить поведение позже.

---

# Что входит в release strategy

```text
versioning
branch/tag policy
approval process
deployment strategy
feature flags
migration strategy
rollback plan
release notes
communication
```

---

# Versioning

Частые варианты:

```text
semver
calendar versioning
git sha tags
build numbers
```

Для container deploy важно знать exact image:

```text
registry/app:1.2.3
registry/app@sha256:...
```

---

# Promotion

Promotion — продвижение одной и той же версии через окружения:

```text
dev -> stage -> production
```

Важно: production должен получать тот же artifact, а не пересобранный заново.

---

# Migrations

DB migrations должны быть совместимы с rollout/rollback.

Безопасная схема:

```text
expand schema
deploy app compatible with old/new schema
backfill
switch reads/writes
contract old schema later
```

---

# Связанные заметки

- [[Continuous Delivery]]
- [[Deployment Strategies]]
- [[Rollback]]
- [[Manual Approvals]]
- [[Database Migrations]]
