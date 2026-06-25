# Kubernetes Security

`Kubernetes Security` — защита Kubernetes API, workloads, network, secrets и nodes.

Kubernetes безопасен только настолько, насколько настроены его policies.

---

# Основные слои

```text
API authentication
RBAC authorization
admission control
Pod securityContext
NetworkPolicy
Secrets encryption
image provenance/scanning
node hardening
audit logs
```

---

# RBAC

Проверять:

```bash
kubectl auth can-i get secrets -n prod
kubectl auth can-i '*' '*' --all-namespaces
```

Опасные права:

```text
create pods
get/list secrets
bind/escalate RBAC
create clusterrolebindings
access nodes/proxy
```

---

# Pod securityContext

Baseline:

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
```

---

# NetworkPolicy

Без NetworkPolicy часто весь namespace может ходить куда угодно.

Для sensitive workloads задавай ingress/egress явно.

---

# Secrets

Kubernetes Secret — base64 encoded object.

Нужно:

```text
encryption at rest
RBAC restriction
external secret management
no plaintext in Git
rotation
```

---

# Частые ошибки

## default ServiceAccount с правами

Каждый Pod получает token и лишний доступ.

## privileged containers

`privileged: true` резко снижает isolation.

## hostPath mount

Mount host filesystem может дать доступ к node.

---

# Связанные заметки

- [[RBAC]]
- [[ServiceAccount]]
- [[Secrets]]
- [[NetworkPolicy]]
- [[Container Security]]
- [[Supply Chain Security]]
