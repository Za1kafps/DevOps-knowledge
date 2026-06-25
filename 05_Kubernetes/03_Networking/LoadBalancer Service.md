# LoadBalancer Service

Service `type: LoadBalancer` просит внешний controller выделить load balancer и направить traffic к Service.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ingress-nginx
spec:
  type: LoadBalancer
  selector:
    app: ingress-nginx
  ports:
    - name: https
      port: 443
      targetPort: 8443
```

Kubernetes сам не предоставляет внешний балансировщик. Реализацию даёт cloud controller, MetalLB, kube-vip или другая интеграция.

## Возможные datapath

```text
client -> cloud LB -> NodePort -> Service dataplane -> Pod
```

или direct-to-Pod/implementation-specific routing. Детали зависят от provider и `loadBalancerClass`.

Обычно LoadBalancer Service также создаёт ClusterIP и NodePort. Если реализация поддерживает прямой маршрут, allocation NodePort можно отключить через `allocateLoadBalancerNodePorts: false`.

## External traffic policy

`Cluster`:

- любой node может принять traffic;
- возможно дополнительное перенаправление между nodes;
- client source IP может быть потерян.

`Local`:

- traffic только к local endpoints;
- source IP обычно сохраняется;
- требуется корректная LB health check и равномерное размещение Pods.

## Проверка

```bash
kubectl get svc ingress-nginx -n ingress-nginx -o wide
kubectl describe svc ingress-nginx -n ingress-nginx
kubectl get endpointslice -n ingress-nginx
kubectl get events -n ingress-nginx --sort-by=.lastTimestamp
```

Если `EXTERNAL-IP` остаётся `<pending>`, в cluster нет подходящего LB controller, не хватает cloud permissions/quota или configuration не поддерживается.

## Не путать

LoadBalancer Service публикует L4 TCP/UDP Service. [[Ingress]] и [[Gateway API]] маршрутизируют application traffic, обычно через controller, который сам опубликован LoadBalancer Service.

## Связи

- [[Kubernetes Service]]
- [[NodePort]]
- [[Load Balancing]]
- [[Ingress]]
- [[Gateway API]]
- [[Ingress Controller]]
