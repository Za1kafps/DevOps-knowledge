# Python

Python удобен для API-клиентов, обработки структурированных данных, orchestration-скриптов и небольших внутренних сервисов. В отличие от Bash, он нормально моделирует данные, исключения и тестируемые функции.

## Изоляция окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

В CI зависимости должны быть зафиксированы lock-файлом или точными версиями. Глобальный `pip install` делает результат зависимым от состояния runner.

## Структура CLI

```python
import argparse
import logging
import sys

log = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--environment", required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    log.info("environment=%s dry_run=%s", args.environment, args.dry_run)
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raise SystemExit(main())
```

Бизнес-логику держат отдельно от parsing и `sys.exit`, иначе её неудобно тестировать.

## HTTP-клиент

```python
import requests


def fetch_health(base_url: str, token: str) -> dict:
    response = requests.get(
        f"{base_url.rstrip('/')}/health",
        headers={"Authorization": f"Bearer {token}"},
        timeout=(3.05, 10),
    )
    response.raise_for_status()
    return response.json()
```

Timeout обязателен. Пара `(connect, read)` разделяет время установки соединения и ожидания данных. `raise_for_status()` превращает HTTP 4xx/5xx в ошибку.

Для повторного использования соединений применяют `requests.Session`. Retry на `POST` требует понимания идемпотентности.

## Работа с subprocess

```python
import subprocess

result = subprocess.run(
    ["kubectl", "get", "pods", "-o", "json"],
    check=True,
    capture_output=True,
    text=True,
    timeout=30,
)
```

Список аргументов безопаснее `shell=True`: shell interpolation не нужен, а вход пользователя не превращается в команду.

## JSON и YAML

```python
import json
from pathlib import Path

data = json.loads(Path("input.json").read_text())
Path("output.json").write_text(json.dumps(data, indent=2) + "\n")
```

Для YAML используй `yaml.safe_load`, а не небезопасную загрузку произвольных Python objects.

## Ошибки и логирование

Лови исключение там, где можешь добавить контекст или выбрать действие:

```python
try:
    config = load_config(path)
except OSError as exc:
    log.error("cannot read config path=%s error=%s", path, exc)
    return 2
```

`except Exception: pass` скрывает root cause. Токены и пароли не должны попадать в exception context и debug logs.

## Качество

```bash
python -m compileall .
python -m pytest -q
ruff check .
ruff format --check .
mypy src
```

`ruff` ловит ошибки и стиль, `mypy` проверяет типы, но type hints не выполняют runtime validation.

## Типовые ошибки

- код запускается прямо при import;
- нет timeout у network call;
- mutable default argument: `items=[]`;
- naive datetime без timezone;
- секрет хранится в исходнике;
- dependency versions не зафиксированы;
- subprocess запускается через `shell=True`;
- весь код находится в одной функции и не тестируется.

## Связи

- [[Programming for DevOps]]
- [[Python Testing]]
- [[HTTP API]]
- [[JSON]]
- [[YAML]]
- [[CLI Tools]]
