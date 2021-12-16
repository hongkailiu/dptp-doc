#!/usr/bin/env bash

set -euo pipefail


for cluster in build01 build02
do
    echo ${cluster}
    identity_file=/tmp/identity-${cluster}.txt
    #oc --context $cluster get identity -o json > ${identity_file}
    cat ${identity_file} | jq -r '.items[]|select(.providerName=="github")|.metadata.name + " " + .user.name' | while read line; do
      username_name=$(echo $line | cut -d " " -f2)
      identity_name=$(echo $line | cut -d " " -f1)
      #TODO delete instead of get
      oc --context ${cluster} get user $username_name
      oc --context ${cluster} get identity $identity_name
    done
done