# Makefile

`Makefile` задаёт короткие воспроизводимые команды для разработки и CI: build, test, lint, image, deploy. Make строит dependency graph целей и решает, какие recipes выполнить.

## Базовый пример

```make
SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help

APP := infra-check
VERSION ?= $(shell git describe --tags --always --dirty)

.PHONY: help fmt lint test build clean

help: ## Show available targets
	@awk 'BEGIN {FS = ":.*## "}; /^[a-zA-Z0-9_.-]+:.*## / {printf "%-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

fmt: ## Format source
	gofmt -w .

lint: ## Run static checks
	go vet ./...

test: ## Run tests
	go test -race ./...

build: ## Build binary
	CGO_ENABLED=0 go build -trimpath \
		-ldflags "-X main.version=$(VERSION)" \
		-o bin/$(APP) ./cmd/$(APP)

clean: ## Remove generated files
	rm -rf -- bin/
```

Recipe начинается TAB, а не spaces. Каждая строка recipe по умолчанию запускается в отдельном shell.

## Переменные

- `=` — recursive expansion;
- `:=` — значение вычисляется один раз;
- `?=` — default, если переменная не задана;
- `$$` — доллар, передаваемый shell;
- `$@` — имя текущей target;
- `$<` — первая prerequisite;
- `$^` — все prerequisites.

```make
ENV ?= dev

deploy:
	./scripts/deploy.sh "$(ENV)"
```

Запуск:

```bash
make deploy ENV=staging
```

## Dependencies

```make
bin/app: cmd/app/main.go go.mod go.sum
	go build -o $@ ./cmd/app
```

Make пропустит build, если target новее prerequisites. Для команд, которые не создают одноимённый файл, нужен `.PHONY`.

## CI

CI должен вызывать те же цели, что разработчик:

```yaml
script:
  - make lint
  - make test
  - make build
```

Не прячь критическую deploy logic внутри нечитаемого Makefile. Сложную логику вынеси в тестируемый script/program, а target оставь интерфейсом.

## Типовые ошибки

- recipe отступлен spaces;
- target не объявлен `.PHONY` и случайный файл блокирует запуск;
- переменная shell записана как `$VAR` вместо `$$VAR`;
- несколько строк ожидают один shell;
- `latest` используется как версия image;
- deploy target не имеет environment guard;
- локальная и CI-команда расходятся.

## Диагностика

```bash
make -n build
make --warn-undefined-variables test
make -d target
make -pRrq : 2>/dev/null
```

`make -n` показывает команды без выполнения, но recipes с recursive `$(MAKE)` могут вести себя отдельно.

## Связи

- [[Programming for DevOps]]
- [[Bash]]
- [[Test Automation]]
- [[CI-CD]]
- [[Dockerfile]]
