# DevOps

## CI cluster

CI-Cluster

Web console: https://api.ci.openshift.org/console/catalog

Authentication provider: github

[GCE console](https://console.cloud.google.com/home/dashboard?project=openshift-ci-infra&authuser=1&_ga=2.69769623.-621947859.1558447342): [VM instances](https://console.cloud.google.com/compute/instances?authuser=1&project=openshift-ci-infra&instancessize=50): 3 masters (n1-highmem-4 (4 vCPUs, 26 GB memory)) and 21 compute/infra (n1-standard-16 (16 vCPUs, 60 GB memory)) with auto-scale:

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

## Tools

### oc

### run command on nodes
$ gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" "origin-ci-ig-n-t48j" --command "ls -al"

### gcloud

[gcloud init](cloud/gce/gce.md)

```
$ gcloud config configurations list
NAME     IS_ACTIVE  ACCOUNT              PROJECT             DEFAULT_ZONE  DEFAULT_REGION
default  True       hongkliu@redhat.com  openshift-ci-infra

$ gcloud config configurations list

### change project: https://stackoverflow.com/questions/46770900/how-to-change-the-project-in-gcp-using-cli-commands
$ gcloud config set project `PROJECT ID`
```

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
$
```

### some prow component is down: 20190822

How steve responded to the alert: [tide and ghproxy down](https://coreos.slack.com/archives/CHY2E1BL4/p1566516725043200)