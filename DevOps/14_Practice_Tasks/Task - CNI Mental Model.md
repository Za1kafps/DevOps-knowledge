# Task - CNI Mental Model

## Цель

Проследить пакет между двумя Pods на разных nodes и объяснить, какие части выполняют Kubernetes, CNI plugin, Linux routing и Service dataplane.

## Что построить

```text
Pod A eth0
  -> veth / CNI dataplane
    -> node route, overlay или underlay
      -> destination node
        -> Pod B eth0
```

Отдельно:

```text
Pod A -> ClusterIP -> kube-proxy/eBPF translation -> Pod B
```

## Команды

```bash
kubectl get pods -A -o wide
kubectl get nodes -o wide
kubectl get daemonset -n kube-system
kubectl get networkpolicy -A
```

На node:

```bash
ip -br link
ip -br addr
ip route
ip rule
ip neigh
bridge link
ss -lunp
```

Dataplane:

```bash
iptables-save
nft list ruleset
bpftool prog show
bpftool map show
```

Не все команды применимы одновременно: iptables, nftables, IPVS и eBPF зависят от реализации cluster.

## Практика

1. Запусти два debug Pods на разных nodes.
2. Зафиксируй Pod IP, node IP и routes.
3. Проверь PodIP-to-PodIP.
4. Создай ClusterIP Service и сравни packet path.
5. Примени default-deny NetworkPolicy.
6. Разреши только конкретный namespace/port.
7. Сними `tcpdump` на Pod interface и node interface.

## Вопросы

- выдаёт ли CNI адреса сам или использует отдельный IPAM;
- overlay инкапсулирует VXLAN/Geneve или используется native routing;
- кто реализует Service: kube-proxy или eBPF;
- поддерживает ли plugin NetworkPolicy;
- где виден drop;
- как MTU overlay влияет на packet size.

## Связи

- [[CNI]]
- [[IPAM]]
- [[Pod-to-Pod Networking]]
- [[NetworkPolicy]]
- [[ClusterIP]]
- [[MTU]]
