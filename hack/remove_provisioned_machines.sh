#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

cmd="echo"
if [[ "${DRY_RUN:-}" == "false" ]]; then
    cmd="oc"
fi

oc --context build01 get machine -l machine.openshift.io/cluster-api-machine-role=worker -n openshift-machine-api -o=jsonpath='{range .items[?(@.status.phase=="Provisioned")]}{.metadata.name}{"\t"}{.status.nodeRef.name}{"\n"}{end}' | while read machine node; do
  echo $machine $node
  ${cmd} --context build01 --as system:admin annotate machine -n openshift-machine-api ${machine} Machine.openshift.io/cluster-api-delete-Machine=true
done