# ImagePullBackOff

`ImagePullBackOff` — Kubernetes не может скачать container image.

Это не ошибка приложения. Container ещё не запущен.

---

# Быстрая проверка

```bash
kubectl describe pod pod-name -n app
kubectl get events -n app --sort-by=.lastTimestamp
```

Смотри events:

```text
Failed to pull image
pull access denied
manifest unknown
no matching manifest
x509 certificate
i/o timeout
```

---

# Частые причины

## Неверный image tag

```bash
docker pull registry.example.com/app:tag
```

Если tag не существует, registry вернёт `manifest unknown`.

---

## Нет imagePullSecret

Для private registry:

```bash
kubectl get secret -n app
kubectl describe sa default -n app
```

Secret можно привязать к Pod или ServiceAccount.

---

## Registry недоступен с node

Проверять с node:

```bash
curl -v https://registry.example.com/v2/
```

Причины:

```text
DNS
firewall
proxy
TLS trust
registry outage
```

---

## Architecture mismatch

Например node `arm64`, image только `amd64`.

Ошибка:

```text
no matching manifest for linux/arm64
```

---

# Связанные заметки

- [[Docker Image]]
- [[Container Registry]]
- [[ImagePullSecrets]]
- [[Kubernetes Events]]
- [[GitLab Container Registry]]
- [[GHCR]]
