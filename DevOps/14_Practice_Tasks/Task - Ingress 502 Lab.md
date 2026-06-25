# Task - Ingress 502 Lab

## Симптом

Внешний request доходит до Ingress Controller, но получает `502 Bad Gateway`.

```text
client -> LB -> Ingress Controller -> Service -> EndpointSlice -> Pod
```

## Сначала определить источник 502

```bash
curl -vk https://app.example.com/
```

Проверь response headers и логи ingress controller:

```bash
kubectl logs -n ingress-nginx \
  deploy/ingress-nginx-controller --since=10m
```

## Проверка маршрута

```bash
kubectl describe ingress app -n app
kubectl get svc app -n app -o yaml
kubectl get endpointslice -n app \
  -l kubernetes.io/service-name=app -o yaml
kubectl get pods -n app -o wide
```

Из controller Pod или debug Pod:

```bash
curl -sv http://app.app.svc.cluster.local
curl -sv http://<pod-ip>:<target-port>
```

## Сценарии 502

1. Service `targetPort` не совпадает с application port.
2. Application слушает `127.0.0.1`.
3. Backend ожидает HTTPS, controller использует HTTP.
4. Pod завершает connection reset.
5. Endpoint устарел во время termination.
6. NetworkPolicy разрешает client Pods, но запрещает ingress namespace.
7. Backend protocol annotation неверна.

Пустые endpoints чаще приводят к `503`, но точный code зависит от controller и configuration. Всегда подтверждай логом proxy.

## Отличить

```text
404 -> host/path/rule/default backend
502 -> proxy получил invalid response/connect/reset
503 -> нет доступного upstream или upstream unavailable
504 -> upstream не ответил до timeout
```

Это ориентир, а не универсальная гарантия всех proxies.

## Критерий готовности

Для каждого сценария покажи:

- внешний status;
- controller log;
- Service/EndpointSlice state;
- прямой request в backend;
- минимальное исправление.

## Связи

- [[Ingress 502]]
- [[Ingress]]
- [[Ingress Controller]]
- [[Kubernetes Service]]
- [[EndpointSlice]]
- [[Nginx 502]]
