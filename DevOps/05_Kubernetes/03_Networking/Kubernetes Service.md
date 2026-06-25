# Kubernetes Service

`Service` даёт стабильную точку доступа к набору Pods.

Pods пересоздаются и меняют IP, Service остаётся стабильным.

```text
client -> Service -> EndpointSlice -> Pod IP
```

---

# Типы Service

## ClusterIP

Доступен внутри cluster.

```yaml
type: ClusterIP
```

Самый частый вариант для internal services.

Подробно: [[ClusterIP]].

---

## NodePort

Открывает порт на каждой node.

```yaml
type: NodePort
```

Часто используется как низкоуровневая база для LoadBalancer, но вручную в production обычно неудобен.

Подробно: [[NodePort]].

---

## LoadBalancer

Просит cloud/controller создать внешний load balancer.

```yaml
type: LoadBalancer
```

Работает, если в cluster есть cloud controller или LB implementation.

Подробно: [[LoadBalancer Service]].

---

## ExternalName

Возвращает DNS CNAME на внешний host.

---

# Selector

Service выбирает Pods по labels:

```yaml
selector:
  app: backend
```

Если selector не совпадает с Pod labels, endpoints будут пустые.

Проверить:

```bash
kubectl get svc -n app
kubectl get endpoints -n app
kubectl get endpointslice -n app
kubectl get pods -n app --show-labels
```

---

# Port mapping

```yaml
ports:
  - port: 80
    targetPort: 8080
```

`port` — порт Service.

`targetPort` — порт container/Pod.

Port mismatch — частая причина 502/connection refused.

---

# Диагностика

```bash
kubectl describe svc backend -n app
kubectl get endpointslice -n app -l kubernetes.io/service-name=backend
kubectl run tmp --rm -it --image=curlimages/curl -- sh
```

Из debug Pod:

```bash
curl -v http://backend.app.svc.cluster.local
```

---

# Связанные заметки

- [[Endpoints]]
- [[EndpointSlice]]
- [[CoreDNS]]
- [[Ingress]]
- [[Kubernetes Service No Endpoints]]
- [[ClusterIP]]
- [[NodePort]]
- [[LoadBalancer Service]]
