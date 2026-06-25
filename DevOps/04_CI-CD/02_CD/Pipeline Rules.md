# Pipeline Rules

`Pipeline Rules` определяют, какие jobs запускаются для branch, merge request, tag или schedule.

Без rules pipeline либо делает слишком много, либо запускает опасные jobs не там.

---

# Что разделять

```text
merge request pipeline
branch pipeline
main pipeline
tag/release pipeline
scheduled pipeline
manual pipeline
```

Production deploy обычно должен быть доступен только для protected branch/tag.

---

# Примеры правил

Логика:

```text
MR: lint + tests
main: lint + tests + build + push image
tag: release + deploy production approval
schedule: nightly scans
```

---

# Protected environments

Для production нужны:

```text
protected branch/tag
protected variables
protected environment
limited approvers
audit trail
```

Иначе feature branch может получить production secrets.

---

# Частые ошибки

## Deploy job доступен из любой branch

Это прямой путь к случайному production deploy.

## Rules дублируются в каждом job

Лучше выносить общие правила в anchors/templates, если CI-система это поддерживает.

## Schedule запускает destructive job

Scheduled pipelines должны иметь отдельные guards.

---

# Связанные заметки

- [[CI-CD]]
- [[Continuous Integration]]
- [[Continuous Delivery]]
- [[Secrets in CI-CD]]
- [[Manual Approvals]]
