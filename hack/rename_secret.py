#!/usr/bin/env python3
import logging
import yaml
import sys


filename = sys.argv[1]

edited = False
def update(job):
    global edited
    if "spec" not in job:
        return job
    for c, container in enumerate(job["spec"].get("containers", [])):
        for e, vm in enumerate(container.get("volumeMounts", [])):
            if vm.get("name", "") == "pull-secret":
                job["spec"]["containers"][c]["volumeMounts"][e]["name"] = "release-pull-secret"
                edited = True
    for v, volume in enumerate(job["spec"].get("volumes", [])):
        if volume.get("name", "") == "pull-secret":
                job["spec"]["volumes"][v]["name"] = "release-pull-secret"
    return job


with open(filename) as f:
    edited = False
    all = yaml.load(f, Loader=yaml.FullLoader)
    for t in ("presubmits", "postsubmits"):
        for repo in all.get(t, {}):
            all[t][repo] = [update(job) for job in all[t][repo]]
    if "periodics" in filename:
        all["periodics"] = [update(job) for job in all["periodics"]]
if edited:
    with open(sys.argv[1], 'w') as f:
        yaml.dump(all, f)
