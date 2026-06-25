# Go

Go часто используют для Kubernetes controllers, operators, exporters, CLI и сетевых сервисов. Основные эксплуатационные преимущества: статически собираемый бинарник, строгая типизация, быстрый startup и встроенные инструменты тестирования и профилирования.

## Модуль и сборка

```bash
go mod init example.com/healthcheck
go mod tidy
go fmt ./...
go vet ./...
go test ./...
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -trimpath -o bin/healthcheck ./cmd/healthcheck
```

`go mod tidy` синхронизирует `go.mod`/`go.sum`. `-trimpath` убирает локальные пути из результата сборки.

## CLI с корректным exit code

```go
package main

import (
	"context"
	"flag"
	"fmt"
	"os"
	"time"
)

func run(ctx context.Context, args []string) error {
	fs := flag.NewFlagSet("healthcheck", flag.ContinueOnError)
	url := fs.String("url", "", "health endpoint")
	if err := fs.Parse(args); err != nil {
		return err
	}
	if *url == "" {
		return fmt.Errorf("-url is required")
	}
	return check(ctx, *url)
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	if err := run(ctx, os.Args[1:]); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
```

Функция `run` тестируется без запуска процесса. `os.Exit` вызывается только в `main`, потому что deferred functions после него не выполняются.

## Ошибки

```go
if err != nil {
	return fmt.Errorf("read config %q: %w", path, err)
}
```

`%w` сохраняет цепочку для `errors.Is` и `errors.As`. Текст ошибки должен добавлять контекст, а не повторять “failed”.

## Context и graceful shutdown

`context.Context` передаёт deadline и отмену через вызовы. Его не хранят в глобальной переменной и обычно передают первым аргументом.

```go
ctx, stop := signal.NotifyContext(
	context.Background(),
	os.Interrupt,
	syscall.SIGTERM,
)
defer stop()
```

HTTP server при `SIGTERM` должен прекратить принимать новые запросы и завершить активные через `Server.Shutdown` с отдельным timeout.

## HTTP-клиент

```go
client := &http.Client{Timeout: 10 * time.Second}
req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
if err != nil {
	return err
}

resp, err := client.Do(req)
if err != nil {
	return err
}
defer resp.Body.Close()
```

Нельзя создавать новый `http.Client` на каждый запрос: теряется connection pooling. `resp.Body` нужно закрывать.

## Concurrency

Goroutine должна иметь понятное условие завершения. Channel не нужен для каждой задачи: иногда достаточно `errgroup` и context. Запускай race detector:

```bash
go test -race ./...
```

## Диагностика

```bash
go test -v ./...
go test -run TestName ./path/to/package
go test -bench=. -benchmem ./...
go tool pprof http://localhost:6060/debug/pprof/profile
govulncheck ./...
```

`pprof` endpoint нельзя бездумно публиковать наружу: он раскрывает внутреннее состояние процесса и может создавать нагрузку.

## Типовые ошибки

- goroutine leak из-за отсутствия cancellation;
- HTTP response body не закрыт;
- копирование mutex;
- unbounded concurrency;
- ignored error;
- map используется конкурентно без синхронизации;
- `time.After` создаётся в горячем цикле;
- panic применяется для обычной ошибки ввода.

## Связи

- [[Programming for DevOps]]
- [[Go Testing]]
- [[CLI Tools]]
- [[HTTP API]]
- [[Graceful Shutdown]]
- [[Prometheus]]
