# Runner Executors

`Runner Executor` — способ, которым CI runner запускает job.

Executor определяет изоляцию, доступ к Docker, скорость и риски безопасности.

---

# Shell executor

Job запускается прямо на host.

Плюсы:

```text
просто
быстро
есть доступ к host tools
```

Минусы:

```text
слабая изоляция
грязное состояние между jobs
опасно для untrusted code
```

---

# Docker executor

Job запускается в container.

Плюсы:

```text
лучше изоляция
повторяемые images
легче чистить окружение
```

Минусы:

```text
сложности с docker build
volume/cache permissions
```

---

# Kubernetes executor

Каждая job запускается как pod.

Плюсы:

```text
scaling
изоляция на namespace/pod уровне
нативно для Kubernetes
```

Минусы:

```text
сложнее debug
нужны RBAC/resources/quotas
network policies
```

---

# Что выбрать

```text
trusted simple server -> shell
обычный CI -> docker
масштабируемый CI в cluster -> kubernetes
```

Для untrusted pull requests shell executor лучше не использовать.

---

# Связанные заметки

- [[GitLab Runner]]
- [[GitLab CI]]
- [[Docker in Docker]]
- [[Kaniko]]
- [[Buildah]]
