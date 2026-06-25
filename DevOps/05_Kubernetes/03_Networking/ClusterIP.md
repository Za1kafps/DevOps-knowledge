# ClusterIP

`ClusterIP` — стандартный тип Kubernetes Service. Он выделяет виртуальный IP, доступный внутри cluster, и направляет traffic к ready endpoints.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  type: ClusterIP
  selector:
    app: api
  ports:
    - name: http
      port: 80
      targetPort: http
```

```text
client Pod -> ClusterIP:80 -> EndpointSlice -> PodIP:targetPort
```

ClusterIP обычно не назначается interface. Dataplane реализуется kube-proxy через iptables/IPVS/nftables или eBPF CNI implementation.

## DNS

```text
api
api.namespace
api.namespace.svc.cluster.local
```

DNS name резолвится в ClusterIP. Для headless Service `clusterIP: None` DNS возвращает endpoint addresses вместо virtual IP.

## Проверка

```bash
kubectl get svc api -n app -o wide
kubectl get endpointslice -n app \
  -l kubernetes.io/service-name=api
kubectl run curl --rm -it --restart=Never \
  --image=curlimages/curl -- \
  curl -sv http://api.app.svc.cluster.local
```

## Когда не работает

- selector не совпадает с Pod labels;
- readiness false и endpoint не ready;
- `targetPort` не соответствует слушающему port;
- NetworkPolicy запрещает traffic;
- kube-proxy/CNI dataplane сломан;
- приложение слушает только `127.0.0.1`;
- CoreDNS сломан, хотя обращение по ClusterIP работает.

## Связи

- [[Kubernetes Service]]
- [[EndpointSlice]]
- [[CoreDNS]]
- [[kube-proxy]]
- [[NetworkPolicy]]
