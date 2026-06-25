# Docker Network

`Docker Network` — сеть, через которую контейнеры общаются друг с другом, host и внешним миром.

Docker networking связан с [[Network]], [[NAT]], [[Firewall]], [[DNS]] и [[Docker Compose]].

---

# Основные типы network

## bridge

Default для одиночного Docker host.

Контейнер получает private IP, а наружу выходит через NAT.

Проверить:

```bash
docker network ls
docker network inspect bridge
```

---

## host

Контейнер использует network namespace host.

```bash
docker run --network host nginx
```

Плюс: меньше сетевой магии.

Минус: хуже изоляция, порты конфликтуют напрямую с host.

---

## none

Без сети.

```bash
docker run --network none alpine
```

---

## user-defined bridge

Лучше, чем default bridge, потому что даёт встроенный DNS по container/service name.

```bash
docker network create appnet
docker run -d --name db --network appnet postgres:16
docker run -it --rm --network appnet alpine
```

Из второго контейнера `db` резолвится по имени.

---

# Port publishing

```bash
docker run -p 8080:80 nginx
```

Смысл:

```text
host:8080 -> container:80
```

Если приложение внутри контейнера слушает только `127.0.0.1`, port publishing не поможет. Нужно слушать `0.0.0.0` внутри контейнера.

---

# DNS внутри Docker

В user-defined network контейнеры резолвят имена друг друга.

Проверить:

```bash
docker exec app getent hosts db
```

В Compose service name становится DNS name:

```text
postgres://user:pass@db:5432/app
```

---

# Проверка

Список сетей:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect appnet
```

IP контейнера:

```bash
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container
```

Порты:

```bash
docker port container
docker ps
```

---

# NAT и iptables

Docker обычно создаёт NAT rules на host.

Проверить:

```bash
sudo iptables -t nat -S
sudo nft list ruleset
```

Если на host жёсткий firewall, Docker rules могут конфликтовать с policy.

---

# Частые проблемы

## Контейнер не доступен снаружи

Проверить:

```bash
docker ps
docker port container
ss -lntp
```

---

## Контейнеры не видят друг друга по имени

Они могут быть в разных networks или в default bridge без нормального DNS.

Используй user-defined network.

---

## localhost внутри контейнера

`localhost` внутри контейнера — сам контейнер, а не host.

Для доступа к host на Docker Desktop есть:

```text
host.docker.internal
```

На Linux это зависит от настройки.

---

# Связанные заметки

- [[Docker]]
- [[Docker Compose]]
- [[Network]]
- [[NAT]]
- [[Firewall]]
- [[DNS]]
