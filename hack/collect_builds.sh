#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

WORKDIR="$(mktemp -d)"
readonly WORKDIR

echo "files are saved ${WORKDIR}"

build=sanitize-prow-jobs-debug-1
namespace=bz002
cluster=build01

oc --context ${cluster} get build -n ${namespace} ${build} -o yaml > ${WORKDIR}/${cluster}.${namespace}.${build}.build.yaml
oc --context ${cluster} describe build -n ${namespace} ${build} > ${WORKDIR}/${cluster}.${namespace}.${build}.describe.txt

oc --context ${cluster} get pod -n ${namespace} ${build}-build -o yaml > ${WORKDIR}/${cluster}.${namespace}.${build}-build.pod.yaml
oc --context ${cluster} describe pod -n ${namespace} ${build}-build > ${WORKDIR}/${cluster}.${namespace}.${build}-build.describe.txt

cat ${WORKDIR}/${cluster}.${namespace}.${build}-build.pod.yaml | yq -r '.spec.initContainers[].name' | while read container; do
  echo $container
  oc --context ${cluster} logs -n ${namespace} ${build}-build -c ${container} > ${WORKDIR}/${cluster}.${namespace}.${build}-build.init.${container}.log
done

echo 111

cat ${WORKDIR}/${cluster}.${namespace}.${build}-build.pod.yaml | yq -r '.spec.containers[].name' | while read container; do
  echo $container
  oc --context ${cluster} logs -n ${namespace} ${build}-build -c ${container} > ${WORKDIR}/${cluster}.${namespace}.${build}-build.${container}.log
done

echo "files are saved ${WORKDIR}"