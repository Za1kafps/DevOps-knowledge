# Bash

`Bash` подходит для небольших сценариев, которые связывают системные команды, файлы и Unix pipes. Это не полноценная замена Python: shell особенно хрупок при работе со строками, массивами, JSON и сложной обработкой ошибок.

## Безопасный каркас

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

cleanup() {
  local rc=$?
  rm -f -- "${tmp_file:-}"
  exit "$rc"
}

trap cleanup EXIT
trap 'printf "failed at line %s\n" "$LINENO" >&2' ERR

main() {
  local environment="${1:?usage: $0 <environment>}"
  printf 'deploying environment=%s\n' "$environment"
}

main "$@"
```

`set -e` не заменяет обработку ошибок и имеет исключения в условиях, pipelines и command substitution. `-u` обнаруживает обращение к неинициализированной переменной. `pipefail` возвращает ошибку, если упала любая команда pipeline.

## Quoting

Почти всегда переменную нужно заключать в кавычки:

```bash
rm -f -- "$file"
for file in "${files[@]}"; do
  printf '%s\n' "$file"
done
```

Без кавычек Bash выполняет word splitting и glob expansion. Имя файла с пробелом или `*` меняет смысл команды. `--` завершает разбор options и защищает от имени файла вида `-rf`.

## Условия и арифметика

```bash
if [[ -f "$config" && -s "$config" ]]; then
  echo "config exists"
fi

if (( retries > 3 )); then
  exit 1
fi
```

Для Bash предпочтителен `[[ ... ]]`, а не старый `[ ... ]`: внутри меньше неожиданных split/glob эффектов.

## Надёжное чтение строк

```bash
while IFS= read -r line; do
  printf '%s\n' "$line"
done < "$file"

find /var/log -type f -print0 |
  while IFS= read -r -d '' file; do
    printf '%s\n' "$file"
  done
```

`for line in $(cat file)` ломает пробелы, пустые строки и glob-символы.

## Временные файлы и блокировки

```bash
tmp_file="$(mktemp)"
chmod 600 "$tmp_file"

exec 9>/run/lock/backup.lock
flock -n 9 || {
  echo "backup already running" >&2
  exit 75
}
```

Не используй предсказуемый `/tmp/result.$$`: возможны race condition и symlink attack.

## Проверка команд

```bash
require() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'required command not found: %s\n' "$1" >&2
    exit 127
  }
}

require curl
require jq
```

## Timeout и retry

```bash
for attempt in 1 2 3 4 5; do
  if timeout 10 curl --fail --silent --show-error "$url"; then
    exit 0
  fi
  sleep $((attempt * 2))
done

exit 1
```

Не повторяй автоматически неидемпотентный `POST`, если API не поддерживает idempotency key.

## Диагностика

```bash
bash -n script.sh
shellcheck script.sh
bash -x script.sh
PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: ' bash -x script.sh
```

`set -x` может вывести секреты. Не включай trace вокруг токенов и паролей.

## Типовые ошибки

- переменная без кавычек;
- pipeline скрывает ошибку первой команды;
- `curl` без `--fail` считает HTTP 500 успешным transport-вызовом;
- secret передан аргументом и виден через `ps`;
- скрипт создаёт ресурс повторно вместо проверки состояния;
- cleanup не вызывается при сигнале;
- парсинг JSON через `grep` и `cut` вместо `jq`.

## Связи

- [[Programming for DevOps]]
- [[Exit Codes]]
- [[Retries and Timeouts]]
- [[Linux Processes]]
- [[curl]]
