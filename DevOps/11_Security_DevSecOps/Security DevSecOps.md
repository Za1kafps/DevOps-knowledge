# Security DevSecOps

`DevSecOps` — это встраивание security-проверок и security-ownership в DevOps pipeline.

Это не отдельная магическая область поверх DevOps. Практически DevSecOps живёт на стыке:

```text
Security
CI-CD
Containers
Kubernetes
Infrastructure
Observability
```

---

# Что входит

```text
IAM and least privilege
secrets in CI/CD
SAST/dependency/container scanning
SBOM
image signing/provenance
policy as code
Kubernetes admission policies
audit logs
incident response
```

---

# Главная идея

Security должна быть:

```text
автоматизирована
проверяема
видна в pipeline
понятна владельцам сервисов
связана с risk/impact
```

Скан без triage не даёт безопасности.

Policy без ownership превращается в раздражение.

---

# Связанные заметки

- [[Security]]
- [[IAM]]
- [[Supply Chain Security]]
- [[Secrets in CI-CD]]
- [[OIDC in CI-CD]]
- [[Image Security]]
- [[Kubernetes Security]]
- [[Audit Logs]]
