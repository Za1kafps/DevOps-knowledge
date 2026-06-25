# Containers in a Pod

Pod может содержать несколько типов containers. Они разделяют Pod network namespace и IP, могут разделять volumes, но имеют отдельные images, processes, resources, security context и restart state.

## Application containers

Основные долгоживущие процессы:

```yaml
spec:
  containers:
    - name: api
      image: registry.example.com/api:1.4.2
```

Несколько application containers допустимы, если они образуют одну эксплуатационную единицу и должны scheduling/scaling-иться вместе. Независимые сервисы должны жить в разных Pods.

## Regular init containers

Выполняются последовательно до application containers и должны успешно завершиться:

```yaml
spec:
  initContainers:
    - name: wait-for-db
      image: busybox:1.36
      command:
        - sh
        - -ec
        - until nc -z postgres 5432; do sleep 2; done
```

Применение:

- подготовить files в shared volume;
- выполнить короткую precondition check;
- получить конфигурацию;
- выставить permissions.

Init container не подходит для бесконечного ожидания без timeout. Ошибка блокирует запуск Pod и отображается в `.status.initContainerStatuses`.

## Sidecar containers

Sidecar работает рядом с основным приложением: proxy, log processor, config reloader. Kubernetes поддерживает native sidecar как restartable init container:

```yaml
spec:
  initContainers:
    - name: log-forwarder
      image: example/log-forwarder:1.2
      restartPolicy: Always
```

Такой sidecar запускается до последующих init/application containers и продолжает работать весь lifecycle Pod. Обычный второй container в `spec.containers` тоже часто называют sidecar pattern, но у него нет специального ordering lifecycle.

Sidecar потребляет CPU/memory, влияет на startup/termination и должен иметь собственные requests/limits.

## Ephemeral containers

Временный debug container внедряется в уже существующий Pod:

```bash
kubectl debug -it pod/api-7d9f --image=nicolaka/netshoot --target=api
```

Он полезен, когда application image distroless и не содержит shell/debug tools. Ephemeral container:

- не задаётся как обычная часть Pod template;
- не перезапускается автоматически;
- не имеет ports/probes/resources requests;
- не предназначен для workload;
- добавляется через специальный API и остаётся в Pod spec/status.

## Pause/infra container

Runtime создаёт Pod sandbox, который удерживает общие namespaces. В Linux реализация часто использует маленький pause container. Это runtime detail, а не container из `spec.containers`.

## Shared network

Все containers Pod обращаются друг к другу через `localhost`, поэтому не могут слушать один и тот же address/port одновременно.

## Shared process namespace

По умолчанию process namespace не общий. Его можно включить:

```yaml
spec:
  shareProcessNamespace: true
```

Это помогает sidecar/debug-сценариям, но увеличивает видимость процессов между containers.

## Диагностика

```bash
kubectl get pod <pod> -o jsonpath='{.spec.initContainers[*].name}'
kubectl get pod <pod> -o jsonpath='{.spec.containers[*].name}'
kubectl logs <pod> -c <container>
kubectl logs <pod> -c <container> --previous
kubectl describe pod <pod>
```

## Связи

- [[Pod]]
- [[Container Runtime and CRI]]
- [[kubectl debug]]
- [[Kubernetes Probes]]
- [[Resources Requests and Limits]]
- [[Distroless Images]]
