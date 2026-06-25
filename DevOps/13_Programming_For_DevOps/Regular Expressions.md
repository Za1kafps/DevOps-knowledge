# Regular Expressions

Regex ищет текстовые patterns. Он полезен для logs, validation простых форматов и extraction, но не заменяет parser для JSON, YAML, HTML, SQL или programming language.

## Базовые конструкции

```text
^          начало строки
$          конец строки
.          любой символ
[0-9]      класс символов
[^ ]       всё кроме пробела
*          0 или больше
+          1 или больше
?          0 или 1
{2,5}      от 2 до 5
(...)      группа
|          альтернатива
```

## grep

```bash
grep -E 'HTTP/[0-9.]+ (5[0-9]{2})' access.log
grep -Ev '^(#|$)' config
rg -n 'timeout|connection reset|refused' logs/
```

Quoting regex одинарными кавычками защищает `$`, `*` и backslash от shell expansion.

## Захват

Python:

```python
match = re.fullmatch(r"(?P<value>\d+)(?P<unit>ms|s|m)", text)
if not match:
    raise ValueError("invalid duration")
```

`fullmatch` подходит для validation всего значения. `search` ищет совпадение внутри строки.

## Производительность

Неудачный pattern с вложенными quantifiers может вызвать catastrophic backtracking:

```text
(a+)+$
```

Для input от пользователя ограничивай длину, избегай неоднозначных вложенных повторов и учитывай regex engine. Go `regexp` использует RE2-подобную модель без backtracking, но не поддерживает часть PCRE constructs.

## Когда нужен parser

Не применяй regex для:

- изменения Kubernetes YAML;
- чтения JSON response;
- разбора URL;
- shell command construction;
- проверки IP/CIDR.

Для этого есть структурированные libraries и `jq`/`yq`.

## Связи

- [[Programming for DevOps]]
- [[Bash]]
- [[Python]]
- [[Logs]]
- [[JSON]]
