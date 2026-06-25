# Task - Kubernetes Service Debug

## Симптом

`curl http://api.app.svc.cluster.local` возвращает timeout, connection refused или DNS error.

## Путь проверки

```text
DNS name
  -> Service ClusterIP and port
    -> EndpointSlice
      -> ready Pod IP and targetPort
        -> process listening address
          -> NetworkPolicy/dataplane
```

## Команды

```bash
kubectl get svc api -n app -o yaml
kubectl get endpointslice -n app \
  -l kubernetes.io/service-name=api -o yaml
kubectl get pods -n app -l app=api -o wide --show-labels
kubectl describe pod -n app -l app=api
```

Из debug Pod:

```bash
kubectl run netshoot --rm -it --restart=Never \
  --image=nicolaka/netshoot -- bash

dig api.app.svc.cluster.local
curl -sv http://api.app.svc.cluster.local
curl -sv http://<pod-ip>:<target-port>
nc -vz <pod-ip> <target-port>
```

В application Pod:

```bash
kubectl exec -n app <pod> -c api -- ss -lntp
```

Если image distroless:

```bash
kubectl debug -n app -it <pod> \
  --image=nicolaka/netshoot --target=api
```

## Матрица результата

DNS не работает, ClusterIP по IP работает:

```text
CoreDNS/resolver/search domain
```

ClusterIP не работает, PodIP работает:

```text
Service port, kube-proxy/eBPF dataplane
```

PodIP connection refused:

```text
process не слушает targetPort или слушает 127.0.0.1
```

EndpointSlice пуст:

```text
selector mismatch или Pods not Ready
```

## Сценарии

- поменять selector Service;
- указать ошибочный `targetPort`;
- сделать readiness fail;
- запретить ingress NetworkPolicy;
- переключить NodePort `externalTrafficPolicy: Local` и обратиться к node без local endpoint.

## Связи

- [[Kubernetes Service]]
- [[ClusterIP]]
- [[NodePort]]
- [[EndpointSlice]]
- [[Kubernetes Service No Endpoints]]
- [[kubectl debug]]
