#!/usr/bin/env bash
set -euo pipefail
DATE="$(date +%F_%H-%M-%S)"
OUT="/backup/postgres/appdb_${DATE}.dump"
mkdir -p /backup/postgres
pg_dump -Fc -h "${PGHOST:-localhost}" -U "${PGUSER:-app}" "${PGDATABASE:-appdb}" > "$OUT"
find /backup/postgres -type f -name '*.dump' -mtime +14 -delete
echo "backup created: $OUT"
