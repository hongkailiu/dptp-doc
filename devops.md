# DevOps

[DPTP Operational Role Signup](https://docs.google.com/spreadsheets/u/1/d/1vfFt_MLg-eFTg6iEMG-ZIw6yiGr7LjvmJXj-LYKvrVM/edit?ouid=117551473102555683702&usp=sheets_home&ths=true), 
[DPTP Operational Duties](https://docs.google.com/document/d/11Ao_as9Pi2WLIffwn6Xh1XO_857Xra1liAwEVjrGtg8/edit#heading=h.yms7sbq3ypl4),
[DPTP Triage Summary](https://docs.google.com/document/d/1xWUtEWuud39zs2RrX9WqV6daF5Be31SmpagsIKeL_HU/edit)

## CI cluster

[CI-Cluster](https://github.com/openshift/release/tree/master/clusters): [deployment](https://github.com/hongkailiu/dptp-doc/blob/master/architecture.md#prow-deployment).

[GCE console](https://console.cloud.google.com/home/dashboard?project=openshift-ci-infra&authuser=1&_ga=2.69769623.-621947859.1558447342): [VM instances](https://console.cloud.google.com/compute/instances?authuser=1&project=openshift-ci-infra&instancessize=50): 3 masters (n1-highmem-4 (4 vCPUs, 26 GB memory)) and 21 compute/infra (n1-standard-16 (16 vCPUs, 60 GB memory)) with [cluster autoscaler](k8s/autoscaling.md).

api.ci installation: check [inventory](https://github.com/openshift/release/blob/master/cluster/test-deploy/api.ci/vars.yaml)

TODO
[autoscaler](k8s/autoscaling.md) setup: ci cluster is 311 openshift cluster on gce. Does k8s-autoscaler just work on it? But no doc says how. See also [autoscaler/issues/638](https://github.com/kubernetes/autoscaler/issues/638). Releated to [kubernetes-node-pool](https://kubernetes.io/docs/tasks/administer-cluster/cluster-management/#resizing-a-cluster)? See [instance groups at GCE console](https://console.cloud.google.com/compute/instanceGroups/list?authuser=1&organizationId=54643501348&project=openshift-ci-infra&instanceGroupsTablesize=50).


## Tools

### oc

### gcloud

run command on nodes: [Set up](cloud/gce/gce.md#google-cloud-cli) `gcloud-cli`.

```
$ gcloud config configurations list
NAME     IS_ACTIVE  ACCOUNT                   PROJECT             DEFAULT_ZONE  DEFAULT_REGION
default  True       <kerberos_id>@redhat.com  openshift-ci-infra  us-east1-c    us-east1

```


### stackdriver: logs viewer

[stackdriver](https://console.cloud.google.com/logs/viewer?authuser=1&organizationId=54643501348&project=openshift-ci-infra)

Track a PR comment, e.g., [619604386](https://github.com/openshift/release/pull/8539#issuecomment-619604386):

```text
resource.type="gce_instance"
jsonPayload.repo="release"
jsonPayload.pr: "8539" 
619604386
```

Then in the above query, replace `619604386` with `jsonPayload."event-GUID"="7863e400-87ee-11ea-885c-f000c395f32d"` in the log of `hook Issue comment created.`

### aws

The aws-tests run on clusters created on aws. [Set up](cloud/ec2/ec2.md#configure) `aws-cli` with the env. vars.

```
### or modify and run to set up
$ dptp-secret/aws-cli/active_aws_ci.sh
### logout
$ dptp-secret/aws-cli/active_aws_ci_unset.sh

```

TODO: How ci-opeator tells aws to create cluster to run e2e tests with?

### bitwarden

TODO: account setup and get access to existing item-collection (@James Russell)

```
###install the bw-cli: https://help.bitwarden.com/article/cli/#download--install
$ bw login [email] [password]
###After successfully logging into the CLI a session key will be returned.
$ export BW_SESSION="<key>"

$ bw logout
You have logged out.

```

### prometheus

```
### ben
container_memory_rss
### steve
max(max_over_time(container_memory_max_usage_bytes{pod_name="artifacts-build"}[3w])) by (container_name)
```

TODO: 

CPU and MEM from k8s-prometheus: [slack](https://coreos.slack.com/archives/CBN38N3MW/p1568146226424800)

autoscaler: node limit? [slack](https://coreos.slack.com/archives/CBN38N3MW/p1568150695436400)

master not responsive: [query](https://prometheus-k8s-openshift-monitoring.svc.ci.openshift.org/graph?g0.range_input=2h&g0.expr=container_memory_usage_bytes%7Bnamespace%3D%22kube-system%22%2Ccontainer_name%3D%22%22%7D&g0.tab=0)


## Troubleshooting

[Outage Postmortems](https://drive.google.com/drive/u/1/folders/1PcUkPa76udM4Fzy5NSX12zs9hrjwt4EQ)

### remove a node from cluster

Michael Gugino: [Never delete a node from an OCP4 cluster](https://coreos.slack.com/archives/CHY2E1BL4/p1586353553317700?thread_ts=1586337299.306200&cid=CHY2E1BL4)

* In the future, delete the machine-object first, always.  
* Then, apply [the annotation](https://github.com/openshift/machine-api-operator/pull/534/files#diff-e6f81a9d8df4fb4d787121a242ea6bf1R46) after some time if drain is not completing (if drain is not completing, it's usually due to some kind of bug, so always report that case)
  > machine.openshift.io/exclude-node-draining
* (unless the drain is blocked by PDBs, which is not a bug, and is expected behavior)


### nodes with registry pods are with high CPU load
https://coreos.slack.com/archives/CBN38N3MW/p1579552231109600?thread_ts=1579541532.082600&cid=CBN38N3MW


### batch rerun on PRs
https://coreos.slack.com/archives/GB7NB0CUC/p1580408531244100?thread_ts=1580408292.241600&cid=GB7NB0CUC

```
    - args:
      - |-
        --query=is:pr
        state:open
        state:failing
        repo:openshift/release
      - --token=/etc/oauth/oauth
      - --updated=0
      - |-
        --comment=/test all
```

Then `make job JOB=periodic-bugzilla-refresh`: It will create [prowjob](https://prow.svc.ci.openshift.org/prowjob?prowjob=73366ce8-5a58-11ea-97a0-96f07a6c9342) in `current` project.

### Resize master VMs
https://coreos.slack.com/archives/CTTNY7TN1

Resize on the GCE UI: Stop, Edit, Save, Start.

```
[root@origin-ci-ig-m-428p ~]# while true; do ETCDCTL_API=3 etcdctl --cert=/etc/origin/master/master.etcd-client.crt --key=/etc/origin/master/master.etcd-client.key --cacert=/etc/origin/master/master.etcd-ca.crt --endpoints="10.142.0.4:2379,10.142.0.2:2379,10.142.0.3:2379" endpoint health; sleep 10; clear; done
```

### Which container OOMKilled

```bash
oc get pod -n ci --context build01 | grep -v Running | grep -v Completed | grep -v Terminating | grep -v "Init:"
NAME                                     READY   STATUS        RESTARTS   AGE
namespace-ttl-controller-691-deploy      0/1     OOMKilled     0          46m

oc get pod -n ci --context build01 -o yaml | yq -c '.items[].status.containerStatuses[] | [.name, .state.terminated.reason]' | grep OOMKilled

oc get pod -n ci --context build01 -o yaml | yq -c '.items[].status.containerStatuses[] | [.name, .state.terminated.reason]' | sort | uniq -c | sort -nr
```

### image url

http://post-office.corp.redhat.com/archives/aos-devel/2020-February/msg00301.html

https://coreos.slack.com/archives/CBN38N3MW/p1585833281055400?thread_ts=1585650114.342500&cid=CBN38N3MW

and it should be 

> IMAGE_TOOLCHAIN_OPERATOR=${IMAGE_TOOLCHAIN_OPERATOR} make test-e2e


### Alerts handling

#### openshift-monitoring

[KubeCPUOvercommit (openshift-monitoring/k8s warning)](https://coreos.slack.com/archives/CV1UZU53R/p1584001711053000)

#### prow-monitoring

* Running out token:
[sort github queries by that token by path and see what's taking up](https://coreos.slack.com/archives/CHY2E1BL4/p1580412051028300), e.g., [this query](https://prometheus-prow-monitoring.svc.ci.openshift.org/graph?g0.range_input=1h&g0.expr=github_token_usage&g0.tab=1&g1.range_input=1h&g1.expr=sum(github_request_duration_count%7Btoken_hash%3D%2235411b2f9833b04c964c7a70640354e5a22a8942682c4fb6c9cc80e4c83a7bfe%22%7D)%20by%20(path)&g1.tab=1)

