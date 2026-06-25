# Pod-to-Pod Networking

Pod-to-Pod networking — связь между Pod IP внутри cluster.

Kubernetes ожидает, что Pod может обратиться к Pod IP другого Pod без NAT, даже если Pods на разных nodes.

---

# Что участвует

```text
CNI plugin
Pod CIDR/IPAM
routes или overlay
node firewall
MTU
NetworkPolicy
```

---

# Проверка

```bash
kubectl get pods -A -o wide
kubectl run tmp --rm -it --image=curlimages/curl -- sh
curl -v http://<pod-ip>:<port>
```

Если Pod IP работает, а Service нет — проблема чаще в Service/EndpointSlice/kube-proxy.

Если Pod IP не работает между nodes — смотри CNI/routes/MTU/firewall.

---

# Частые проблемы

```text
CNI daemon не работает
Pod CIDR routes отсутствуют
overlay port закрыт firewall
MTU blackhole
NetworkPolicy запрещает traffic
```

---

# Связанные заметки

- [[CNI]]
- [[Kubernetes Networking]]
- [[NetworkPolicy]]
- [[MTU]]
