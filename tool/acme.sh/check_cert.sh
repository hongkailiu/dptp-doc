#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

#https://unix.stackexchange.com/questions/234970/script-to-check-if-ssl-certificate-is-valid

# registry.svc.ci.openshift.org
# default-route-openshift-image-registry.apps.build01.ci.devcluster.openshift.com

if [[ "$#" -ne 1 ]]; then
  >&2 echo "[ERROR] Illegal number of parameters: Please specify the host[:port] to verfiy"
  exit 1
fi

TARGET=$1
readonly TARGET

curl --insecure -v "https://${TARGET}" 2>&1 | awk 'BEGIN { cert=0 } /^\* Server certificate:/ { cert=1 } /^\*/ { if (cert) print }'


