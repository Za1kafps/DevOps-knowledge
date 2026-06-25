# Task - Debug DNS

## Симптом

Приложение возвращает:

```text
lookup api.internal: no such host
temporary failure in name resolution
SERVFAIL
```

## Задача

Определить, где ломается resolution: application configuration, resolver, search domain, authoritative DNS, CoreDNS или network path к DNS server.

## Диагностика на Linux

```bash
getent ahosts api.internal
resolvectl query api.internal
cat /etc/resolv.conf
dig api.internal A
dig +trace example.com
dig @<dns-server> api.internal A
tcpdump -ni any port 53
```

Сравни:

- имя с точкой и без: `api.internal` / `api.internal.`;
- A и AAAA;
- system resolver и прямой `dig`;
- UDP и TCP: `dig +tcp`;
- ответ `NXDOMAIN`, `SERVFAIL`, timeout.

## Kubernetes

```bash
kubectl run dns-test --rm -it --restart=Never \
  --image=registry.k8s.io/e2e-test-images/dnsutils:1.3 -- sh

cat /etc/resolv.conf
nslookup kubernetes.default.svc.cluster.local
nslookup api.app.svc.cluster.local
```

CoreDNS:

```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns
kubectl get configmap coredns -n kube-system -o yaml
kubectl get svc kube-dns -n kube-system
```

## Сценарии поломки

1. Неверное service name/namespace.
2. `NetworkPolicy` блокирует UDP/TCP 53.
3. Неверный upstream resolver в CoreDNS.
4. Слишком большой `ndots` создаёт лишние search-запросы.
5. AAAA возвращается, но IPv6 route отсутствует.
6. `systemd-resolved` stub address недоступен из container.

## Критерий готовности

Нужно показать packet/request path, конкретный failed response и исправление. `ping` не является достаточной проверкой DNS или application port.

## Связи

- [[DNS]]
- [[CoreDNS]]
- [[DNS Failure]]
- [[NetworkPolicy]]
- [[tcpdump]]
