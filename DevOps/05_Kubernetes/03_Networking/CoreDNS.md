# CoreDNS

`CoreDNS` — DNS-сервер Kubernetes cluster.

Он резолвит Service и Pod DNS names.

---

# Service DNS

Формат:

```text
service.namespace.svc.cluster.local
```

Пример:

```text
postgres.db.svc.cluster.local
```

---

# Проверка

```bash
kubectl -n kube-system get pods -l k8s-app=kube-dns
kubectl -n kube-system logs deploy/coredns
kubectl exec -it pod -n app -- cat /etc/resolv.conf
kubectl exec -it pod -n app -- nslookup kubernetes.default.svc.cluster.local
```

---

# Частые проблемы

## DNS timeout из Pod

CoreDNS down, NetworkPolicy, CNI, node DNS issue.

## External DNS не резолвится

Проверить CoreDNS forwarders и upstream DNS.

## ndots latency

Много search domains может создавать лишние DNS queries.

---

# Связанные заметки

- [[DNS]]
- [[Kubernetes Service]]
- [[DNS Failure]]
- [[Kubernetes Networking]]
