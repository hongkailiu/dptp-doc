#!/usr/bin/env bash

set -euo pipefail

MAPPING_FILE=/tmp/github-ldap-mapping.txt
readonly MAPPING_FILE

oc --context app.ci get cm -n ci github-ldap-mapping -o yaml | yq -r '.data."mapping.yaml"' > ${MAPPING_FILE}

RELEASE_REPO=/Users/hongkliu/repo/openshift/release
readonly RELEASE_REPO
CLUSTERS_FOLDER=${RELEASE_REPO}/clusters

while read line; do
  echo $line
  if [[ "$line" != *": "* ]]; then
    echo "Invalid line=${line}="
    continue
  fi
  github_user="${line%%:*}"
  ldap_user=$(echo ${line#*:} | xargs)
  # those are interesting github usernames
  if [[ ${github_user} == "github.com" || ${github_user} == "filter" || ${github_user} == "openshift" || ${github_user} == "ansible" || ${github_user} == "ansible-security" ]] ; then
    # overkill otherwise
    continue
  fi
  if [[ ${github_user} == ${ldap_user} ]]; then
    echo "same username on both IDPs: ${github_user}."
    continue
  fi
  if rg ": ${github_user}$" ${MAPPING_FILE} ; then
    echo "used in both IDPs but for different users: ${github_user}."
    exit 1
  fi
  # grep lines end with github_user and a leading space
  filenames=$(echo -n $(rg --type yaml " ${github_user}$" ${CLUSTERS_FOLDER} -l))
  if [[ -n $filenames ]] ; then
    echo $filenames | while read file; do
      gsed -i -e "s/${github_user}/${ldap_user}/g" $file
    done
  fi

done < ${MAPPING_FILE}