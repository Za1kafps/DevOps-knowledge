# CI-CD

[[CI-CD]] — область DevOps про путь изменения от commit до production.

Главная идея:

```text
изменение должно быть проверено, собрано, доставлено, задеплоено и откатываемо
```

CI/CD — это не один YAML-файл. Это цепочка контроля качества, артефактов, секретов, окружений, deploy-стратегий и rollback.

---

# Правильное разделение

## CI

[[Continuous Integration]] отвечает за проверку изменения.

Обычно:

```text
checkout
install deps
lint
unit tests
integration tests
build
security scans
publish artifact/image
```

CI должен ответить:

```text
можно ли доверять этому commit?
какой artifact/image получился?
где он лежит?
какой digest/version надо деплоить?
```

---

## CD

[[Continuous Delivery]] отвечает за доставку проверенного artifact в окружение.

Обычно:

```text
choose version
apply manifests/chart/compose
run migrations if needed
wait health/readiness
verify metrics/logs
rollback if failed
```

---

## Continuous Deployment

[[Continuous Deployment]] — частный случай CD, когда deploy в production происходит автоматически после успешных проверок.

Это не “просто deploy job”. Это высокий уровень доверия к тестам, rollback, observability и release process.

---

# Где GitOps

[[GitOps]] — часть CD.

GitOps меняет способ доставки:

```text
push-based CD:
  pipeline сам выполняет kubectl/helm на cluster

pull-based GitOps:
  controller внутри cluster читает Git и применяет desired state
```

CI при этом никуда не исчезает:

```text
CI build/test/scan/push image
GitOps controller deploy image/manifests from Git
```

---

# Ветки области

## CI

- [[Continuous Integration]]
- [[Build]]
- [[Test Automation]]
- [[Linting]]
- [[SAST]]
- [[Artifacts and Cache]]
- [[CI Build Cache]]
- [[Secrets in CI-CD]]

---

## CD

- [[Continuous Delivery]]
- [[Continuous Deployment]]
- [[Deployment Strategies]]
- [[Release Strategy]]
- [[Rollback]]
- [[Manual Approvals]]
- [[Pipeline Rules]]
- [[Preview Environments]]
- [[Rolling Update]]
- [[Deploy via SSH]]
- [[Deploy via Docker Compose]]
- [[Deploy to Kubernetes]]
- [[Deploy via Helm]]
- [[GitOps]]

---

## Tools

- [[GitLab CI]]
- [[GitHub Actions]]
- [[Jenkins]]
- [[TeamCity]]
- [[GitLab Runner]]
- [[Runner Executors]]
- [[GitLab Container Registry]]
- [[GHCR]]
- [[Harbor]]
- [[Docker in Docker]]
- [[Kaniko]]
- [[Buildah]]
- [[OIDC in CI-CD]]

---

# Что важно в production

Хороший CI/CD pipeline:

```text
не деплоит непроверенный код
не использует latest для production
хранит artifact/image отдельно от cache
не светит secrets в logs
умеет rollback
имеет approvals там, где нужен контроль
пишет понятный audit trail
проверяет результат deploy
```

---

# Частые ошибки

## Cache принят за artifact

Cache можно потерять без нарушения pipeline.

Artifact должен быть явно опубликован и версионирован.

---

## Deploy из branch без правил

Pipeline должен явно отделять:

```text
feature branch
merge request
main
tag
production release
```

---

## GitOps смешали с CI

Если CI сам делает `kubectl apply`, а Flux/Argo CD потом возвращает состояние из Git, получаются гонки и drift.

Нужно выбрать ownership:

```text
pipeline owns deploy
или GitOps controller owns deploy
```

---

# Связанные заметки

- [[DevOps]]
- [[Containers]]
- [[Container Registry]]
- [[Kubernetes]]
- [[Observability]]
- [[Supply Chain Security]]
