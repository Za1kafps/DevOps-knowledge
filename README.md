# DevOps Knowledge Vault

A structured DevOps knowledge base focused on Linux, networking, containers, Kubernetes, CI/CD, observability, security, reliability and troubleshooting.

This repository is built as a Markdown/Obsidian vault. It is designed not as a random collection of notes, but as a connected technical map for learning, interview preparation, incident analysis and practical DevOps work.

## Purpose

The goal of this vault is to keep DevOps knowledge organized by real operational areas:

* Linux systems and process troubleshooting
* Networking, DNS, TCP/IP, routing and firewalls
* Docker and container runtime basics
* Kubernetes architecture and production concepts
* CI/CD and GitOps workflows
* Databases, storage and backups
* Monitoring, logs and observability
* Security, hardening and DevSecOps
* Reliability, high availability and incident response
* Practical troubleshooting scenarios and examples

## Structure

```text
DevOps/
├── 01_Linux/
├── 02_Network/
├── 03_Containers/
├── 04_CI-CD/
├── 05_Kubernetes/
├── 06_Databases/
├── 07_Infrastructure/
├── 08_Observability/
├── 09_Security/
├── 10_Reliability_HA/
├── 11_Security_DevSecOps/
├── 12_Troubleshooting/
├── 13_Programming_For_DevOps/
├── 14_Practice_Tasks/
└── 15_Examples/
```

## Main Topics

### Linux

Notes about Linux fundamentals, filesystems, processes, services, logs, systemd, permissions, resource usage and debugging tools such as `strace`, `lsof`, `ss`, `journalctl`, `top`, `htop` and `free`.

### Networking

Networking notes cover DNS, TCP/UDP, ports, routing, gateways, NAT, firewalls, packet flow, troubleshooting with `curl`, `ping`, `traceroute`, `tcpdump`, `ip route`, `ss` and related tools.

### Containers

Docker and container-related notes: images, containers, Docker Compose, networking, volumes, logs, published ports and common operational issues.

### Kubernetes

Kubernetes notes include pods, nodes, deployments, services, ingress, config maps, secrets, StatefulSets, scheduler, kubelet, control plane components, CNI, network policies and troubleshooting scenarios.

### CI/CD and GitOps

Notes about build pipelines, deployment automation, GitHub Actions, GitLab CI, FluxCD, Helm and general release workflows.

### Observability

Monitoring and debugging notes with Prometheus, Grafana, logs, metrics, alerting, service health checks and incident investigation.

### Security and DevSecOps

Security-focused notes about hardening, access control, secrets, TLS, firewalls, infrastructure exposure, Zero Trust ideas and secure deployment practices.

### Troubleshooting

Practical cases and diagnostic flows for situations such as:

* service does not start
* API is unavailable
* ingress returns 502/500
* DNS does not resolve
* port is busy
* packet goes through the wrong route
* container cannot start
* Kubernetes workload is stuck
* application works locally but fails through ingress or VPN

## How to Use

This vault can be opened directly in Obsidian or viewed on GitHub as a Markdown knowledge base.

Recommended usage:

1. Start from the main DevOps areas.
2. Open a topic such as Linux, Networking or Kubernetes.
3. Follow internal links between related concepts.
4. Use troubleshooting notes as practical checklists.
5. Add real incidents and commands after each practice session.

## Repository Type

This is a living technical knowledge base. It is continuously updated as new DevOps, infrastructure, troubleshooting and security topics are studied or practiced.

## Tech Focus

```text
Linux
Networking
Docker
Kubernetes
CI/CD
GitOps
Helm
FluxCD
Nginx
PostgreSQL
Redis
Prometheus
Grafana
Security
Troubleshooting
Markdown
Obsidian
```
