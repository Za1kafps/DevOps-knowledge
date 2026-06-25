# TLS

`TLS` — протокол шифрования транспортного соединения.

Чаще всего его видят в HTTPS, но TLS используется не только там:

```text
HTTPS
PostgreSQL TLS
Redis TLS
Kafka TLS
SMTP STARTTLS
service mesh mTLS
```

В [[HTTPS and TLS]] разобран именно HTTP поверх TLS.

---

# Что даёт TLS

TLS решает три задачи:

```text
confidentiality  трафик нельзя прочитать
integrity        трафик нельзя незаметно изменить
authentication   клиент проверяет, что сервер настоящий
```

При mTLS сервер тоже проверяет клиентский сертификат.

---

# TLS handshake

Упрощённо:

```text
client hello
server hello
certificate
key exchange
finished
encrypted application data
```

В handshake согласуются TLS version, cipher suite и ключи для шифрования.

---

# Сертификат

Сертификат связывает публичный ключ с именем.

Для HTTPS имя должно быть в `Subject Alternative Name`.

Проверить сертификат:

```bash
openssl x509 -in cert.pem -noout -text
```

Проверить удалённый сервер:

```bash
openssl s_client -connect example.com:443 -servername example.com
```

---

# CA и chain

Клиент доверяет не любому сертификату, а цепочке:

```text
server certificate
intermediate CA
root CA
```

Root CA уже есть в trust store клиента.

Если сервер не отдаёт intermediate, часть клиентов не сможет построить chain.

---

# mTLS

`mTLS` — mutual TLS.

Обычный TLS:

```text
client проверяет server
```

mTLS:

```text
client проверяет server
server проверяет client certificate
```

Используется в service mesh, internal APIs, Kubernetes webhooks, banking/integration systems.

---

# Частые TLS-проблемы

## Expired certificate

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -dates
```

---

## Unknown authority

Клиент не доверяет CA.

Часто бывает с self-signed, private CA или неполной chain.

---

## Protocol version

Старый клиент не поддерживает новый TLS или сервер отключил старые версии.

Проверка:

```bash
openssl s_client -tls1_2 -connect example.com:443 -servername example.com
openssl s_client -tls1_3 -connect example.com:443 -servername example.com
```

---

## Wrong SNI

Без правильного hostname сервер может отдать неправильный сертификат.

Проверка:

```bash
openssl s_client -connect 1.2.3.4:443 -servername example.com
```

---

# Связанные заметки

- [[HTTPS and TLS]]
- [[HTTP]]
- [[TLS Certificates]]
- [[cert-manager]]
- [[Secrets]]
- [[Database TLS]]
