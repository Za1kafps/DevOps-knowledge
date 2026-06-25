# Docker Volume

`Docker Volume` — способ хранить данные вне writable layer контейнера.

Контейнеры временные. Данные, которые должны пережить пересоздание контейнера, надо хранить в volume, bind mount или внешнем хранилище.

Связано с [[Docker]], [[Docker Compose]], [[Databases]], [[Backups]].

---

# Зачем нужны volumes

Без volume данные пишутся в container writable layer.

Если удалить контейнер:

```bash
docker rm container
```

эти данные пропадут.

Volume живёт отдельно от контейнера.

---

# Named volume

Создать:

```bash
docker volume create pgdata
```

Использовать:

```bash
docker run -d \
  --name postgres \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16
```

Посмотреть:

```bash
docker volume ls
docker volume inspect pgdata
```

---

# Bind mount

Bind mount монтирует директорию host:

```bash
docker run --rm \
  -v "$PWD/config:/app/config" \
  app:dev
```

Плюсы:

```text
удобно для разработки
видно файлы на host
```

Минусы:

```text
зависит от host path
можно случайно перетереть файлы
права пользователей часто ломаются
```

---

# tmpfs

tmpfs хранит данные в памяти:

```bash
docker run --tmpfs /tmp app:dev
```

Подходит для временных файлов, которые не должны попадать на диск.

---

# Volumes в Compose

```yaml
services:
  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Удаление:

```bash
docker compose down
```

не удаляет named volume.

А вот:

```bash
docker compose down -v
```

удаляет.

---

# Backup volume

Простой пример backup:

```bash
docker run --rm \
  -v pgdata:/data \
  -v "$PWD:/backup" \
  alpine tar czf /backup/pgdata.tgz -C /data .
```

Для баз данных лучше использовать штатный backup инструмент, например [[pg_dump and pg_restore]], а не просто tar live data directory.

---

# Частые проблемы

## Permission denied

UID/GID внутри контейнера не совпадает с владельцем файлов на host/volume.

Проверить:

```bash
docker exec container id
ls -ln /path/on/host
```

---

## Данные не там

Проверить mount:

```bash
docker inspect container --format '{{json .Mounts}}'
```

---

## Удалили volume

`docker system prune --volumes` и `docker compose down -v` удаляют volumes.

Перед чисткой проверять:

```bash
docker volume ls
docker system df -v
```

---

# Связанные заметки

- [[Docker]]
- [[Docker Compose]]
- [[Database Backups]]
- [[Backup Strategy]]
