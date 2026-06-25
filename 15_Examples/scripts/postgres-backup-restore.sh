#!/usr/bin/env bash
set -euo pipefail
: "${PGHOST:?}"
: "${PGUSER:?}"
: "${PGDATABASE:?}"
BACKUP_DIR="${BACKUP_DIR:-./backups}"
mkdir -p "$BACKUP_DIR"
FILE="$BACKUP_DIR/${PGDATABASE}_$(date -u +%Y%m%dT%H%M%SZ).dump"
pg_dump -Fc -h "$PGHOST" -U "$PGUSER" -d "$PGDATABASE" -f "$FILE"
echo "Backup: $FILE"
echo "Restore test: createdb ${PGDATABASE}_restore && pg_restore -d ${PGDATABASE}_restore $FILE"
