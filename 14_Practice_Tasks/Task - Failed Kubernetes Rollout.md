# Task - Failed Kubernetes Rollout

## Симптом

Deployment rollout завис или завершился `ProgressDeadlineExceeded`.

## Команды

```bash
kubectl rollout status deploy/api -n app --timeout=2m
kubectl describe deploy api -n app
kubectl get rs -n app --sort-by=.metadata.creationTimestamp
kubectl get pods -n app -o wide
kubectl get events -n app --sort-by=.lastTimestamp
```

Для нового Pod:

```bash
kubectl describe pod <pod> -n app
kubectl logs <pod> -n app -c api
kubectl logs <pod> -n app -c api --previous
```

## Сценарии

- `ImagePullBackOff`;
- `CrashLoopBackOff`;
- readiness не проходит;
- requests не помещаются на nodes;
- PVC pending;
- admission policy запрещает Pod;
- ConfigMap/Secret отсутствует;
- `maxUnavailable: 0`, но нет capacity для surge;
- application не завершает старые connections.

## Rollback

```bash
kubectl rollout history deploy/api -n app
kubectl rollout undo deploy/api -n app
kubectl rollout status deploy/api -n app --timeout=2m
```

Rollback не исправляет database migration и другие внешние side effects автоматически.

## Критерий готовности

- найдена конкретная condition/event;
- определено, новая или старая ReplicaSet обслуживает traffic;
- rollback проверен пользовательским request и metrics;
- исправлена причина, а не только увеличен deadline.

## Связи

- [[Deployment]]
- [[Rolling Update]]
- [[Readiness Probe]]
- [[Rollback]]
- [[Kubernetes Events]]
