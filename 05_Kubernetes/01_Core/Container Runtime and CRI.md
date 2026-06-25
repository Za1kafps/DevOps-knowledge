# Container Runtime and CRI

Container runtime на каждой Kubernetes node создаёт Pod sandbox, скачивает images, запускает и останавливает containers. `kubelet` обращается к runtime через gRPC-интерфейс CRI.

```text
kubelet
  -> CRI RuntimeService / ImageService
    -> containerd или CRI-O
      -> OCI runtime: runc/crun
        -> Linux namespaces, cgroups, mounts, capabilities
```

## CRI, OCI и runtime

`CRI` — Kubernetes API между kubelet и high-level runtime.

`OCI Runtime Specification` описывает запуск container bundle. Низкоуровневый `runc` или `crun` создаёт процесс с namespaces/cgroups, но не занимается Kubernetes orchestration.

`containerd`:

- управляет lifecycle containers и images;
- использует CRI plugin;
- часто запускает OCI runtime `runc`;
- используется не только Kubernetes.

`CRI-O`:

- runtime, сфокусированный на Kubernetes CRI;
- использует OCI-compatible runtimes;
- часто встречается в OpenShift и Kubernetes-дистрибутивах.

Docker Engine не является CRI runtime напрямую. Старый встроенный `dockershim` удалён из Kubernetes; для Docker Engine требуется внешний `cri-dockerd`. Наличие container images формата OCI/Docker не означает, что node обязана запускать Docker daemon.

## Pod sandbox

Runtime сначала создаёт sandbox для Pod. Его network namespace и IP разделяются application containers Pod. В Linux sandbox часто виден как pause/infra container.

```text
Pod sandbox
  network namespace
  Pod IP
  containers join the sandbox
```

## Сокеты

Частые endpoints:

```text
/run/containerd/containerd.sock
/run/crio/crio.sock
```

Путь зависит от установки. Kubelet получает его через `--container-runtime-endpoint` или configuration.

## Диагностика

`crictl` работает с CRI независимо от конкретного runtime:

```bash
crictl info
crictl ps -a
crictl pods
crictl images
crictl inspect <container-id>
crictl inspectp <pod-id>
crictl logs <container-id>
```

Runtime service:

```bash
systemctl status containerd
journalctl -u containerd --since -30m
systemctl status crio
journalctl -u crio --since -30m
journalctl -u kubelet --since -30m
```

Для containerd дополнительно существует `ctr`, но это низкоуровневый debug-client, а не стабильная замена `crictl` для Kubernetes.

## Частые поломки

- kubelet не подключается к CRI socket;
- runtime и kubelet используют несовместимую CRI API version;
- disk заполнен images/snapshots;
- image pull падает из-за registry auth/DNS/TLS;
- cgroup driver kubelet и runtime настроены несовместимо;
- CNI не настроил sandbox network;
- OCI runtime не может применить seccomp/cgroup/mount.

## Связи

- [[Kubernetes Architecture]]
- [[kubelet]]
- [[Pod]]
- [[Containers]]
- [[Docker Image]]
- [[CNI]]
- [[ImagePullBackOff]]
