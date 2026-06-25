# Docker

`Docker` — платформа для сборки, доставки и запуска контейнеров.

В DevOps Docker обычно используют для:

```text
локального запуска сервисов
сборки container images
CI build/test окружений
публикации image в registry
простых deploy через Docker Compose
```

Docker относится к [[Containers]] и связан с [[Dockerfile]], [[Docker Image]], [[Container Registry]], [[Docker Compose]].

---

# Из чего состоит Docker

Основные части:

```text
docker CLI
dockerd
containerd
runc
images
containers
networks
volumes
registry
```

Упрощённая цепочка:

```text
docker run nginx
  -> CLI отправляет запрос dockerd
  -> dockerd скачивает image
  -> containerd управляет container lifecycle
  -> runc создаёт Linux container
```

---

# Image и container

`Image` — шаблон, из которого создают контейнер.

`Container` — запущенный или остановленный экземпляр image.

Пример:

```bash
docker pull nginx:1.27
docker run -d --name web -p 8080:80 nginx:1.27
```

Один image можно запустить много раз:

```bash
docker run -d --name web1 nginx:1.27
docker run -d --name web2 nginx:1.27
```

---

# Основные команды

Контейнеры:

```bash
docker ps
docker ps -a
docker stop web
docker start web
docker rm web
```

Images:

```bash
docker images
docker pull alpine:3.20
docker rmi alpine:3.20
```

Логи:

```bash
docker logs web
docker logs -f --tail=100 web
```

Shell внутри:

```bash
docker exec -it web sh
```

Inspect:

```bash
docker inspect web
docker inspect nginx:1.27
```

---

# Запуск контейнера

```bash
docker run -d \
  --name app \
  -p 8080:8080 \
  -e APP_ENV=prod \
  --restart unless-stopped \
  myapp:1.0.0
```

Смысл:

```text
-d                     background
--name                 имя контейнера
-p 8080:8080           host port -> container port
-e                     env variable
--restart              политика рестарта
myapp:1.0.0            image
```

---

# Где Docker хранит данные

Обычно:

```text
/var/lib/docker
```

Там лежат layers, containers, volumes, network metadata.

Проверить размер:

```bash
docker system df
du -sh /var/lib/docker
```

---

# Частые проблемы

## Cannot connect to the Docker daemon

Docker daemon не запущен или нет прав.

Проверить:

```bash
systemctl status docker
id
```

---

## Port is already allocated

Host port уже занят.

Проверить:

```bash
ss -lntp | grep ':8080'
docker ps
```

---

## No space left on device

Часто забились images, build cache, volumes или logs.

Проверить:

```bash
docker system df
docker builder du
df -h
```

Чистить осторожно:

```bash
docker system prune
docker builder prune
```

---

# Связанные заметки

- [[Containers]]
- [[Dockerfile]]
- [[Docker Image]]
- [[Docker Network]]
- [[Docker Volume]]
- [[Docker Compose]]
- [[Container Security]]
