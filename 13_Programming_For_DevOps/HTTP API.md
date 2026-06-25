# HTTP API

HTTP API связывает automation с GitLab, Kubernetes, Vault, cloud providers и внутренними сервисами. Для надёжного клиента недостаточно отправить запрос: нужно учитывать semantics метода, timeout, pagination, rate limits и повторяемость операции.

## Запрос

```http
POST /v1/deployments HTTP/1.1
Host: deploy.example.com
Authorization: Bearer <token>
Content-Type: application/json
Idempotency-Key: 2ef5...

{"image":"registry.example.com/api:1.4.2"}
```

В ответе важны status code, headers, body и request ID.

## Методы

- `GET` читает ресурс и должен быть safe;
- `PUT` заменяет ресурс и обычно идемпотентен;
- `PATCH` изменяет часть ресурса, semantics зависит от patch format;
- `POST` создаёт действие/ресурс и без idempotency key может дублироваться;
- `DELETE` удаляет ресурс, но повтор может вернуть `404`.

Идемпотентность описывает эффект повторного запроса, а не одинаковый response code.

## Status codes

- `200`/`201`/`204` — успех разных видов;
- `400` — malformed/invalid request;
- `401` — нет или неверна authentication;
- `403` — identity известна, но operation запрещена;
- `404` — ресурс не найден или скрыт политикой;
- `409` — conflict текущего состояния/version;
- `422` — структура распознана, validation не прошла;
- `429` — rate limit, учитывай `Retry-After`;
- `500`/`502`/`503`/`504` — server/upstream failure.

## Timeout

Разделяй:

- DNS/connect timeout;
- TLS handshake;
- time to first byte;
- read timeout;
- общий deadline операции.

Timeout должен прерывать запрос, а не только переставать ждать в вызывающем коде.

## Retry

Обычно повторяют временные ошибки `429`, `502`, `503`, `504` и transport failures. Нужны:

- ограничение attempts/total time;
- exponential backoff;
- jitter;
- соблюдение `Retry-After`;
- проверка идемпотентности.

Повтор `POST create` без ключа идемпотентности способен создать несколько ресурсов.

## Pagination

API может вернуть только страницу:

```json
{
  "items": [],
  "next_cursor": "eyJpZCI6..."
}
```

Клиент должен обходить страницы до отсутствия cursor, но иметь общий limit/deadline. Offset pagination может пропускать или дублировать объекты при конкурентных изменениях.

## Optimistic concurrency

`ETag`/`If-Match`, resource version или revision предотвращают lost update:

```http
PATCH /v1/config
If-Match: "revision-42"
```

При `409`/`412` клиент перечитывает состояние и решает конфликт, а не бесконечно повторяет старый patch.

## Диагностика через curl

```bash
curl --fail-with-body --silent --show-error \
  --connect-timeout 3 \
  --max-time 15 \
  --retry 3 \
  --retry-all-errors \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json" \
  https://api.example.com/v1/items
```

Осторожно: `--retry-all-errors` подходит только когда повтор операции безопасен.

## Безопасность

- проверяй TLS certificate;
- ограничивай token scopes;
- не логируй Authorization header;
- валидируй response schema;
- не следуй redirect с credentials на чужой host;
- ограничивай размер body;
- защищай webhook подписью и replay window.

## Связи

- [[Programming for DevOps]]
- [[curl]]
- [[HTTP requests]]
- [[Response HTTP States]]
- [[Retries and Timeouts]]
- [[JSON]]
- [[TLS]]
