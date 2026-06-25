# GitLab CI

`GitLab CI` — CI/CD система GitLab, которая читает `.gitlab-ci.yml` и запускает pipeline через [[GitLab Runner]].

GitLab CI используют для:

```text
lint/test/build
container image build
push в GitLab Container Registry
deploy jobs
security scans
manual approvals
scheduled pipelines
```

---

# Основные сущности

```text
pipeline  весь запуск CI/CD
stage     группа jobs
job       конкретная задача
runner    агент, который выполняет job
artifact  результат job
cache     ускорение job
variable  переменная/secret
environment окружение deploy
```

---

# Пример pipeline

```yaml
stages:
  - test
  - build
  - deploy

test:
  stage: test
  image: golang:1.22
  script:
    - go test ./...

build-image:
  stage: build
  image: docker:27
  services:
    - docker:27-dind
  script:
    - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" "$CI_REGISTRY"
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA" .
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA"
```

---

# Rules

GitLab `rules` определяют, когда job запускается.

Пример:

```yaml
deploy-prod:
  stage: deploy
  script: ./deploy.sh
  rules:
    - if: '$CI_COMMIT_TAG'
      when: manual
```

Production deploy лучше привязывать к protected tags/branches и protected environments.

---

# Частые проблемы

## Runner offline

```bash
gitlab-runner status
gitlab-runner verify
```

## Tags mismatch

Job требует runner tag, которого нет у доступных runners.

## Protected variables недоступны

Protected variables доступны только protected branches/tags.

## Cache перепутали с artifacts

Deploy должен брать artifact/image из registry, а не из cache.

---

# Связанные заметки

- [[CI-CD]]
- [[GitLab Runner]]
- [[Runner Executors]]
- [[GitLab Container Registry]]
- [[Artifacts and Cache]]
- [[Pipeline Rules]]
