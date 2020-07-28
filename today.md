
## Jul. 28

certs required? https://coreos.slack.com/archives/GB7NB0CUC/p1595946559490300

certs expired? https://coreos.slack.com/archives/CHY2E1BL4/p1595898486493000

Joseph: https://coreos.slack.com/archives/CBN38N3MW/p1595946690102900?thread_ts=1595870062.035900&cid=CBN38N3MW





## May 19

[Clayton's telemetry recording](https://coreos.slack.com/archives/GB7NB0CUC/p1589899863018700)

## May 14: aws training

* [Alert](https://coreos.slack.com/archives/CHY2E1BL4/p1589458825068200?thread_ts=1589443485.063900&cid=CHY2E1BL4) when upgrade is triggered.


## May 8: aws training

FYI, many have requested a link for an on-demand version of this course. This is not the same, but it covers some of the same ground. It is the "Cloud Practitioner Essentials" course which includes some of the business related details (pricing, costing) while this is more technical. Hopefully this helps those that need a little more time with the material. https://aws.amazon.com/training/course-descriptions/cloud-practitioner-essentials/

## May 7

* build02: design doc
* [aos-devel] machine API AWS spot instances support


## May 4

* [slack01](https://coreos.slack.com/archives/CHY2E1BL4/p1588269732276800) for [bz1830018](https://bugzilla.redhat.com/show_bug.cgi?id=1830018) and [slack01](https://coreos.slack.com/archives/GB7NB0CUC/p1588604917370000)




## May 1

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
