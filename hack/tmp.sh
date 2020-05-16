#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail
cmd="echo"
if [[ "${DRY_RUN:-}" == "false" ]]; then
    cmd="oc"
fi
oc --context build01 get machine -n openshift-machine-api -l machine.openshift.io/cluster-api-machine-role=worker -o=jsonpath='{range .items[?(@.spec.providerSpec.value.blockDevices[0].ebs.volumeSize==600)]}{.metadata.name}{"\t"}{.status.nodeRef.name}{"\n"}{end}' | while read machine node; do
  echo $machine $node
  #${cmd} --context build01 --as system:admin adm cordon $node
  ${cmd} --context build01 --as system:admin annotate machine -n openshift-machine-api ${machine} machine.openshift.io/cluster-api-delete-machine=true
done
