1. raid0 on m5d

verify raid0 is working:
a. io throughput on ec2 console on the NVMe devices.
b. system .mount is running
c. https://coreos.slack.com/archives/CHY2E1BL4/p1588274124302700?thread_ts=1588269732.276800&cid=CHY2E1BL4

```
as far as checking...I guess oc get -o yaml crd/machineconfigs.machineconfiguration.openshift.io | grep -c x-kubernetes-preserve-unknown-fields should be 3
```

2. doc on build01 and build02
https://coreos.slack.com/archives/GB7NB0CUC/p1588266713270500

a. failover
b. distribute evenly among available cluster
c. provider of e2e
