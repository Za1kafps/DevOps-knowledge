# Examples

Файлы в этом разделе можно использовать как основу для lab, но перед production их нужно адаптировать под registry, namespaces, policies и версии cluster.

## Programming

- `programming/main.go` — HTTP server с probes и graceful shutdown;
- `programming/main_test.go` — table boundary test через `httptest`;
- `programming/check_http.py` — JSON CLI healthcheck;
- `programming/test_check_http.py` — pytest с подменой HTTP boundary;
- `programming/Makefile` — единые local/CI targets.

## Kubernetes

- `kubernetes/deployment-probes-resources.yaml`;
- `kubernetes/pod-containers.yaml`;
- `kubernetes/service-types.yaml`;
- `kubernetes/statefulset-headless-service.yaml`;
- `kubernetes/deployment-service-ingress-probes.yaml`.

Проверка:

```bash
kubectl apply --dry-run=server -f <file>
kubeconform -strict <file>
```

## Operations

- `scripts/incident-snapshot.sh`;
- `scripts/postgres-backup-restore.sh`;
- `monitoring/prometheus-alerts.yml`;
- `nginx/reverse-proxy.conf`.

## Связи

- [[Programming for DevOps]]
- [[Practice Tasks]]
- [[Kubernetes]]
- [[CI-CD]]
