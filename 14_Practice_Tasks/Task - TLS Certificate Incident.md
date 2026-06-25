# Task - TLS Certificate Incident

## Симптом

Client сообщает expired certificate, hostname mismatch, unknown CA или incomplete chain.

## Проверка endpoint

```bash
openssl s_client \
  -connect app.example.com:443 \
  -servername app.example.com \
  -showcerts </dev/null
```

Краткие даты и issuer:

```bash
openssl s_client \
  -connect app.example.com:443 \
  -servername app.example.com </dev/null 2>/dev/null |
openssl x509 -noout -subject -issuer -serial -dates -ext subjectAltName
```

HTTP:

```bash
curl -vI https://app.example.com
```

## Проверить

- `notBefore`/`notAfter`;
- SAN содержит hostname;
- client видит полный intermediate chain;
- SNI выбирает правильный certificate;
- system time корректно;
- certificate и private key совпадают;
- LB/Ingress действительно загрузил новый secret.

Сравнить public keys:

```bash
openssl x509 -in tls.crt -pubkey -noout | sha256sum
openssl pkey -in tls.key -pubout | sha256sum
```

## Kubernetes/cert-manager

```bash
kubectl get certificate,certificaterequest,order,challenge -A
kubectl describe certificate app-tls -n app
kubectl get secret app-tls -n app -o yaml
kubectl logs -n cert-manager deploy/cert-manager
```

## Сценарии

- Secret обновлён, controller не reload-нулся;
- DNS challenge смотрит не в ту zone;
- HTTP-01 path не достигает solver;
- rate limit ACME;
- chain неполная;
- clock skew;
- certificate выдан для другого hostname.

## Связи

- [[TLS Certificates]]
- [[cert-manager]]
- [[HTTPS and TLS]]
- [[TLS certificate expired]]
- [[Ingress]]
