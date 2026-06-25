# GHCR

`GHCR` — GitHub Container Registry.

Images обычно имеют вид:

```text
ghcr.io/owner/image:tag
```

GHCR часто используют с [[GitHub Actions]].

---

# Login

Локально:

```bash
echo "$TOKEN" | docker login ghcr.io -u USERNAME --password-stdin
```

В GitHub Actions обычно хватает `GITHUB_TOKEN`, если заданы permissions:

```yaml
permissions:
  contents: read
  packages: write
```

---

# Push

```bash
docker build -t ghcr.io/org/app:$GIT_SHA .
docker push ghcr.io/org/app:$GIT_SHA
```

---

# Visibility

Package может быть private или public.

Для pull private image нужны права у token/user.

---

# Частые проблемы

## denied

Нет `packages: write` или token не имеет прав на package.

## Kubernetes не может pull

Нужен imagePullSecret с credentials, если image private.

## Package привязан не к тому repo/org

Проверить owner и package settings.

---

# Связанные заметки

- [[GitHub Actions]]
- [[Container Registry]]
- [[Docker Image]]
- [[ImagePullSecrets]]
