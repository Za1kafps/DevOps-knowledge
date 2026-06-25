# Secrets in CI-CD

Secrets в CI/CD — токены, ключи и пароли, которые pipeline использует для доступа к registry, cloud, servers, Kubernetes и external APIs.

Главная задача: дать pipeline минимально нужный доступ и не раскрыть secret в logs/artifacts/images.

---

# Где secrets протекают

```text
echo $TOKEN
set -x
docker build --build-arg TOKEN
artifact with .env
test report with headers
cache with credentials
container image layers
```

---

# Хорошая практика

```text
masked/protected variables
separate secrets per environment
short-lived credentials
OIDC вместо long-lived cloud keys
least privilege
rotation
secret scanning
```

Смотри [[OIDC in CI-CD]].

---

# Docker build secrets

Плохо:

```bash
docker build --build-arg TOKEN=$TOKEN .
```

Лучше через BuildKit:

```bash
docker build \
  --secret id=npmrc,src=$HOME/.npmrc \
  -t app:$GIT_SHA .
```

Dockerfile:

```dockerfile
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

---

# Protected variables

Production secrets должны быть доступны только protected branches/tags.

Иначе feature branch может получить production deploy token.

---

# Частые ошибки

## Один token на всё

Registry push, prod deploy и cloud admin через один secret — плохая идея.

## Secrets в image

Проверять:

```bash
docker history --no-trunc image
```

## Secrets в logs

Отключай verbose вывод вокруг команд с credentials.

---

# Связанные заметки

- [[CI-CD]]
- [[OIDC in CI-CD]]
- [[BuildKit]]
- [[Secrets Management]]
- [[Supply Chain Security]]
