# Test Automation

`Test Automation` — автоматический запуск проверок в CI.

Задача тестов в DevOps не “набрать coverage”, а остановить плохое изменение до deploy.

Тесты должны быть:

```text
быстрые для обратной связи
воспроизводимые
понятные при падении
изолированные от случайного внешнего состояния
```

---

# Уровни тестов

## Unit tests

Проверяют маленькую часть кода.

```bash
go test ./...
npm test
pytest
```

Обычно запускаются на каждый commit/MR.

---

## Integration tests

Проверяют взаимодействие с БД, broker, filesystem, API.

Часто используют Docker Compose или testcontainers.

```bash
docker compose -f compose.test.yaml up -d
pytest tests/integration
```

---

## E2E tests

Проверяют пользовательский сценарий целиком.

Дорогие и более хрупкие, поэтому их часто запускают перед release или на staging.

---

# Test reports

CI должен сохранять reports:

```text
junit xml
coverage
screenshots
logs
artifacts для debug
```

Иначе падение теста превращается в “смотри лог на 5000 строк”.

---

# Flaky tests

Flaky test — тест, который иногда падает без изменения кода.

Причины:

```text
race condition
зависимость от времени
общая БД между тестами
network dependency
порядок запуска тестов
```

Flaky tests нельзя просто rerun-ить бесконечно: они уничтожают доверие к CI.

---

# Связанные заметки

- [[Continuous Integration]]
- [[Build]]
- [[Artifacts and Cache]]
- [[Docker Compose]]
- [[Preview Environments]]
