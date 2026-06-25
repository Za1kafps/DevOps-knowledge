# Artifacts and Cache

`Artifact` и `cache` в CI — разные вещи.

Их нельзя смешивать.

---

# Artifact

Artifact — результат pipeline, который нужен дальше.

Примеры:

```text
binary
docker image
test report
coverage report
SBOM
helm chart package
frontend dist
```

Artifact должен быть:

```text
привязан к commit
доступен после job
версионирован
срок хранения понятен
```

---

# Cache

Cache — временное ускорение pipeline.

Примеры:

```text
npm cache
pip cache
go build cache
maven repository cache
docker build cache
```

Cache можно потерять. Pipeline от этого должен стать медленнее, но не неправильным.

---

# Главное различие

```text
artifact = результат
cache = ускорение
```

Если deploy зависит от cache, pipeline спроектирован плохо.

---

# Пример ошибки

Job `build` положил binary только в cache.

Следующая job иногда находит его, иногда нет.

Правильно:

```text
binary сохранить как artifact
dependencies сохранить как cache
```

---

# Docker images

Docker image обычно не хранят как CI artifact.

Его публикуют в [[Container Registry]]:

```bash
docker build -t registry.example.com/app:$GIT_SHA .
docker push registry.example.com/app:$GIT_SHA
```

А в deploy передают tag/digest.

---

# Связанные заметки

- [[Continuous Integration]]
- [[Build]]
- [[CI Build Cache]]
- [[Container Registry]]
- [[Docker Image]]
