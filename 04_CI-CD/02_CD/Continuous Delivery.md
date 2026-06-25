# Continuous Delivery

`Continuous Delivery` — практика доставки проверенного artifact до окружения так, чтобы release можно было выполнить безопасно и повторяемо.

CD начинается после CI:

```text
CI: проверить и собрать
CD: доставить и подготовить release
```

CD не всегда означает автоматический production deploy. Может быть manual approval перед production, но сам процесс должен быть автоматизирован и воспроизводим.

---

# Что CD принимает на вход

CD не должен “собирать что-нибудь заново”.

Нормальные входы:

```text
image tag/digest
artifact version
helm chart version
manifests commit
release notes
migration plan
```

Если deploy job делает `docker build` прямо перед production deploy, граница CI/CD смешана.

---

# Что CD делает

Типовая цепочка:

```text
выбрать version
получить approval если нужен
применить конфигурацию
запустить rollout
дождаться readiness
проверить health/metrics/logs
сделать smoke tests
зафиксировать release
откатить при проблеме
```

---

# Способы delivery

## Push-based

Pipeline сам подключается к target и применяет изменения.

Примеры:

- [[Deploy via SSH]]
- [[Deploy via Docker Compose]]
- [[Deploy to Kubernetes]]
- [[Deploy via Helm]]

Плюсы:

```text
просто понять
меньше moving parts
подходит для маленьких проектов
```

Минусы:

```text
CI получает доступ к production
сложнее контролировать drift
сложнее audit desired state
```

---

## Pull-based GitOps

Controller внутри окружения сам подтягивает desired state из Git.

Смотри [[GitOps]], [[FluxCD]], [[Argo CD]].

Плюсы:

```text
Git как source of truth
меньше прямого доступа из CI в cluster
drift detection
удобный audit через commits
```

Минусы:

```text
нужна дисциплина repo structure
сложнее bootstrap
секреты надо решать отдельно
не все изменения удобно выражаются manifests
```

---

# Continuous Delivery vs Continuous Deployment

Continuous Delivery:

```text
release всегда можно выполнить
production может требовать manual approval
```

Continuous Deployment:

```text
каждое изменение после успешных проверок автоматически идёт в production
```

Смотри [[Continuous Deployment]].

---

# Rollback

CD без rollback — опасная кнопка deploy.

Rollback должен отвечать:

```text
какую версию вернуть?
как откатить конфиг?
что делать с миграциями БД?
как проверить, что откат помог?
```

Смотри [[Rollback]].

---

# Частые проблемы

## Deploy использует latest

Нельзя понять, что именно задеплоено.

Лучше:

```text
image tag = git sha / semver
deploy stores digest
```

---

## Нет health verification

Pipeline завершился успешно после `kubectl apply`, но приложение не стало Ready.

Нужно ждать rollout:

```bash
kubectl rollout status deploy/app -n production
```

---

## Миграции несовместимы с rollback

DB migration может сделать rollback приложения невозможным.

Нужны backward-compatible migrations.

---

# Связанные заметки

- [[CI-CD]]
- [[Continuous Integration]]
- [[Continuous Deployment]]
- [[Deployment Strategies]]
- [[Rollback]]
- [[GitOps]]
- [[Manual Approvals]]
