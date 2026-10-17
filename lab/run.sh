#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export COMPOSE_PROJECT_NAME="${COMPOSE_PROJECT_NAME:-vbox-ovf-href-dest-escape}"
export PYTHONUNBUFFERED=1

LABEL="vbox-ovf-href-dest-escape"
WITNESS="VBOX-OVF-HREF-DEST-ESCAPE-WITNESS"

down() {
  echo "== docker compose down -v =="
  docker compose -p "${COMPOSE_PROJECT_NAME}" down -v --remove-orphans || true
}

fail_setup() {
  local reason="$1"
  echo "FAIL ${LABEL} ${reason} ${WITNESS}" | tee poc-last-run.txt
  exit 1
}

trap down EXIT

echo "== docker compose down (clean) =="
down

echo "== docker compose build =="
build_ok=0
for attempt in $(seq 1 5); do
  if docker compose -p "${COMPOSE_PROJECT_NAME}" build; then
    build_ok=1
    break
  fi
  echo "compose-build-retry attempt=${attempt}"
  sleep 8
done
if [[ "${build_ok}" != 1 ]]; then
  fail_setup "compose-build-failed"
fi

echo "== docker compose run gadget =="
up_ok=0
rc=1
for attempt in $(seq 1 5); do
  set +e
  docker compose -p "${COMPOSE_PROJECT_NAME}" run --rm --no-deps -T gadget \
    | tee poc-last-run.txt
  rc=${PIPESTATUS[0]}
  set -e
  if [[ "${rc}" -eq 0 ]] || [[ "${rc}" -eq 1 ]]; then
    up_ok=1
    break
  fi
  echo "compose-run-retry attempt=${attempt} rc=${rc}"
  sleep 8
  down
done
if [[ "${up_ok}" != 1 ]]; then
  fail_setup "compose-run-failed"
fi

if ! tail -n1 poc-last-run.txt 2>/dev/null | grep -qE '^(SUCCESS|FAIL) '; then
  echo "FAIL ${LABEL} poc-exit=${rc} ${WITNESS}" >> poc-last-run.txt
  rc=1
fi

exit "${rc}"
