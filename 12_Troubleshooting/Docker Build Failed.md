# Docker Build Failed

Docker build failed — image не собрался из Dockerfile/build context.

---

# Проверка

```bash
docker build --progress=plain -t app:debug .
docker build --no-cache -t app:debug .
```

Проверить context:

```bash
ls -la
cat .dockerignore
```

---

# Частые причины

```text
COPY path не существует
.dockerignore исключил файл
package registry недоступен
secret передан неправильно
base image не скачивается
команда RUN падает
architecture mismatch
```

---

# Связанные заметки

- [[Dockerfile]]
- [[BuildKit]]
- [[Container Registry]]
