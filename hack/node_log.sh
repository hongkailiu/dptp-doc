#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

WORKDIR="$(mktemp -d)"
readonly WORKDIR

mkdir -p "${WORKDIR}"
for node in $( oc --context build01 get events --all-namespaces -o json | jq --raw-output '.items[] | select(.message | test(".*context deadline exceeded.")) | .source.host' | sort | uniq ); do
  if oc --context build01 get node "${node}"; then
    mkdir -p "${WORKDIR}/${node}"
    oc --as system:admin --context build01 adm node-logs "${node}" --unit=crio --unit=kubelet > "${WORKDIR}/${node}/journal.log"
  fi
done

echo "files are saved ${WORKDIR}"
