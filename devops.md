# DevOps

## CI cluster

CI-Cluster

Web console: https://api.ci.openshift.org/console/catalog

Authentication provider: github

[GCE console](https://console.cloud.google.com/home/dashboard?project=openshift-ci-infra&authuser=1&_ga=2.69769623.-621947859.1558447342): [VM instances](https://console.cloud.google.com/compute/instances?authuser=1&project=openshift-ci-infra&instancessize=50): 3 masters (n1-highmem-4 (4 vCPUs, 26 GB memory)) and 21 compute/infra (n1-standard-16 (16 vCPUs, 60 GB memory)) with auto-scale.

* Version
```
$ oc version
...
Server https://api.ci.openshift.org:443
openshift v3.11.0+e5dbec2-186
kubernetes v1.11.0+d4cacc0
```
* IPs

```
### show internal/external IPs of the nodes
$ oc get node -o wide
```

TOOD
installation: check [inventory](https://github.com/openshift/release/blob/master/cluster/test-deploy/api.ci/vars.yaml)

TODO
[autoscaler](k8s/autoscaling.md) setup.


## Tools

### oc

[some-prow-component-is-down-20190822](#some-prow-component-is-down-20190822) shows an example of using
`oc` to troubleshoot.

More oc-cli commands: [cmd.md](cmd.md)

### gcloud

run command on nodes: [Set up](cloud/gce/gce.md#google-cloud-cli) `gcloud-cli`.

```
$ gcloud config configurations list
NAME     IS_ACTIVE  ACCOUNT                   PROJECT             DEFAULT_ZONE  DEFAULT_REGION
default  True       <kerberos_id>@redhat.com  openshift-ci-infra  us-east1-c    us-east1

$ gcloud compute ssh "origin-ci-ig-n-t48j" --command "ls -al"
```

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

After changes on [populate-secrets-from-bitwarden.sh](https://github.com/openshift/release/blob/master/ci-operator/populate-secrets-from-bitwarden.sh) is merged, we need to manually run the script to apply the changes:

```
###install the bw-cli: https://help.bitwarden.com/article/cli/#download--install
$ bw login [email] [password]
###After successfully logging into the CLI a session key will be returned.
$ export BW_SESSION="<key>"

$ cd <path_to_github.com/openshift/release>
###install jq, oc (assume that oc-login is done)
$ ci-operator/populate-secrets-from-bitwarden.sh

$ bw logout
You have logged out.

```

## Troubleshooting

[Outage Postmortems](https://drive.google.com/drive/u/1/folders/1PcUkPa76udM4Fzy5NSX12zs9hrjwt4EQ)

### pod stuck with terminating

* Need to kill Pod

```
$ oc describe pod -n prow-monitoring prometheus-prow-0
  Warning  Unhealthy  11m                kubelet, origin-ci-ig-n-nmhz  Readiness probe failed: dial tcp 172.16.134.109:9091: connect: connection refused
  Normal   Killing    11m                kubelet, origin-ci-ig-n-nmhz  Killing container with id docker://prometheus-proxy:Need to kill Pod

### https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues/917
$ oc delete pod --force --grace-period 0 -n prow-monitoring prometheus-prow-0

$ oc get pod -n prow-monitoring prometheus-prow-0
NAME                READY     STATUS    RESTARTS   AGE
prometheus-prow-0   4/4       Running   1          4m

```

### restart master-controller: 20190822

```
$ for master in origin-ci-ig-m-428p origin-ci-ig-m-f3g1 origin-ci-ig-m-pbj3; do
    gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" "${master}" -- "/usr/local/bin/master-restart controllers"
done

```

### some prow component is down: 20190822

How steve responded to the alert: [tide and ghproxy down](https://coreos.slack.com/archives/CHY2E1BL4/p1566516725043200)

```
###https://coreos.slack.com/archives/CMA78N30T/p1566521000000200
$ oc project ci
### 1. `tide` is in `CrashLoopBackOff`
$ oc get pods --selector component=tide
NAME                    READY   STATUS    RESTARTS   AGE
tide-86db6f6958-dsrnm   1/1     CrashLoopBackOff   8          1h
tide-86db6f6958-nc455   1/1     Unknown   0          1d


$ oc describe pod tide-86db6f6958-dsrnm
...
 origin-ci-ig-n-g68v  Back-off restarting failed container
###2. `tide` cannot reach `ghproxy`
$ oc logs tide-86db6f6958-dsrnm
...
{"component":"tide","error":"error getting bot name: fetching bot name from GitHub: Get http://ghproxy/user: dial tcp 172.30.199.140:80: connect: no route to host","file":"prow/cmd/tide/main.go:158","func":"main.main","level":"fatal","msg":"Error getting Git client.","time":"2019-08-23T00:40:21Z"}

###3. `ghproxy` has `Unknown` `Pods`
$ oc get pods --selector component=ghproxy
NAME                                    READY   STATUS              RESTARTS   AGE
ghproxy-f9bbcc785-d29v4                 0/1     ContainerCreating   0          1h
ghproxy-f9bbcc785-r4lwz                 1/1     Unknown             0          1d

###4. `ghproxy` `Pod` is in `Unknown` due to losing the node:
$ oc describe pod ghproxy-f9bbcc785-r4lwz
Status:                    Terminating (lasts <invalid>)
Termination Grace Period:  30s
Reason:                    NodeLost
Message:                   Node origin-ci-ig-n-d4fs which was running pod ghproxy-f9bbcc785-r4lwz is unresponsive

###5. Node has the following events:
$ oc describe node origin-ci-ig-n-d4fs
  Resource           Requests       Limits
  --------           --------       ------
  cpu                11660m (75%)   3220m (20%)
  memory             28228Mi (48%)  20496Mi (35%)
  ephemeral-storage  0 (0%)         0 (0%)
Events:
  Type     Reason             Age                 From                          Message
  ----     ------             ----                ----                          -------
  Normal   NodeNotReady       89m                 kubelet, origin-ci-ig-n-d4fs  Node origin-ci-ig-n-d4fs status is now: NodeNotReady
  Warning  ContainerGCFailed  26m (x65 over 91m)  kubelet, origin-ci-ig-n-d4fs  rpc error: code = ResourceExhausted desc = grpc: trying to send message larger than max (8392271 vs. 8388608)
  Warning  ImageGCFailed      86s (x6 over 41m)   kubelet, origin-ci-ig-n-d4fs  rpc error: code = ResourceExhausted desc = grpc: trying to send message larger than max (8392271 vs. 8388608)

###Resolution -- going to cordon the node
$ oc adm cordon origin-ci-ig-n-d4fs --as system:admin
node/origin-ci-ig-n-d4fs cordoned

###All pods that use PV and have something in Unkown status cannot release the PVC, so new Pods cannot come up 
$ oc adm drain origin-ci-ig-n-d4fs --delete-local-data --force --ignore-daemonsets --as system:admin --loglevel 4

###fetch journals on the node
$ gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" origin-ci-ig-n-d4fs -- "sudo journalctl --all --lines all --no-pager --unit origin-node.service --since '24 hours ago'" > /tmp/origin-ci-ig-n-d4fs.txt
$ gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" origin-ci-ig-n-d4fs -- "sudo journalctl --all --lines all --no-pager --unit docker.service --since '24 hours ago'" > /tmp/origin-ci-ig-n-d4fs-docker.txt


###nuke the pods
###https://kubernetes.io/docs/reference/kubectl/jsonpath/
$ oc get pods --all-namespaces -o "jsonpath={range .items[?(@.spec.nodeName==\"origin-ci-ig-n-d4fs\")]}{\"oc delete --force --grace-period 0 pod \"}{.metadata.name}{\" --namespace \"}{.metadata.namespace}{\"\\n\"}{end}"
###not that start version but easy to understand
$ oc get pod --all-namespaces -o wide --no-headers |  awk '{ if ($8 == "origin-ci-ig-n-0rlt") { print $1, $2} }' | xargs -l oc get pod -o wide -n

###find PVs attached to an instance
$ gcloud compute disks list  --filter="users:(origin-ci-ig-n-0rlt)"
###also visible on the UI: https://console.cloud.google.com/compute/instancesDetail/zones/us-east1-c/instances/origin-ci-ig-n-0rlt?authuser=1&project=openshift-ci-infra
$ gcloud compute instances describe origin-ci-ig-n-0rlt --format json | jq -r '.disks[].deviceName'
origin-ci-instance-template-node-large-disk

###detach a disk from an instance: https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk

```

TO ask Steve:  i forgot to take it out of the node pool
