#!/usr/bin/env python3
"""This script ensures the cluster of prowjobs is defined as expected.
e.g., python ./hack/ensure_job_cluster.py
"""

import argparse
import logging
import os
import yaml


def ensure(job_dir):
    jobs = []
    for dirpath, _, filenames in os.walk(job_dir):
        for filename in filenames:
            if filename.endswith('.yaml'):
                file_path = os.path.join(dirpath, filename)
                if 'ci-operator/jobs/openshift-priv/' in file_path:
                    continue
                logging.info("handling file %s", file_path)
                with open(file_path) as file:
                    data = yaml.safe_load(file)
                    for job_type in ["presubmits"]:
                        for repo in data.get(job_type, {}):
                            jobs.extend([j['name'] for j in data[job_type][repo] if j.get("agent", "") != "kubernetes" or not "labels" in j or not "ci-operator.openshift.io/prowgen-controlled" in j["labels"] or j["labels"]["ci-operator.openshift.io/prowgen-controlled"] != "true"])
    with open("/Users/hongkliu/Downloads/non_prowgen_jobs.yaml", 'w') as file:
        yaml.dump(jobs, file)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )


def main():
    """main function."""
    logging.info("checking jobs ...")
    parser = argparse.ArgumentParser(description='Ensure prow jobs\' cluster.')
    parser.add_argument('-d', '--job-dir', default='./ci-operator/jobs',
                        help="the path to the job directory")
    args = parser.parse_args()
    ensure(args.job_dir)



if __name__ == "__main__":
    main()