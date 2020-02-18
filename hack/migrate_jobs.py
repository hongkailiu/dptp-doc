#!/usr/bin/env python3

### handle the non-prowgen jobs at migration
### example to run the command:
### release_repo=/path_to_release_repo bash -c 'find ${release_repo}  -name "*openshift-origin-master-presubmits.yaml" -exec python3 hack/migrate_non_prowgen_jobs.py {} \;'

import logging
import yaml
import sys

filename = sys.argv[1]

def migrate(job):
    if "cluster" in job:
        logging.warning("the cluster of job '%s' has been defined: '%s'", job["name"], job["cluster"])
        return job
    if job.get("agent", "") != "kubernetes":
        logging.warning("the agent '%s' of job '%s' is not 'kubernetes'", job.get("agent", ""), job["name"])
        return job
    job["cluster"]="ci/api-build01-ci-devcluster-openshift-com:6443"
    return job

with open(filename) as f:
    all = yaml.load(f, Loader=yaml.FullLoader)
    for t in ("presubmits", "postsubmits"):
        if t not in filename:
            continue
        for repo in all[t]:
            jobs = []
            for job in all[t][repo]:
                if not "labels" in job or not "ci-operator.openshift.io/prowgen-controlled" in job["labels"] or job["labels"]["ci-operator.openshift.io/prowgen-controlled"] != "true":
                    logging.info('job is not controlled by prowgen: %s', job["name"])
                    jobs.append(migrate(job))
                else:
                    jobs.append(job)
            all[t][repo] = jobs
    if "periodics" in filename:
        jobs = []
        for job in all["periodics"]:
            if not "labels" in job or not "ci-operator.openshift.io/prowgen-controlled" in job["labels"] or job["labels"]["ci-operator.openshift.io/prowgen-controlled"] != "true":
                logging.info('job is not controlled by prowgen: %s', job["name"])
                jobs.append(migrate(job))
            else:
                jobs.append(job)
        all["periodics"] = jobs

with open(sys.argv[1], 'w') as f:
    yaml.dump(all, f)