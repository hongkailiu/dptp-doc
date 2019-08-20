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