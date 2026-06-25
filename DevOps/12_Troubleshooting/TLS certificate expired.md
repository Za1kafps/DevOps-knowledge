# TLS certificate expired

TLS certificate expired — сертификат истёк, и клиенты перестали доверять HTTPS endpoint.

---

# Проверка

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -dates -subject -issuer
```

Через curl:

```bash
curl -v https://example.com
```

---

# Где чинить

```text
load balancer certificate
Nginx certificate
Ingress TLS secret
cert-manager Certificate
Cloudflare edge/origin cert
```

---

# Kubernetes

```bash
kubectl get certificate -A
kubectl describe certificate <name> -n <ns>
kubectl get secret <tls-secret> -n <ns>
```

---

# Связанные заметки

- [[TLS Certificates]]
- [[cert-manager]]
- [[HTTPS and TLS]]
- [[Cloudflare]]
