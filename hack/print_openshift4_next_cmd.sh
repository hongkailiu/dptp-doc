#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Illegal number of parameters"
  exit 1
fi

Y_STREAM_VERSION=$1
readonly Y_STREAM_VERSION

RELEASE_TXT_URL=https://mirror2.openshift.com/pub/openshift-v4/amd64/clients/ocp-dev-preview/latest-${Y_STREAM_VERSION}/release.txt
readonly RELEASE_TXT_URL

LINE=$(curl -s "${RELEASE_TXT_URL}" | grep 'Pull From: quay.io/openshift-release-dev/ocp-release-nightly@sha256:')
readonly LINE

PREFIX="Pull From: quay.io/openshift-release-dev/ocp-release-nightly@sha256:"
readonly PREFIX
SHA=${LINE#$PREFIX}
readonly SHA

PULL_SPEC="quay.io/openshift-release-dev/ocp-release-nightly@sha256:${SHA}"
readonly PULL_SPEC

echo "cmd: oc --context build02 adm upgrade --allow-explicit-upgrade --force --to-image ${PULL_SPEC}"
