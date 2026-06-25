# Docker in Docker

`Docker in Docker` (`DinD`) — запуск Docker daemon внутри CI job/container.

Его часто используют, чтобы собирать Docker images в CI.

---

# Как выглядит

В GitLab CI:

```yaml
image: docker:27
services:
  - docker:27-dind

variables:
  DOCKER_HOST: tcp://docker:2375

build:
  script:
    - docker build -t app:$CI_COMMIT_SHA .
```

---

# Риски

DinD часто требует privileged mode.

Это повышает риск:

```text
escape на runner host
доступ к kernel features
грязное состояние daemon
сложности с cache
```

Для shared runners privileged DinD надо использовать очень осторожно.

---

# Альтернативы

```text
Docker socket binding
BuildKit rootless
Kaniko
Buildah
cloud build service
```

Смотри [[Kaniko]], [[Buildah]], [[BuildKit]].

---

# Частые проблемы

## Cannot connect to Docker daemon

Неверный `DOCKER_HOST` или service не поднялся.

## TLS mismatch

Docker client ждёт TLS, daemon слушает без TLS или наоборот.

## No cache

Ephemeral daemon теряет layer cache между jobs.

---

# Связанные заметки

- [[GitLab CI]]
- [[GitLab Runner]]
- [[BuildKit]]
- [[Kaniko]]
- [[Container Security]]
