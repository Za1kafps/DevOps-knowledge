# DaemonSet

`DaemonSet` запускает Pod на каждой подходящей node.

Используется для node-level компонентов.

---

# Где нужен

```text
log agent
node exporter
CNI agent
storage agent
security agent
node local DNS/cache
```

---

# Проверка

```bash
kubectl get daemonset -A
kubectl describe daemonset <name> -n <ns>
kubectl get pods -n <ns> -o wide
```

Смотреть, на каких nodes нет Pod.

---

# Scheduling

DaemonSet учитывает:

```text
nodeSelector
affinity
tolerations
taints
```

Если на tainted node не появился Pod, проверь tolerations.

---

# Частые проблемы

## Не запускается на control-plane nodes

Нужна toleration для taint control-plane.

## Агент ломает node

DaemonSet runs everywhere, поэтому ошибка затрагивает весь cluster.

---

# Связанные заметки

- [[Pod]]
- [[node_exporter]]
- [[CNI]]
- [[Kubernetes Events]]
