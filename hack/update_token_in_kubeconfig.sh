#!/usr/bin/env bash
# KUBECONFIG_TOKEN=<COPY_FROM_CONSOLE> update_token_in_kubeconfig.sh <CONTEXT>

set -euo pipefail

if [[ "$#" -ne 1 ]]; then
    >&2 echo "Please specify the context name"
    exit 1
fi

CONTEXT=$1
readonly CONTEXT

if oc --context "${CONTEXT}" whoami > /dev/null 2>&1 ; then
  >&2 echo "The token for context $CONTEXT has not been expired"
  exit 1
fi

FOUND=false
for c in $(oc config view --output jsonpath="{.contexts[*].name}"); do
  if [[ "$c" = "$CONTEXT" ]]; then
    FOUND=true
    break
  fi
done

if [[ "$FOUND" != true ]]; then
  >&2 echo "Failed to find context $CONTEXT"
  exit 1
fi

TOKEN="${KUBECONFIG_TOKEN:-}"
readonly TOKEN

if [[ -z "$TOKEN" ]]; then
  >&2 echo "Env. Var. KUBECONFIG_TOKEN is not set"
  exit 1
fi

oc config set-credentials "${CONTEXT}" --token "${TOKEN}"
oc --context "${CONTEXT}" project
