# Docker Compose

`Docker Compose` — инструмент для описания и запуска нескольких контейнеров через `compose.yaml`.

Его используют для:

```text
локальной разработки
тестовых окружений
маленьких single-host deploy
integration tests в CI
```

Compose не заменяет Kubernetes. Он удобен, когда один host и простая схема.

---

# Пример

```yaml
services:
  app:
    image: myapp:dev
    ports:
      - "8080:8080"
    environment:
      DATABASE_URL: postgres://app:password@db:5432/app
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: password
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Запуск:

```bash
docker compose up -d
```

---

# Основные команды

```bash
docker compose up -d
docker compose ps
docker compose logs -f
docker compose logs -f app
docker compose exec app sh
docker compose down
docker compose pull
docker compose up -d --build
```

Удалить вместе с volumes:

```bash
docker compose down -v
```

Осторожно: так можно удалить данные БД.

---

# Service DNS

Сервисы в одной compose network видят друг друга по имени service.

Пример:

```text
app -> db:5432
```

Не надо подключаться из `app` к `localhost:5432`, потому что `localhost` внутри контейнера — это сам контейнер `app`.

---

# Ports

```yaml
ports:
  - "8080:80"
```

Смысл:

```text
host port 8080 -> container port 80
```

Если `ports` не указан, сервис доступен другим контейнерам в compose network, но не опубликован на host port.

---

# Volumes

Named volume:

```yaml
volumes:
  - pgdata:/var/lib/postgresql/data
```

Bind mount:

```yaml
volumes:
  - ./src:/app/src
```

Named volume лучше для данных сервиса, bind mount удобен для разработки.

---

# depends_on

`depends_on` задаёт порядок запуска контейнеров, но не гарантирует готовность приложения.

Если app стартует раньше, чем Postgres готов принимать connections, нужен:

```text
healthcheck
retry logic в приложении
wait script только как временная мера
```

---

# Частые проблемы

## App не видит db

Проверить:

```bash
docker compose ps
docker compose exec app getent hosts db
docker compose logs db
```

---

## Port already allocated

Host port занят.

```bash
ss -lntp | grep ':8080'
```

---

## После down пропали данные

Скорее всего был `docker compose down -v` или данные лежали не в volume.

---

# Связанные заметки

- [[Docker]]
- [[Docker Network]]
- [[Docker Volume]]
- [[Deploy via Docker Compose]]
- [[PostgreSQL]]
