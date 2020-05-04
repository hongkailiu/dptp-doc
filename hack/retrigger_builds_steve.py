#!/usr/bin/env python
import json
builds = {}
# oc --context build01 get builds --namespace ci-op-n62ingvx -o json > /tmp/builds.json
with open("/tmp/builds.json") as raw:
	builds = json.load(raw)
for build in builds["items"]:
	build["metadata"]["annotations"].pop("openshift.io/build.pod-name")
	build["metadata"].pop("creationTimestamp")
	build["metadata"].pop("labels")
	build["metadata"].pop("resourceVersion")
	build["metadata"].pop("selfLink")
	build["metadata"].pop("uid")
	build["metadata"]["name"] = build["metadata"]["name"] + "-debug-1"
	build.pop("status")
	build["spec"]["output"]["to"]["name"] = build["spec"]["output"]["to"]["name"] + "-debug"
	build["spec"]["strategy"]["dockerStrategy"]["env"][0] = {"name":"BUILD_LOGLEVEL","value":"6"}
with open("/tmp/builds-debug.json", "w") as raw:
	json.dump(builds, raw)