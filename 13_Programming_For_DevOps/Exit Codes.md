# Exit Codes

Exit code сообщает вызывающему процессу, завершилась ли команда успешно. В Unix shell код находится в диапазоне `0..255`.

```bash
command
rc=$?
printf 'exit=%d\n' "$rc"
```

## Основные значения

- `0` — success;
- `1` — общая ошибка приложения;
- `2` — неправильное использование CLI;
- `126` — command найден, но не может быть выполнен;
- `127` — command не найден;
- `128 + N` — процесс завершён signal `N`, например `143` для `SIGTERM`.

Значения выше — conventions, а не универсальный протокол всех программ. Всегда проверяй документацию конкретной команды.

## Shell

```bash
if ! output="$(command)"; then
  rc=$?
  echo "failed: $rc" >&2
fi
```

В таком виде `!` меняет status, поэтому для сохранения исходного кода надёжнее:

```bash
set +e
output="$(command)"
rc=$?
set -e

if (( rc != 0 )); then
  echo "command failed: $rc" >&2
  exit "$rc"
fi
```

У pipeline без `pipefail` возвращается status последней команды:

```bash
set -o pipefail
producer | consumer
```

## Приложение

CLI должен:

- возвращать `0` только после достижения заявленного результата;
- писать machine-readable result в stdout;
- писать причину ошибки в stderr;
- не использовать разные коды без документированной пользы;
- отличать invalid input от временной external failure, если caller это использует.

## systemd и Kubernetes

systemd показывает code/status:

```bash
systemctl status app
journalctl -u app
```

В Kubernetes:

```bash
kubectl get pod app -o jsonpath='{.status.containerStatuses[0].lastState.terminated.exitCode}'
```

Code `137` часто означает `SIGKILL`, но причину нужно подтверждать: OOMKilled, ручной kill или истёкший grace period.

## Связи

- [[Programming for DevOps]]
- [[Bash]]
- [[CLI Tools]]
- [[Linux Processes]]
- [[OOMKilled]]
