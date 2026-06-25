# kube-proxy

`kube-proxy` реализует Service networking на node.

Он следит за Services/EndpointSlices и настраивает dataplane, чтобы traffic на ClusterIP/NodePort попадал в Pods.

---

# Режимы

```text
iptables
IPVS
userspace old/rare
```

В eBPF CNI часть функций kube-proxy может заменяться eBPF dataplane.

---

# Что ломается

Если kube-proxy/dataplane сломан:

```text
Pod IP доступен напрямую
Service ClusterIP не работает
NodePort не работает
traffic распределяется неправильно
```

---

# Проверка

```bash
kubectl -n kube-system get pods -l k8s-app=kube-proxy -o wide
kubectl -n kube-system logs ds/kube-proxy
kubectl get svc,endpointslice -A
```

На node:

```bash
sudo iptables-save | grep KUBE-SVC
sudo ipvsadm -Ln
```

---

# Связанные заметки

- [[Kubernetes Service]]
- [[EndpointSlice]]
- [[CNI]]
- [[eBPF]]
