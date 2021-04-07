#!/usr/bin/env bash

set -euxo pipefail

TMP_DIR="$(mktemp -d -t ci-XXXXXXXXXX)"
readonly TMP_DIR
VERSION="$(curl -s https://amd64.ocp.releases.ci.openshift.org/api/v1/releasestream/4-stable/latest | jq -r .name)"
readonly VERSION
INSTALLED_VERSION="$(oc version --client -o json | jq -r .releaseClientVersion)"
readonly INSTALLED_VERSION

if [ "${VERSION}" = "${INSTALLED_VERSION}" ]; then
    echo "${INSTALLED_VERSION} is latest."
    exit
fi

curl -o "${TMP_DIR}/openshift-client-mac-${VERSION}.tar.gz" "https://openshift-release-artifacts.apps.ci.l2s4.p1.openshiftapps.com/${VERSION}/openshift-client-mac-${VERSION}.tar.gz"
tar -xzvf "${TMP_DIR}/openshift-client-mac-${VERSION}.tar.gz" -C "${TMP_DIR}"
mv "${TMP_DIR}/oc" "$HOME/bin"
oc version --client
