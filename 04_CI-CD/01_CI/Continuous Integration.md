# Continuous Integration

`Continuous Integration` — практика частой автоматической проверки изменений.

CI начинается с commit/merge request и заканчивается понятным результатом:

```text
passed / failed
artifact
test report
image tag/digest
scan report
```

CI не должен молча деплоить непроверенный код. Его задача — доказать, что изменение можно передавать в delivery.

---

# Что входит в CI

Обычная цепочка:

```text
checkout
restore cache
install dependencies
lint
unit tests
integration tests
build
SAST / dependency scan
container build
container scan
publish artifact/image
```

Не каждый проект делает всё, но production pipeline должен осознанно выбирать проверки, а не случайно пропускать их.

---

# Artifact

Artifact — результат build, которому можно доверять.

Примеры:

```text
binary
jar
npm package
docker image
helm chart
test report
coverage report
SBOM
```

Artifact должен быть воспроизводимым и привязанным к commit.

---

# Cache

Cache ускоряет pipeline, но не является результатом.

Примеры:

```text
npm cache
go build cache
maven cache
docker build cache
```

Если cache пропал, pipeline должен стать медленнее, но не сломаться логически.

Смотри [[Artifacts and Cache]] и [[CI Build Cache]].

---

# Пример Docker CI

```bash
docker build -t registry.example.com/app:$GIT_SHA .
trivy image registry.example.com/app:$GIT_SHA
docker push registry.example.com/app:$GIT_SHA
```

Для production полезно сохранять digest:

```bash
docker inspect --format='{{index .RepoDigests 0}}' registry.example.com/app:$GIT_SHA
```

---

# Что проверять в CI

## Быстрые проверки

```text
format
lint
unit tests
type checks
```

Они должны падать быстро и давать понятную ошибку.

---

## Более дорогие проверки

```text
integration tests
e2e tests
container scan
dependency scan
license scan
```

Их можно запускать на merge request, main или nightly, в зависимости от цены и риска.

---

# Частые проблемы

## Pipeline зелёный, artifact плохой

Причины:

```text
tests проверяют не тот build
image собран после tests с другими deps
artifact не опубликован
tag перезаписан
```

---

## Flaky tests

Flaky test нельзя просто игнорировать.

Нужно понять причину:

```text
race condition
real time dependency
shared external service
test order dependency
недостаточная изоляция
```

---

## Secrets в logs

Проверить:

```text
set -x
echo env
docker build args
verbose package managers
```

---

# Связанные заметки

- [[CI-CD]]
- [[Build]]
- [[Test Automation]]
- [[Linting]]
- [[SAST]]
- [[Artifacts and Cache]]
- [[CI Build Cache]]
- [[Secrets in CI-CD]]
- [[Container Registry]]
