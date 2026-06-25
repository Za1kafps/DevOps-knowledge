# StatefulSet

`StatefulSet` управляет stateful Pods со стабильными именами и storage.

В отличие от Deployment, StatefulSet даёт:

```text
stable pod name
stable network identity
ordered rollout
volumeClaimTemplates
```

---

# Имена

Pods получают имена:

```text
postgres-0
postgres-1
postgres-2
```

Это важно для кластеров, где identity имеет значение.

---

# Storage

`volumeClaimTemplates` создаёт отдельный PVC на Pod.

При удалении Pod PVC обычно остаётся.

---

# Когда использовать

```text
databases
queues
systems with quorum
clustered storage
apps requiring stable identity
```

Не используй StatefulSet для stateless API только “на всякий случай”.

StatefulSet даёт identity и orchestration, но не настраивает replication, quorum, backup или automatic database failover. Это делает приложение, operator или внешний control plane.

Подробное сравнение: [[Deployment vs StatefulSet]].

---

# Диагностика

```bash
kubectl get statefulset -A
kubectl describe statefulset <name> -n <ns>
kubectl get pvc -n <ns>
kubectl get pods -n <ns> -o wide
```

---

# Связанные заметки

- [[Pod]]
- [[PVC]]
- [[StorageClass]]
- [[Replication]]
- [[Databases]]
- [[Deployment vs StatefulSet]]
