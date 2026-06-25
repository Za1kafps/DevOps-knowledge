# DNS Failure

`DNS Failure` — домен не резолвится, резолвится не туда или разные клиенты получают разные ответы.

---

# Быстрая проверка

```bash
dig example.com
dig example.com A
dig example.com AAAA
dig @1.1.1.1 example.com
dig @8.8.8.8 example.com
```

Trace:

```bash
dig +trace example.com
```

Локальный resolver:

```bash
cat /etc/resolv.conf
resolvectl status
```

---

# Симптомы

## Could not resolve host

Проверить resolver и authoritative records.

## У части пользователей работает

Причины:

```text
TTL/cache
GeoDNS/CDN
AAAA IPv6 сломан
split-horizon DNS
разные resolvers
```

## По IP работает, по домену нет

Это DNS, Host header или TLS SNI.

Проверить:

```bash
curl -v -H "Host: example.com" http://1.2.3.4
curl -vk --resolve example.com:443:1.2.3.4 https://example.com
```

---

# Kubernetes DNS

```bash
kubectl -n kube-system get pods -l k8s-app=kube-dns
kubectl exec -it pod -n app -- nslookup kubernetes.default.svc.cluster.local
```

Проверить CoreDNS logs:

```bash
kubectl -n kube-system logs deploy/coredns
```

---

# Связанные заметки

- [[DNS]]
- [[CoreDNS]]
- [[Network]]
- [[HTTPS and TLS]]
