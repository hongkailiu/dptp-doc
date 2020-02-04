#!/usr/bin/env python3

### handle the non-prowgen jobs at migration
### example to run the command:
### release_repo=/path_to_release_repo bash -c 'find ${release_repo}  -name "*openshift-origin-master-presubmits.yaml" -exec python3 hack/duplicate_prowgen_jobs_on_build01.py {} \;'

import copy
import logging
from ruamel.yaml import YAML
import sys

filename = sys.argv[1]

yaml = YAML()
yaml.compact(seq_seq=False)
yaml.preserve_quotes = True

with open(filename) as f:
    all = yaml.load(f)
    for t in ("presubmits", "postsubmits", "periodics"):
        if t not in filename:
            continue
        for repo in all[t]:
            jobs = []
            for job in all[t][repo]:
                jobs.append(job)
                if "labels" in job and "ci-operator.openshift.io/prowgen-controlled" in job["labels"] and job["labels"]["ci-operator.openshift.io/prowgen-controlled"] == "true":
                    build01_job = copy.deepcopy(job)
                    build01_job["name"] += "-migrated"
                    build01_job['cluster'] = 'ci/api-build01-ci-devcluster-openshift-com:6443'
                    build01_job["labels"]["ci-operator.openshift.io/prowgen-controlled"] = "false"
                    #build01_job["labels"]["ci-operator.openshift.io/semantics-ignored"] = "true"
                    build01_job['optional'] = True
                    build01_job['skip_report'] = True
                    jobs.append(build01_job)
            #jobs = sorted(jobs, key=lambda job: job['name'])
            all[t][repo] = jobs

with open(sys.argv[1], 'w') as f:
    yaml.dump(all, f)
