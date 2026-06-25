# Distroless Images

`Distroless images` — container images без shell, package manager и обычного набора Linux userland.

В них оставляют только то, что нужно приложению для запуска.

Идея:

```text
меньше файлов
меньше attack surface
меньше CVE от лишних packages
сложнее жить злоумышленнику внутри контейнера
```

Связано с [[Image Security]], [[Dockerfile]], [[Multi-stage Build]].

---

# Когда использовать

Хорошо подходят для:

```text
Go static binaries
Java apps с нужным runtime
Node/Python если есть подходящий base
production runtime images
```

Плохо подходят, если приложению нужен shell, package manager или runtime debug прямо внутри контейнера.

---

# Пример Go

```dockerfile
FROM golang:1.22 AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /out/app ./cmd/app

FROM gcr.io/distroless/static-debian12
COPY --from=build /out/app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

---

# Debug

В distroless обычно нет:

```text
sh
bash
curl
ps
apt
apk
```

Поэтому это не сработает:

```bash
docker exec -it app sh
```

Для debug используют:

```text
логи приложения
metrics/traces
debug variant image
ephemeral debug container в Kubernetes
tcpdump на node/sidecar
```

---

# Риски

## Труднее расследовать руками

Нельзя просто зайти и поставить `curl`.

Это нормально для production, но команда должна иметь другие инструменты observability.

---

## Не хватает CA certificates

Приложение может не доверять HTTPS endpoints, если runtime image не содержит CA bundle.

Проверять ошибку:

```text
x509: certificate signed by unknown authority
```

---

## Dynamic binary не запускается

Если бинарник зависит от shared libraries, static distroless может не подойти.

Проверить в build stage:

```bash
ldd /out/app
```

---

# Связанные заметки

- [[Image Security]]
- [[Dockerfile]]
- [[Multi-stage Build]]
- [[Container Security]]
