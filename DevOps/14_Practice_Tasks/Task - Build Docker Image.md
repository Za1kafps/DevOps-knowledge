# Task - Build Docker Image

## Цель

Собрать минимальный reproducible image для HTTP-приложения, запустить его непривилегированным пользователем и проверить содержимое и vulnerability report.

## Требования

- multi-stage build;
- fixed base image tag, для строгой воспроизводимости digest;
- `.dockerignore`;
- процесс не работает от root;
- приложение корректно получает `SIGTERM`;
- secret не попадает в build args/layers;
- image содержит только runtime dependencies.

## Выполнение

```bash
docker build --pull --progress=plain -t local/app:test .
docker image inspect local/app:test
docker history --no-trunc local/app:test
docker run --rm --name app -p 8080:8080 local/app:test
curl --fail http://127.0.0.1:8080/health
docker stop --time 10 app
```

Проверить пользователя:

```bash
docker run --rm local/app:test id
```

Проверить image:

```bash
docker sbom local/app:test
trivy image --severity HIGH,CRITICAL local/app:test
```

## Сломать и диагностировать

1. Удали runtime shared library и найди ошибку startup.
2. Запусти приложение на privileged port непривилегированным user.
3. Укажи неправильный `ENTRYPOINT`.
4. Передай secret через `ARG` и найди его в `docker history`, затем исправь через BuildKit secret mount.
5. Собери без `.dockerignore` и сравни build context.

## Критерий готовности

- health endpoint отвечает;
- image запускается без root;
- повторная сборка использует cache предсказуемо;
- secret отсутствует в history/filesystem;
- объяснена разница `CMD` и `ENTRYPOINT`;
- описан rollback по immutable tag/digest.

## Связи

- [[Dockerfile]]
- [[Multi-stage Build]]
- [[BuildKit]]
- [[Docker Image]]
- [[Container Security]]
- [[Distroless Images]]
