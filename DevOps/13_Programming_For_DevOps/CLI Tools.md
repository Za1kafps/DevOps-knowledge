# CLI Tools

Хороший CLI предсказуем для человека и автоматизации: имеет стабильные arguments, понятные exit codes, разделяет результат и диагностику, не требует интерактивного ввода в CI.

## Контракт CLI

```text
tool <command> [flags] [arguments]
```

Пример:

```bash
infra-check dns --server 10.96.0.10 --name api.default.svc.cluster.local --timeout 3s
```

Основные свойства:

- `--help` работает без внешних зависимостей;
- `--version` выводит версию и commit;
- флаги имеют разумные defaults;
- секрет можно передать через environment/file/stdin, но не обязательным argv;
- машинный вывод доступен через `--output json`;
- цвет отключается при non-TTY или через `NO_COLOR`;
- destructive operation поддерживает `--dry-run` и явное подтверждение.

## stdout и stderr

`stdout` содержит результат, который можно передать дальше:

```bash
tool list --output json | jq '.items[]'
```

`stderr` содержит progress, warning и диагностику. Это позволяет перенаправлять данные независимо:

```bash
tool export >result.json 2>export.log
```

## Exit codes

- `0` — команда выполнена;
- `1` — общая runtime error;
- `2` — неверные arguments/config;
- `126` — файл найден, но не исполняется;
- `127` — команда не найдена;
- `128 + signal` — завершение сигналом в shell convention.

Собственные коды документируют и не меняют без причины. Для вызывающего процесса важнее категория ошибки, чем десятки нестабильных кодов.

## Конфигурация и приоритет

Обычно:

```text
flags > environment > config file > defaults
```

Инструмент должен уметь показать эффективную конфигурацию без раскрытия secrets.

## Совместимость

- не меняй смысл существующего flag;
- deprecated option сначала предупреждает, затем удаляется в major release;
- JSON schema вывода версионируется;
- timestamps выводятся в RFC 3339 с timezone;
- sorting фиксирован, если вывод сравнивается в CI.

## Сигналы

Долгая команда обрабатывает `SIGINT`/`SIGTERM`, прекращает создавать новую работу, закрывает временные файлы и возвращает ненулевой код. Второй сигнал может завершить процесс немедленно.

## Проверка

```bash
tool --help
tool --version
tool check --output json | jq -e .
timeout 5 tool wait
tool invalid-command; echo "$?"
```

## Типовые ошибки

- prompts блокируют CI;
- логи смешаны с JSON в stdout;
- success возвращает code 1 или failure code 0;
- token передаётся через `--token` и виден в process list;
- нет timeout;
- команда частично изменила состояние, но не сообщает что именно;
- output зависит от локальной timezone/locale.

## Связи

- [[Programming for DevOps]]
- [[Exit Codes]]
- [[Bash]]
- [[Python]]
- [[Go]]
