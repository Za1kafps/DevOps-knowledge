# Retries and Timeouts

Timeout ограничивает ожидание, retry повторяет временно неуспешную операцию. Без общего deadline retries способны превратить короткий сбой в долгую очередь и усилить нагрузку на уже больной сервис.

## Виды timeout

- connection timeout;
- TLS handshake timeout;
- request/read timeout;
- idle timeout;
- total operation deadline.

Значение выбирают по latency distribution и SLO, а не случайно. Timeout должен быть меньше budget вызывающей операции.

## Exponential backoff

```text
delay = min(cap, base * 2^attempt) + random_jitter
```

Jitter не даёт всем clients повторить запрос одновременно.

Пример последовательности:

```text
200ms, 400ms, 800ms, 1.6s, stop
```

## Что можно повторять

Обычно:

- DNS/connection reset;
- `429` с учётом `Retry-After`;
- `502`, `503`, `504`;
- optimistic lock conflict после reread.

Опасно:

- payment/create/deploy `POST` без idempotency key;
- операция частично выполнилась, а response потерян;
- authentication/authorization error;
- validation error.

## Retry budget

Ограничивай:

- максимальное число попыток;
- общее время;
- долю retry traffic;
- параллелизм;
- размер очереди.

Если каждый из нескольких service layers делает по три попытки, один request может породить десятки downstream calls.

## Python

```python
deadline = time.monotonic() + 15
for attempt in range(4):
    try:
        return call(timeout=min(3, deadline - time.monotonic()))
    except TemporaryError:
        if time.monotonic() >= deadline:
            raise
        time.sleep(random.uniform(0, min(2**attempt, 5)))
```

## Go

```go
ctx, cancel := context.WithTimeout(parent, 15*time.Second)
defer cancel()
```

Каждый retry использует оставшееся время `ctx`, а не новый бесконечный deadline.

## Связи

- [[Programming for DevOps]]
- [[HTTP API]]
- [[Rate Limiting]]
- [[SLO]]
- [[Incident Response Flow]]
