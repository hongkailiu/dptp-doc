#!/bin/bash

### This script is to sync the source secrets in the mapping of `ci-secret-controller`
### to build01 so that its deployment on build01 can sync them to their targets there

set -euo pipefail

BASH_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly BASH_DIR

#MAPPING_FILE="${BASH_DIR}/_mapping.yaml"
MAPPING_FILE="/Users/hongkliu/repo/openshift/release/core-services/secret-mirroring/_mapping.yaml"
readonly MAPPING_FILE

TMP_DIR=$(mktemp -d -t ci-XXXXXXXXXX)
trap 'rm -rf "${TMP_DIR}"' EXIT

SOURCE_SECRETS_FILE="${TMP_DIR}/source_secrets.txt"
readonly SOURCE_SECRETS_FILE

yq -r '.secrets[].to | .namespace + " " + .name ' "${MAPPING_FILE}" > ${SOURCE_SECRETS_FILE}

while read namespace name
do
  echo "handling ${namespace} ${name} ..."
  if ! oc --context build01 get project "${namespace}"; then
    oc --context build01 new-project "${namespace}" --skip-config-write=true
  fi
done < ${SOURCE_SECRETS_FILE}
