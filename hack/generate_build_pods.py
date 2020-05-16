#!/usr/bin/env python3

import logging
import yaml
import sys
import random
import string

#oc --context build01 get pods -n ci-op-vikrw48v -l openshift.io/build.name -o yaml > /tmp/pods.yaml
#oc --as system:admin --context build01 apply -f /tmp/pods-debug.yaml

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


with open('/tmp/pods.yaml') as f:
    pods = yaml.load(f, Loader=yaml.FullLoader)

name_suffix="-"+randomString()

for pod in pods["items"]:
    pod["metadata"]["annotations"].pop("openshift.io/build.name")
    pod["metadata"]["labels"].pop("openshift.io/build.name")
    pod["metadata"]["labels"]["dptp-debug"]="true"
    pod["metadata"].pop("ownerReferences")
    pod["metadata"].pop("creationTimestamp")
    pod["metadata"].pop("resourceVersion")
    pod["metadata"].pop("selfLink")
    pod["metadata"].pop("uid")
    pod["metadata"]["name"] = pod["metadata"]["name"] + name_suffix
    pod.pop("status")
    pod["spec"].pop("nodeName")
    pod["spec"]["nodeSelector"]={"node-role.kubernetes.io/debug":""}
    pod["spec"]["tolerations"]=[{"key":"dptp-debug","operator":"Equal","effect":"NoSchedule","value":"true"}]

with open("/tmp/pods-debug.yaml", 'w') as f:
    yaml.dump(pods, f)