#!/usr/bin/env bash
set -Eeuo pipefail

readonly OUTPUT_DIR="${1:-incident-$(date -u +%Y%m%dT%H%M%SZ)}"
mkdir -m 0700 -- "$OUTPUT_DIR"

capture() {
  local name="$1"
  shift
  {
    printf '$'
    printf ' %q' "$@"
    printf '\n'
    timeout 15 "$@"
  } >"$OUTPUT_DIR/$name.txt" 2>&1 || true
}

capture date date -Is
capture uptime uptime
capture processes ps -eo pid,ppid,user,stat,%cpu,%mem,rss,etime,cmd --sort=-%cpu
capture memory free -h
capture vmstat vmstat 1 5
capture filesystem df -hT
capture inodes df -ih
capture sockets ss -s
capture listening ss -lntup
capture failed-units systemctl --failed --no-pager
capture kernel journalctl -k --since -30m --no-pager

printf 'snapshot written to %s\n' "$OUTPUT_DIR"
