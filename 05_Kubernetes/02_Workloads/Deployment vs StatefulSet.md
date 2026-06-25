# Deployment vs StatefulSet

Deployment и StatefulSet управляют Pods, но дают разные гарантии identity, rollout и storage.

## Deployment

```text
api-7d9f68f9c7-bq2k9
api-7d9f68f9c7-xp6m4
```

- Pods взаимозаменяемы;
- имя и IP меняются при пересоздании;
- replicas могут создаваться/удаляться без стабильного ordinal;
- rollout выполняется через ReplicaSets;
- один общий PVC с `ReadWriteMany` возможен, но отдельный PVC на replica автоматически не создаётся;
- подходит для stateless API, frontend, workers.

## StatefulSet

```text
postgres-0
postgres-1
postgres-2
```

- Pod имеет стабильный ordinal и DNS identity;
- `volumeClaimTemplates` создаёт PVC для каждого ordinal;
- rollout и scaling по умолчанию упорядочены;
- обычно нужен headless Service для стабильных DNS records;
- подходит, когда приложение использует identity, leader/follower roles, quorum или локальный persistent volume.

## Что StatefulSet не делает

StatefulSet не превращает приложение в отказоустойчивую БД. Он не настраивает:

- replication;
- leader election;
- consistency;
- backup;
- failover;
- schema migration.

Эти функции реализует само приложение, operator или внешний control plane.

## Storage lifecycle

Удаление Pod не удаляет его PVC. При пересоздании Pod с тем же ordinal снова получает соответствующий claim. Политика retention на scale/delete задаётся отдельно и должна быть проверена до production.

## Headless Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  clusterIP: None
  selector:
    app: postgres
  ports:
    - name: postgres
      port: 5432
```

Pods доступны по именам вида:

```text
postgres-0.postgres.namespace.svc.cluster.local
```

## Выбор

Используй Deployment, если replica можно безболезненно заменить другой.

Используй StatefulSet, если конкретная replica должна сохранить identity/storage после пересоздания.

Не выбирай StatefulSet только потому, что приложение подключается к внешней БД: само приложение при этом может оставаться stateless.

## Связи

- [[Deployment]]
- [[StatefulSet]]
- [[ReplicaSet]]
- [[PVC]]
- [[Kubernetes Service]]
- [[Replication]]
