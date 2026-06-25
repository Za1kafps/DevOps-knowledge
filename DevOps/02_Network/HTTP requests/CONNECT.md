# CONNECT

`CONNECT` — HTTP-метод для создания TCP-туннеля через HTTP proxy.

Чаще всего используется для HTTPS через corporate proxy.

Пример идеи:

```text
client -> proxy: CONNECT example.com:443
proxy -> example.com:443
client <-> encrypted TLS through proxy
```

Proxy видит, к какому host:port открывают tunnel, но не видит содержимое TLS без MITM.

---

# Где встречается

```text
corporate proxy
CI runners behind proxy
package managers
docker build behind proxy
browser HTTPS proxy
```

Переменные окружения:

```text
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

---

# Проверка proxy

```bash
curl -v -x http://proxy.example.com:3128 https://example.com
```

Если нужен логин:

```bash
curl -v -x http://user:pass@proxy.example.com:3128 https://example.com
```

---

# Частые проблемы

## Proxy запрещает CONNECT к порту

Многие proxy разрешают CONNECT только к 443.

## NO_PROXY не настроен

Внутренние адреса случайно идут через внешний proxy.

Пример:

```bash
export NO_PROXY="localhost,127.0.0.1,.svc,.cluster.local,10.0.0.0/8"
```

## TLS interception

Corporate proxy подменяет сертификат, и клиент должен доверять корпоративному CA.

---

# Связанные заметки

- [[HTTP requests]]
- [[HTTPS and TLS]]
- [[curl]]
- [[CI-CD]]
