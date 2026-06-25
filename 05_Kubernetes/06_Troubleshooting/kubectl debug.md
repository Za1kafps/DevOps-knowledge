# kubectl debug

`kubectl debug` помогает диагностировать Pods/nodes через ephemeral containers или debug Pods.

---

# Ephemeral container

```bash
kubectl debug -it pod/app-123 -n app --image=nicolaka/netshoot --target=app
```

Полезно, если production image distroless и внутри нет shell/curl.

---

# Debug node

```bash
kubectl debug node/node-name -it --image=nicolaka/netshoot
```

---

# Что проверять

```bash
ip addr
ip route
ss -lntp
dig service.namespace.svc.cluster.local
curl -v http://service:port
```

---

# Осторожно

Debug container получает доступ к namespace Pod. Не использовать как обход security без audit.

---

# Связанные заметки

- [[Distroless Images]]
- [[Kubernetes Networking]]
- [[Troubleshooting]]
