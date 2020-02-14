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
        correctCommand = container.get("command", []) == ["ci-operator"]
        for e, env in enumerate(container.get("env", [])):
            if env.get("name", "") == "CONFIG_SPEC" and "valueFrom" not in env:
                if not correctCommand:
                    print(job["name"], ": job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits")
                    return job
                config = yaml.load(env.get("value", ""), Loader=yaml.FullLoader)
                if "build_root" in config and "image_stream_tag" in config["build_root"]:
                    config["build_root"]["image_stream_tag"]["cluster"] = "https://api.ci.openshift.org"
                if "tag_specification" in config:
                    config["tag_specification"]["cluster"] = "https://api.ci.openshift.org"
                for image in config.get("base_images", {}):
                    config["base_images"][image]["cluster"] = "https://api.ci.openshift.org"
                env["value"] = yaml.dump(config)
                job["spec"]["containers"][c]["env"][e] = env
                edited = True
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