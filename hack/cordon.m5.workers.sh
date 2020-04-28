#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

cmd="echo"
if [[ "${DRY_RUN:-}" == "false" ]]; then
    cmd="oc"
fi

oc --context build01 get machine -n openshift-machine-api -l machine.openshift.io/instance-type=m5.4xlarge,machine.openshift.io/cluster-api-machine-role=worker -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.nodeRef.name}{"\n"}{end}' | while read machine node; do
  echo $machine $node
  "${cmd}" --context build01 get node $node
  "${cmd}" --as system:admin --context build01 adm cordon $node
done