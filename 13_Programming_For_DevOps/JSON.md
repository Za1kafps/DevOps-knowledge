# JSON

JSON передаёт структурированные данные между API и инструментами. Он поддерживает object, array, string, number, boolean и `null`, но не comments, datetime или binary.

## Пример

```json
{
  "service": "api",
  "replicas": 3,
  "enabled": true,
  "ports": [8080, 9090],
  "metadata": null
}
```

Object keys всегда строки. Порядок keys не должен иметь semantic meaning.

## jq

```bash
# Проверить syntax
jq -e . response.json

# Получить поле
jq -r '.metadata.name' response.json

# Отфильтровать элементы
jq -r '.items[] | select(.status == "failed") | .name' response.json

# Построить новый object
jq '{name: .metadata.name, ready: .status.readyReplicas}' response.json
```

Без `-r` строка выводится как JSON string с кавычками. `-e` возвращает ненулевой exit code для `false`, `null` и parse error, что удобно в scripts.

## Поток и размер

Обычный parser загружает весь документ в memory. Для больших файлов используй streaming parser или NDJSON:

```json
{"time":"2026-01-01T00:00:00Z","level":"info"}
{"time":"2026-01-01T00:00:01Z","level":"error"}
```

Каждая строка NDJSON является отдельным JSON object.

## Числа

JSON не различает integer и floating point на уровне общего стандарта потребителей. Большой 64-bit ID может потерять точность в JavaScript, поэтому API иногда передают ID строкой.

## API contract

Schema должна определять:

- required fields;
- допустимые types и enum;
- формат timestamps;
- возможность `null`;
- поведение при неизвестных fields;
- backward compatibility.

Клиент не должен считать отсутствующее поле и `null` одним и тем же без определения API.

## Типовые ошибки

- trailing comma;
- comments внутри JSON;
- boolean записан строкой `"false"`;
- `jq` без `-r` передал кавычки следующей команде;
- secret dump попал в log;
- parser доверяет неограниченному body;
- shell парсит JSON через regex.

## Связи

- [[Programming for DevOps]]
- [[HTTP API]]
- [[YAML]]
- [[curl]]
- [[Logs]]
