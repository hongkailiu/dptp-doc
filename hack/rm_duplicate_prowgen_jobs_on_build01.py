#!/usr/bin/env python3

### handle the non-prowgen jobs at migration
### example to run the command:
### release_repo=/path_to_release_repo bash -c 'find ${release_repo}  -name "*openshift-origin-master-presubmits.yaml" -exec python3 hack/duplicate_prowgen_jobs_on_build01.py {} \;'

import copy
import logging
from ruamel.yaml import YAML
from  ruamel.yaml.scalarstring import DoubleQuotedScalarString
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
                if job["name"].endswith("-migrated") and "labels" in job and not "ci-operator.openshift.io/prowgen-controlled" in job["labels"]:
                    continue
                jobs.append(job)
            all[t][repo] = jobs

with open(sys.argv[1], 'w') as f:
    yaml.dump(all, f)
