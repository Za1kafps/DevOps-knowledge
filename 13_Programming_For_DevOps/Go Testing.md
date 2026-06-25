# Go Testing

Go включает unit tests, benchmarks, fuzzing и race detector в стандартный toolchain. Test-файл называется `*_test.go`, функция — `TestXxx(t *testing.T)`.

## Unit test

```go
func TestNormalizeURL(t *testing.T) {
	got := NormalizeURL("https://api.example.com/")
	want := "https://api.example.com"
	if got != want {
		t.Fatalf("NormalizeURL() = %q, want %q", got, want)
	}
}
```

## Table-driven tests

```go
func TestParseDuration(t *testing.T) {
	tests := []struct {
		name    string
		input   string
		want    time.Duration
		wantErr bool
	}{
		{name: "seconds", input: "30s", want: 30 * time.Second},
		{name: "minutes", input: "2m", want: 2 * time.Minute},
		{name: "invalid", input: "later", wantErr: true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := ParseDuration(tt.input)
			if (err != nil) != tt.wantErr {
				t.Fatalf("error = %v, wantErr %v", err, tt.wantErr)
			}
			if got != tt.want {
				t.Errorf("got %v, want %v", got, tt.want)
			}
		})
	}
}
```

## HTTP test server

```go
func TestClientHealth(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/health" {
			t.Fatalf("path = %q", r.URL.Path)
		}
		w.WriteHeader(http.StatusOK)
	}))
	defer server.Close()

	client := NewClient(server.URL)
	if err := client.Health(context.Background()); err != nil {
		t.Fatal(err)
	}
}
```

`httptest.Server` проверяет реальный HTTP boundary без внешней сети.

## Interface вместо глобального mock

```go
type Clock interface {
	Now() time.Time
}
```

Маленький interface определяют рядом с потребителем. Это позволяет подменить clock/client/storage, не превращая весь проект в набор mock.

## Запуск

```bash
go test ./...
go test -v ./...
go test -run '^TestClientHealth$' ./internal/client
go test -count=100 ./...
go test -race ./...
go test -coverprofile=coverage.out ./...
go tool cover -func=coverage.out
```

`-count=100` помогает находить flaky tests, `-race` обнаруживает data race во время конкретного execution path.

## Benchmark

```go
func BenchmarkParse(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Parse(sample)
	}
}
```

```bash
go test -bench=. -benchmem ./...
```

## Fuzz test

```go
func FuzzParseNeverPanics(f *testing.F) {
	f.Add("30s")
	f.Fuzz(func(t *testing.T, value string) {
		_, _ = ParseDuration(value)
	})
}
```

Fuzzing особенно полезен для parsers, decoders и boundary input.

## Типовые ошибки

- test зависит от реального internet/API;
- parallel test изменяет общую global state;
- assertion проверяет implementation, а не behaviour;
- timeout отсутствует и test зависает;
- `t.Fatal` вызывается из чужой goroutine;
- flaky test просто rerun-ится в CI без исправления причины.

## Связи

- [[Go]]
- [[Test Automation]]
- [[HTTP API]]
- [[CI-CD]]
