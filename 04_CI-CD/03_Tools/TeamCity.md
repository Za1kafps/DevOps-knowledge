# TeamCity

`TeamCity` — CI/CD сервер JetBrains.

Используется для build pipelines, test reports, artifacts, deployment jobs и интеграций с VCS.

---

# Основные части

```text
server
build agents
projects
build configurations
VCS roots
build steps
artifacts
parameters/secrets
```

---

# Что важно

```text
agents должны быть воспроизводимыми
build configurations лучше хранить как code
secrets должны быть scoped
artifacts должны публиковаться явно
deploy jobs должны иметь approvals/permissions
```

---

# Kotlin DSL

TeamCity умеет хранить конфигурацию pipeline как Kotlin DSL в Git.

Это лучше, чем полностью ручная настройка через UI, потому что изменения review-ятся.

---

# Частые проблемы

## Agent requirements mismatch

Build ждёт agent с нужным tool/os/tag, но такого нет.

## Artifact не опубликован

Следующий step/deploy не должен брать файлы из случайного workspace.

## Secrets видны в logs

Проверять masking и verbose команды.

---

# Связанные заметки

- [[CI-CD]]
- [[Continuous Integration]]
- [[Artifacts and Cache]]
- [[Secrets in CI-CD]]
