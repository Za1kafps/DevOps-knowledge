# cert-manager

`cert-manager` — Kubernetes controller для выпуска и обновления TLS certificates.

Он создаёт/обновляет Kubernetes Secrets с сертификатами по ресурсам Certificate и Issuer/ClusterIssuer.

---

# Основные сущности

```text
Issuer          issuer в namespace
ClusterIssuer   issuer на весь cluster
Certificate     desired certificate
CertificateRequest request на выпуск
Order/Challenge ACME flow
Secret          итоговый tls.crt/tls.key
```

---

# ACME HTTP-01

HTTP-01 проверяет домен через HTTP endpoint.

Нужно:

```text
домен указывает на ingress
ingress доступен извне
80 порт открыт
правильный ingressClass
```

---

# ACME DNS-01

DNS-01 создаёт TXT record.

Плюсы:

```text
можно wildcard
не нужен внешний HTTP доступ
подходит для private ingress
```

Минусы:

```text
нужны credentials к DNS provider
TTL/propagation delays
```

---

# Проверка

```bash
kubectl get certificate -A
kubectl describe certificate app-tls -n app
kubectl get certificaterequest -A
kubectl get order,challenge -A
```

Secret:

```bash
kubectl get secret app-tls -n app -o yaml
```

---

# Частые проблемы

## Certificate not ready

Смотреть events Certificate/Order/Challenge.

## DNS propagation

DNS-01 TXT запись ещё не видна authoritative/public resolvers.

## Wrong ingressClass

HTTP-01 challenge route создан не там.

---

# Связанные заметки

- [[TLS Certificates]]
- [[HTTPS and TLS]]
- [[Ingress]]
- [[DNS]]
- [[Kubernetes Security]]
