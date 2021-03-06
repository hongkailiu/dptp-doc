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
    containers = []
    found = False
    boskos = False
    for container in job['spec']['containers']:
        if container['image'].endswith("ci-operator:latest"):
            found = True
            if 'args' not in container:
                logging.warning("no args for job %s", job["name"])
                containers.append(container)
                continue
            if container.get('command', []) != ["ci-operator"]:
                logging.warning("command not ci-operator in job %s", job["name"])
                containers.append(container)
                continue
            if "--resolver-address=http://ci-operator-configresolver" in container.get('args', []):
                container['args'].remove("--resolver-address=http://ci-operator-configresolver")
                container['args'].append("--resolver-address=http://ci-operator-configresolver-ci.svc.ci.openshift.org")
            if "--lease-server=http://boskos" in container.get('args', []):
                boskos = True
                container['args'].remove("--lease-server=http://boskos")
                container['args'].append("--lease-server-password-file=/etc/boskos/password")
                container['args'].append("--lease-server-username=ci")
                container['args'].append("--lease-server=https://boskos-ci.svc.ci.openshift.org")
                container['volumeMounts'].append({'mountPath': '/etc/boskos', 'name': 'boskos', 'readOnly': True})
            container['args'].append("--image-import-pull-secret=/etc/pull-secret/.dockerconfigjson")
            container['args'].append("--kubeconfig=/etc/apici/kubeconfig")
            container['args'] = sorted(container['args'])
            if not "volumeMounts" in container:
                 container['volumeMounts'] = []
            container['volumeMounts'].append({'mountPath': '/etc/apici', 'name': 'apici-ci-operator-credentials', 'readOnly': True})
            container['volumeMounts'].append({'mountPath': '/etc/pull-secret', 'name': 'pull-secret', 'readOnly': True})
            container['volumeMounts'] = sorted(container['volumeMounts'], key=lambda vm: vm['name'])
        else:
            logging.warning('ignoring appending args and volumes job %s whose image %s is not ci-operator:latest', job["name"], container['image'])
        containers.append(container)
    job['spec']['containers'] = containers
    if found:
        if not "volumes" in job['spec']:
            job['spec']['volumes'] = []
        job['spec']['volumes'].append({'name': 'apici-ci-operator-credentials', 'secret': {'items': [{'key': 'sa.ci-operator.apici.config', 'path': 'kubeconfig'}], 'secretName': 'apici-ci-operator-credentials'}})
        job['spec']['volumes'].append({'name': 'pull-secret', 'secret': {'secretName': 'regcred'}})
        if boskos:
            job['spec']['volumes'].append({'name': 'boskos', 'secret': {'items': [{'key': 'password', 'path': 'password'}], 'secretName': 'boskos-credentials'}})
        job['spec']['volumes'] = sorted(job['spec']['volumes'], key=lambda v: v['name'])
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