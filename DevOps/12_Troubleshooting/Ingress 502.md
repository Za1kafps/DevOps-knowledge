# Ingress 502

`Ingress 502` означает, что Ingress controller не получил нормальный ответ от backend.

---

# Проверка

```bash
kubectl describe ingress <ingress> -n <ns>
kubectl get svc,endpointslice -n <ns>
kubectl get pods -n <ns> -o wide
kubectl logs -n ingress-nginx deploy/ingress-nginx-controller
```

Проверить backend изнутри:

```bash
kubectl run tmp --rm -it --image=curlimages/curl -- sh
curl -v http://service.namespace.svc.cluster.local
```

---

# Частые причины

```text
Service endpoints empty
wrong service port/targetPort
Pod not Ready
backend protocol mismatch
app timeout
NetworkPolicy blocks ingress controller
```

---

# Связанные заметки

- [[Ingress]]
- [[Nginx Ingress]]
- [[Kubernetes Service No Endpoints]]
- [[Nginx 502]]
