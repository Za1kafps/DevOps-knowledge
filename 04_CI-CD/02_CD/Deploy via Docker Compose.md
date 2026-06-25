# Deploy via Docker Compose

`Deploy via Docker Compose` — деплой нескольких контейнеров на один сервер через compose file.

Обычно используется с [[Deploy via SSH]].

---

# Типовая цепочка

```text
CI build image
CI push image to registry
SSH to server
docker compose pull
docker compose up -d
healthcheck
```

---

# Compose файл на сервере

Production compose обычно хранит:

```text
image tags
ports
volumes
networks
restart policy
env_file или secrets reference
healthchecks
```

Не надо собирать image на production сервере, если CI уже собрал artifact.

---

# Команды

```bash
docker compose pull
docker compose up -d
docker compose ps
docker compose logs -f --tail=100
```

Rollback на предыдущий tag:

```bash
APP_IMAGE=registry.example.com/app:previous docker compose up -d
```

Конкретная реализация зависит от того, как передаются env/image tags.

---

# Частые проблемы

## latest в compose

Неясно, какая версия запущена.

## down вместо up -d

`docker compose down` может удалить network и остановить всё. С `-v` удалит volumes.

## Нет healthcheck

Pipeline завершился, но приложение не готово.

---

# Связанные заметки

- [[Docker Compose]]
- [[Deploy via SSH]]
- [[Docker Volume]]
- [[Rollback]]
