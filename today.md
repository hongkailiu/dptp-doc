1. raid0 on m5d

verify raid0 is working:

* io throughput on ec2 console on the NVMe devices.
* system .mount is running
* https://coreos.slack.com/archives/CHY2E1BL4/p1588274124302700?thread_ts=1588269732.276800&cid=CHY2E1BL4

```
as far as checking...I guess oc get -o yaml crd/machineconfigs.machineconfiguration.openshift.io | grep -c x-kubernetes-preserve-unknown-fields should be 3
```

2. doc on build01 and build02
https://coreos.slack.com/archives/GB7NB0CUC/p1588266713270500

* failover
* distribute evenly among available cluster
* provider of e2e

3. [bz](https://bugzilla.redhat.com/show_bug.cgi?id=1828065#c16) and [samples-operator](https://docs.openshift.com/container-platform/4.1/openshift_images/configuring-samples-operator.html)
