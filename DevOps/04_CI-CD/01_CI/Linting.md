# Linting

`Linting` — статическая проверка кода, конфигов и инфраструктурных файлов до запуска приложения.

Lint обычно быстрый, поэтому его ставят в начало CI.

---

# Что проверяют

```text
код
Dockerfile
YAML
Helm charts
Terraform
Ansible
Kubernetes manifests
shell scripts
```

Примеры:

```bash
shellcheck script.sh
yamllint .
hadolint Dockerfile
helm lint chart/
terraform fmt -check
terraform validate
```

---

# Почему lint важен

Lint ловит ошибки, которые дешевле исправить до build/deploy:

```text
битый YAML
опасный Dockerfile
неформатированный Terraform
shell quoting bug
невалидный Helm chart
```

---

# Lint не заменяет tests

Lint проверяет форму и часть статических правил.

Он не доказывает, что приложение работает.

Цепочка должна быть:

```text
lint -> tests -> build -> scan -> publish
```

---

# Частые ошибки

## Lint только advisory

Если lint падает, job должен падать.

## Разные версии локально и в CI

Фиксируй версии tools через image, lockfile или pre-commit config.

## Слишком шумные правила

Если команда массово игнорирует lint, правила надо настроить, а не терпеть шум.

---

# Связанные заметки

- [[Continuous Integration]]
- [[YAML]]
- [[Dockerfile]]
- [[Helm]]
- [[Terraform]]
