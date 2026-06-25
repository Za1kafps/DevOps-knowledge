SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help

.PHONY: help fmt lint test build clean

help: ## Show targets
	@awk 'BEGIN {FS = ":.*## "}; /^[a-zA-Z0-9_.-]+:.*## / {printf "%-16s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

fmt: ## Format Go and Python
	gofmt -w .
	ruff format check_http.py test_check_http.py

lint: ## Run static checks
	go vet ./...
	ruff check check_http.py test_check_http.py

test: ## Run tests
	go test -race ./...
	python -m unittest -v

build: ## Build Linux binary
	CGO_ENABLED=0 go build -trimpath -o bin/healthcheck .

clean: ## Remove generated files
	rm -rf -- bin/ .pytest_cache/ __pycache__/
