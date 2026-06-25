# CI Build Cache

`CI Build Cache` ускоряет повторные сборки.

Cache не должен быть источником истины. Он нужен только для скорости.

---

# Что кэшируют

```text
package manager cache
compiled object cache
Docker/BuildKit cache
test framework cache
tool downloads
```

Примеры:

```text
~/.npm
~/.cache/pip
~/.cache/go-build
~/.m2/repository
BuildKit registry cache
```

---

# Cache key

Cache key должен меняться, когда меняются dependencies.

Пример идеи:

```text
cache key = OS + language version + lockfile hash
```

Если key слишком общий, можно получить старые зависимости.

Если key слишком уникальный, cache почти не используется.

---

# Docker BuildKit cache

Для ephemeral runners полезен registry cache:

```bash
docker buildx build \
  --cache-from type=registry,ref=registry.example.com/app:buildcache \
  --cache-to type=registry,ref=registry.example.com/app:buildcache,mode=max \
  -t registry.example.com/app:$GIT_SHA \
  --push .
```

Смотри [[BuildKit]].

---

# Частые ошибки

## Cache скрывает проблему

Pipeline проходит только потому, что в cache лежит старый dependency.

Периодически проверяй clean build.

## Cache содержит secrets

Нельзя кэшировать директории, куда package manager пишет tokens.

## Cache используется как artifact

Deploy не должен брать результат из cache.

---

# Связанные заметки

- [[Artifacts and Cache]]
- [[Build]]
- [[BuildKit]]
- [[Continuous Integration]]
