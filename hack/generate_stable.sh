#!/usr/bin/env bash

set -euo pipefail

if [[ "$#" -ne 1 ]]; then
    >&2 echo "Illegal number of parameters"
    >&2 echo "$0 <namespace|streams|result>"
    exit 1
fi

TMP_DIR="$(mktemp -d)"
#trap 'rm -rf ${TMP_DIR}' EXIT

cat >"${TMP_DIR}/a.json" <<'EOL'
{
    "apiVersion": "image.openshift.io/v1",
    "kind": "ImageStream",
    "metadata": {
        "name": "{{IS_NAME}}",
        "namespace": "{{IS_NAMESPACE}}"
    },
    "spec": {
        "lookupPolicy": {
            "local": false
        },
        "tags": []
    }  
}
EOL

IMAGESTREAMS_FILE='https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/test-platform-results/pr-logs/pull/openshift_release/48891/rehearse-48891-pull-ci-openshift-csi-external-attacher-master-e2e-aws-csi/1761921575579291648/artifacts/build-resources/imagestreams.json'
IS_NAMESPACE="${IS_NAMESPACE_ENV:-hongkliu-test-021}"
CONTEXT=build01
DRY_RUN=server
#DRY_RUN=none

create_streams () {
  echo "create yamls"
  curl -s ${IMAGESTREAMS_FILE} | jq -r '.items[]|select(.metadata.name=="stable")|.spec.tags[]|select(.from.name|contains("quay-proxy.ci.openshift.org"))' > "${TMP_DIR}/t1.json"
  jq --slurpfile tags "${TMP_DIR}/t1.json" '.spec.tags = $tags' "${TMP_DIR}/a.json" > "${TMP_DIR}/t2.json"
  curl -s ${IMAGESTREAMS_FILE} | jq -r '.items[]|select(.metadata.name=="stable")|.status.tags[]|select(.items[0].dockerImageReference | contains("quay-proxy.ci.openshift.org"))|{"name":.tag, "from": {"kind":"DockerImage","name":.items[0].dockerImageReference},"importPolicy":{"importMode":"PreserveOriginal"},"referencePolicy":{"type":"Local"}}' > "${TMP_DIR}/b.json"
  jq --slurpfile tags "${TMP_DIR}/b.json" '.spec.tags = $tags' "${TMP_DIR}/a.json" > "${TMP_DIR}/c.json"
  for is_name in stable stable-initial; do
    sed "s/{{IS_NAMESPACE}}/${IS_NAMESPACE}/g;s/{{IS_NAME}}/quay-proxy-${is_name}/g" "${TMP_DIR}/c.json" > "${TMP_DIR}/is.quay-proxy-${is_name}.json"
    sed "s/{{IS_NAMESPACE}}/${IS_NAMESPACE}/g;s/{{IS_NAME}}/quay-${is_name}/g;s/quay-proxy.ci.openshift.org/quay.io/g" "${TMP_DIR}/c.json" > "${TMP_DIR}/is.quay-${is_name}.json"
    sed "s/{{IS_NAMESPACE}}/${IS_NAMESPACE}/g;s/{{IS_NAME}}/quay-float-${is_name}/g;s/quay-proxy.ci.openshift.org/quay.io/g" "${TMP_DIR}/t2.json" > "${TMP_DIR}/is.quay-float-${is_name}.json"
  done 
  find "${TMP_DIR}" -maxdepth 1 -type f -name 'is.quay-*stable*.json' -print -exec oc --context "${CONTEXT}" create --as system:admin --dry-run="${DRY_RUN}" -f {} \;
}


set_up_namespace () {
  oc --context "${CONTEXT}" create ns "${IS_NAMESPACE}" --as system:admin
  oc --context "${CONTEXT}" label ns "${IS_NAMESPACE}" my-test=stable-stream-$(oc whoami) --as system:admin
  oc --context build01 -n hongkliu-test extract secret/stable-credentials --to=- --keys .dockerconfigjson > /tmp/dc.json
  oc --context "${CONTEXT}" create secret generic stable-credentials --from-file=.dockerconfigjson=/tmp/dc.json --type=kubernetes.io/dockerconfigjson -n "${IS_NAMESPACE}" --as system:admin
}

#set -x
show_results () {
  echo "===${IS_NAMESPACE}==="
  #oc --context "${CONTEXT}" get is -n "${IS_NAMESPACE}"
  printf "%-27s %-21s %-6s %-21s %-6s\n" "stream" "created" "tags" "last import" "duration(s)"
  for is_name in quay-proxy-stable quay-proxy-stable-initial quay-stable quay-stable-initial quay-float-stable quay-float-stable-initial; do
    created="$(oc --context "${CONTEXT}" get is -n "${IS_NAMESPACE}" "${is_name}" -o json | jq -r '.metadata.creationTimestamp')"
    length="$(oc --context "${CONTEXT}" get is -n "${IS_NAMESPACE}" "${is_name}" -o json | jq '.status.tags[]|select(((.items|length) > 0) and (.items[0].image|startswith("sha256:")))' | jq -s | jq length)"
    finished="$(oc --context build01 get is -n "${IS_NAMESPACE}" "${is_name}" -o json | jq -r '.status.tags[]|select(((.items|length) > 0) and (.items[0].image|startswith("sha256:")))|.items[0].created' | sort | tail -n 1)"  
    date1=$(date -jf "%Y-%m-%dT%H:%M:%SZ" "${created}" +%s)
    date2=$(date -jf "%Y-%m-%dT%H:%M:%SZ" "${finished}" +%s)
    diffSeconds="$(($date2-$date1))"
    printf "%-27s %-21s %-6s %-21s %-6s\n" "${is_name}" "${created}" "${length}" "${finished}" "${diffSeconds}"
  done 
}

CMD=$1

case $CMD in

  streams)
    create_streams
    ;;

  namespace)
    set_up_namespace
    ;;

  results)
    show_results
    ;;

  *)
    >&2 echo -n "unknown command"
    exit 1 
    ;;
esac

