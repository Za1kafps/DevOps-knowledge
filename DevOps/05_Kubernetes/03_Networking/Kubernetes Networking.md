# Kubernetes Networking

Kubernetes networking строится вокруг нескольких идей:

```text
каждый Pod получает IP
Pods могут общаться между nodes
Service даёт стабильный virtual IP/DNS
Ingress/Gateway публикует HTTP наружу
CNI реализует сеть
```

---

# Основные слои

```text
Pod IP
Service ClusterIP
EndpointSlice
Ingress/Gateway
CoreDNS
NetworkPolicy
CNI dataplane
```

---

# Диагностика по слоям

DNS:

```bash
kubectl exec -it pod -n app -- nslookup backend.app.svc.cluster.local
```

Service:

```bash
kubectl get svc,endpointslice -n app
```

Pod IP:

```bash
kubectl get pods -n app -o wide
curl http://pod-ip:port
```

Ingress:

```bash
kubectl describe ingress app -n app
curl -v -H "Host: app.example.com" http://lb-ip/
```

---

# Частые причины сетевых проблем

```text
selector не совпал
targetPort wrong
Pod not Ready
CoreDNS не работает
NetworkPolicy режет
CNI daemon down
MTU/overlay issue
```

---

# Связанные заметки

- [[CNI]]
- [[CoreDNS]]
- [[Kubernetes Service]]
- [[Ingress]]
- [[NetworkPolicy]]
