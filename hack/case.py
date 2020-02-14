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
        correctImage = container.get("image", "") == "ci-operator:latest"
        if not correctImage:
            continue
        correctCommand = container.get("command", []) == ["ci-operator"]
        if correctCommand:
            continue
        found_config_spec = False
        for e, env in enumerate(container.get("env", [])):
            if env.get("name", "") == "CONFIG_SPEC":
                found_config_spec = True
        if not found_config_spec:
            print(job["name"], ": job has not $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits")
    return job
with open(filename) as f:
    all = yaml.load(f, Loader=yaml.FullLoader)
    for t in ("presubmits", "postsubmits"):
        for repo in all.get(t, {}):
            all[t][repo] = [update(job) for job in all[t][repo]]
    if "periodics" in filename:
        all["periodics"] = [update(job) for job in all["periodics"]]
if edited:
    with open(sys.argv[1], 'w') as f:
        yaml.dump(all, f)