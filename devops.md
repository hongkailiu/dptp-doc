# DevOps

## pod stuck with terminating

### Need to kill Pod

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
## bitwarden

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

```
