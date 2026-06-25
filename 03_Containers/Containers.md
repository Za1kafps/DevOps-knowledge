# Containers

[[Containers]] — область DevOps про упаковку и запуск приложения в изолированной среде.

Контейнер — это не маленькая виртуальная машина. Это обычный Linux-процесс, которому ядро ограничило видимость и ресурсы через namespaces, cgroups, capabilities и filesystem layers.

Упрощённо:

```text
image -> container process -> namespaces/cgroups -> host kernel
```

---

# Что контейнер даёт

Контейнер помогает:

```text
одинаково запускать приложение на laptop, CI и server
упаковать runtime dependencies
быстро создавать и удалять окружения
изолировать filesystem/process/network view
доставлять приложение через registry
```

Контейнер не заменяет security boundary уровня VM. Это изоляция процесса на общем ядре.

---

# Основные темы

- [[Docker]]
- [[Dockerfile]]
- [[Docker Image]]
- [[Multi-stage Build]]
- [[BuildKit]]
- [[Container Registry]]
- [[Docker Compose]]
- [[Docker Network]]
- [[Docker Volume]]
- [[Container Security]]
- [[Image Security]]
- [[Distroless Images]]

---

# Главная цепочка

```text
source code
  -> Dockerfile
  -> docker build / buildkit
  -> image
  -> registry
  -> docker run / compose / kubernetes
  -> container
  -> logs / metrics / healthcheck
```

В CI/CD обычно:

```text
CI собирает image
CI прогоняет tests/scans
CI push в registry
CD deploy-ит конкретный image tag/digest
```

---

# Важные команды

Показать контейнеры:

```bash
docker ps
docker ps -a
```

Логи:

```bash
docker logs -f container_name
```

Зайти внутрь:

```bash
docker exec -it container_name sh
```

Посмотреть подробности:

```bash
docker inspect container_name
```

Использование диска:

```bash
docker system df
```

---

# Что важно в production

Контейнер должен быть:

```text
воспроизводимо собран
минимален по размеру и attack surface
запущен не от root
без secrets внутри image layers
с понятным healthcheck
с ограничениями CPU/memory
с логами в stdout/stderr
```

---

# Частые поломки

## Контейнер сразу завершился

Проверить:

```bash
docker ps -a
docker logs container_name
docker inspect container_name --format '{{.State.ExitCode}}'
```

---

## Приложение не доступно снаружи

Проверить:

```bash
docker ps
docker port container_name
ss -lntp
```

Часто забыли `-p host_port:container_port` или приложение слушает `127.0.0.1` внутри контейнера.

---

## Данные пропали после пересоздания

Если данные были только внутри container writable layer, они удалились вместе с контейнером.

Для состояния нужны [[Docker Volume]] или внешняя БД.

---

# Связанные заметки

- [[DevOps]]
- [[CI-CD]]
- [[Kubernetes]]
- [[Docker]]
- [[Container Security]]
