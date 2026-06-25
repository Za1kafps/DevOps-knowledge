# Buildah

`Buildah` — инструмент для сборки OCI/container images без Docker daemon.

Buildah часто используют вместе с Podman/Skopeo и rootless container workflows.

---

# Что умеет

```text
build from Dockerfile/Containerfile
build images scriptable steps
rootless builds
push/pull images
работа с OCI images
```

---

# Команды

Собрать:

```bash
buildah bud -t registry.example.com/app:$GIT_SHA .
```

Push:

```bash
buildah push registry.example.com/app:$GIT_SHA
```

Login:

```bash
buildah login registry.example.com
```

---

# Где полезен

```text
rootless CI
OpenShift/Kubernetes environments
security-sensitive runners
альтернатива Docker daemon
```

---

# Частые проблемы

## Storage driver

Rootless builds зависят от fuse-overlayfs/overlay support.

## Registry auth

Нужно правильно передать auth config.

## Отличия от Docker

Некоторые Docker-specific ожидания могут отличаться.

---

# Связанные заметки

- [[Docker in Docker]]
- [[Kaniko]]
- [[BuildKit]]
- [[Dockerfile]]
- [[Container Registry]]
