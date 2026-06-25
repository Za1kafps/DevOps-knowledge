# Practice Tasks

Практика строится вокруг симптома и доказательства root cause. Задача считается выполненной, когда проблема воспроизведена, диагностика проведена от внешнего симптома к конкретному слою, исправление проверено, а не просто применено.

## Базовый порядок инцидента

```text
1. зафиксировать symptom, scope и время начала
2. проверить impact и недавние изменения
3. пройти путь request: DNS -> network -> proxy -> service -> process -> dependency
4. собрать факты до изменения системы
5. выполнить минимальное обратимое исправление
6. подтвердить recovery метриками и пользовательским запросом
7. записать root cause и preventive action
```

## Linux

- [[Task - Linux Incident Drill]]
- [[Task - High CPU Incident]]
- [[Task - Disk Full Incident]]

## Network и Kubernetes

- [[Task - Debug DNS]]
- [[Task - CNI Mental Model]]
- [[Task - Kubernetes Service Debug]]
- [[Task - Ingress 502 Lab]]
- [[Task - Failed Kubernetes Rollout]]
- [[Task - TLS Certificate Incident]]

Теория:

- типы containers в Pod: [[Containers in a Pod]];
- containerd, CRI-O и CRI: [[Container Runtime and CRI]];
- Deployment/StatefulSet: [[Deployment vs StatefulSet]];
- Service types: [[ClusterIP]], [[NodePort]], [[LoadBalancer Service]];
- probes: [[Kubernetes Probes]], [[Readiness Probe]], [[Liveness Probe]], [[Startup Probe]].

## Containers и CI/CD

- [[Task - Build Docker Image]]
- [[Task - Deploy With GitLab CI]]

## Databases

- [[Task - PostgreSQL Backup Restore]]

## Команды

- [[Incident Command Map]]
- [[Incident Response Flow]]
- [[Troubleshooting]]

## Результат каждой задачи

Сохрани:

- symptom и blast radius;
- команды и значимые строки вывода;
- подтверждённый root cause;
- временное и постоянное исправление;
- способ обнаружить повтор автоматически;
- rollback.

## Связи

- [[DevOps]]
- [[Programming for DevOps]]
- [[Observability]]
- [[Reliability and High Availability]]
