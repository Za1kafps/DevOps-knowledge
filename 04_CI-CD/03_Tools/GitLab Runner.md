# GitLab Runner

`GitLab Runner` — агент, который выполняет jobs из [[GitLab CI]].

GitLab создаёт job, runner забирает её и запускает в выбранном executor.

---

# Executors

Частые executors:

```text
shell
docker
kubernetes
ssh
docker+machine
```

Смотри [[Runner Executors]].

---

# Команды

Статус:

```bash
gitlab-runner status
```

Проверить регистрацию:

```bash
gitlab-runner verify
```

Список runners:

```bash
gitlab-runner list
```

Логи systemd:

```bash
journalctl -u gitlab-runner -f
```

---

# Tags

Job может требовать runner tags:

```yaml
build:
  tags:
    - docker
```

Если runner с таким tag недоступен, job будет pending.

---

# Protected runners

Protected runner выполняет jobs только для protected branches/tags.

Это важно для production deploy и secrets.

---

# Частые проблемы

## Job stuck pending

Причины:

```text
нет runner
tag mismatch
runner paused
runner protected, branch not protected
нет concurrency
```

## Docker executor не может build image

Нужен Docker socket, DinD или rootless builder: [[Docker in Docker]], [[Kaniko]], [[Buildah]].

## Runner хранит грязное состояние

Shell executor особенно легко загрязняется между job.

---

# Связанные заметки

- [[GitLab CI]]
- [[Runner Executors]]
- [[Docker in Docker]]
- [[Kaniko]]
- [[Buildah]]
