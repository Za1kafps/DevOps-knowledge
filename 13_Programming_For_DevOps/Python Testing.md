# Python Testing

Тесты automation-кода защищают от ошибок в parsing, API contracts, retry logic и destructive operations. В Python для этого часто используют `pytest`.

## Структура

```text
src/infra_check/
  api.py
tests/
  test_api.py
pyproject.toml
```

Тесты обнаруживаются в файлах `test_*.py` и `*_test.py`.

```python
from infra_check.api import normalize_url


def test_normalize_url_removes_trailing_slash():
    assert normalize_url("https://api.example.com/") == "https://api.example.com"
```

## Arrange, Act, Assert

```python
def test_select_unhealthy_hosts():
    hosts = [
        {"name": "a", "healthy": True},
        {"name": "b", "healthy": False},
    ]

    result = select_unhealthy_hosts(hosts)

    assert result == ["b"]
```

Один тест должен проверять одно поведение, а имя объяснять ожидаемый результат.

## Parametrize

```python
import pytest


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("30s", 30),
        ("2m", 120),
        ("1h", 3600),
    ],
)
def test_parse_duration(value, expected):
    assert parse_duration(value) == expected
```

## Exceptions

```python
def test_rejects_negative_timeout():
    with pytest.raises(ValueError, match="timeout"):
        parse_timeout("-1")
```

## Fixtures и временные файлы

```python
import json


def test_load_config(tmp_path):
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"environment": "test"}))

    assert load_config(config)["environment"] == "test"
```

Fixture должна очищать созданные ресурсы. Для внешней БД лучше создавать изолированную database/schema и удалять её после теста.

## Mock на границе

Не mock каждую внутреннюю функцию. Подменяй network, clock, filesystem или subprocess boundary:

```python
def test_healthcheck_uses_timeout(monkeypatch):
    calls = []

    def fake_get(url, *, timeout):
        calls.append((url, timeout))
        return FakeResponse(200)

    monkeypatch.setattr("infra_check.api.requests.get", fake_get)
    check_health("https://example.com")

    assert calls == [("https://example.com/health", 5)]
```

## Запуск

```bash
python -m pytest
python -m pytest -q
python -m pytest tests/test_api.py::test_name
python -m pytest -x
python -m pytest --maxfail=1
```

Для coverage:

```bash
python -m pytest --cov=infra_check --cov-report=term-missing
```

Coverage показывает исполненные строки, но не качество assertions.

## Что тестировать

- parsing и validation;
- формирование request;
- mapping status codes на ошибки;
- timeout/retry limits;
- dry-run;
- partial failure;
- redaction secrets;
- idempotent repeated execution.

## Связи

- [[Python]]
- [[Test Automation]]
- [[HTTP API]]
- [[CI-CD]]
