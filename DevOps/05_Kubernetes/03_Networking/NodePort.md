# NodePort

`NodePort` публикует Service на одном port каждой node:

```text
<NodeIP>:<nodePort> -> Service -> ready Pod endpoint
```

NodePort Service также получает ClusterIP.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  type: NodePort
  selector:
    app: api
  ports:
    - name: http
      port: 80
      targetPort: 8080
      nodePort: 30080
```

Default range обычно `30000-32767`, но cluster administrator может изменить `--service-node-port-range`.

## Маршрут traffic

При `externalTrafficPolicy: Cluster` node может перенаправить пакет к Pod на другой node. Source IP может быть SNAT-ирован, но traffic распределяется по cluster.

При `externalTrafficPolicy: Local` traffic идёт только в local endpoints:

- source IP клиента обычно сохраняется;
- node без local endpoint не должна обслуживать traffic;
- возможен imbalance, если Pods распределены неравномерно.

## Применение

- lab/bare metal;
- backend для внешнего load balancer;
- временная диагностика;
- инфраструктура, где LB сам направляет traffic на node ports.

Для пользовательского HTTP обычно удобнее LoadBalancer + Ingress/Gateway.

## Проверка

```bash
kubectl get svc api -n app
kubectl get nodes -o wide
curl -v http://<node-ip>:30080
```

На node проверяют firewall и service dataplane:

```bash
iptables-save | rg '30080|KUBE-NODEPORT'
nft list ruleset
```

Команда зависит от используемого kube-proxy/CNI режима.

## Частые поломки

- cloud/security group или host firewall блокирует port;
- выбран internal NodeIP вместо reachable address;
- `externalTrafficPolicy: Local`, но на node нет ready Pod;
- nodePort вне разрешённого range;
- kube-proxy/eBPF dataplane не запрограммирован.

## Связи

- [[Kubernetes Service]]
- [[ClusterIP]]
- [[LoadBalancer Service]]
- [[kube-proxy]]
- [[Firewall]]
