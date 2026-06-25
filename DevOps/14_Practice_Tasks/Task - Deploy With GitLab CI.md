# Task - Deploy With GitLab CI

## Цель

Построить pipeline, который тестирует приложение, собирает immutable image, публикует его и выполняет контролируемый deploy с проверкой rollout и rollback.

## Pipeline

```text
lint -> unit test -> build -> image scan -> push -> deploy -> verify
```

Image tag должен включать commit SHA:

```text
registry.example.com/app:$CI_COMMIT_SHA
```

## Минимальные требования

- jobs используют pinned image versions;
- cache не подменяет artifacts;
- secrets находятся в protected/masked variables или external secret store;
- production job доступен только protected branch/tag;
- deploy serialised через `resource_group`;
- environment имеет URL и deployment history;
- rollout failure завершает job ненулевым code;
- rollback использует предыдущий digest.

## Проверки job

```bash
make lint
make test
docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA" .
docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA"
```

Kubernetes deploy:

```bash
kubectl -n app set image deploy/app \
  app="$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA"
kubectl -n app rollout status deploy/app --timeout=5m
kubectl -n app get pods
```

## Сломать

1. Unit test fails.
2. Registry token не имеет push permission.
3. Runner не резолвит cluster endpoint.
4. ImagePullSecret отсутствует.
5. Readiness новой версии всегда false.
6. Два deploy pipeline стартуют одновременно.
7. Job успешен, хотя `kubectl rollout status` упал.

## Диагностика

```bash
env | sort
getent hosts "$KUBE_HOST"
curl -vk --connect-timeout 3 "$KUBE_HOST/version"
kubectl auth can-i patch deployment -n app
kubectl get events -n app --sort-by=.lastTimestamp
```

Не печатай environment целиком, если там secrets. Для диагностики выводи только allowlist переменных.

## Критерий готовности

- artifact/image однозначно связан с commit;
- failed rollout делает pipeline failed;
- параллельные deploy не конфликтуют;
- rollback проверен;
- production credentials минимальны и protected.

## Связи

- [[GitLab CI]]
- [[CI-CD]]
- [[Deploy to Kubernetes]]
- [[Rollback]]
- [[Supply Chain Security]]
