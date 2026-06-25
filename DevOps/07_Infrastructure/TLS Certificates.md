# TLS Certificates

`TLS Certificate` связывает domain name с public key.

Для HTTPS клиент проверяет certificate chain, срок действия и совпадение имени.

---

# Что проверять

```bash
openssl s_client -connect example.com:443 -servername example.com
```

Даты:

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -dates
```

SAN:

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -ext subjectAltName
```

---

# Частые проблемы

```text
certificate expired
wrong SAN
incomplete chain
wrong SNI/default certificate
private key mismatch
ACME renewal failed
```

---

# Renewal

Certificate renewal должен мониториться.

Для Kubernetes смотри [[cert-manager]].

Для VM часто используют ACME clients вроде certbot/acme.sh.

---

# Связанные заметки

- [[HTTPS and TLS]]
- [[TLS]]
- [[cert-manager]]
- [[TLS certificate expired]]
