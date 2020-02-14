# issues with migration

[MEM issue on build](https://bugzilla.redhat.com/show_bug.cgi?id=1784163)

* pull-ci-openshift-origin-master-artifacts
* pull-ci-openshift-origin-master-images

* pull-ci-openshift-windows-machine-config-bootstrapper-master-e2e-wsu

https://coreos.slack.com/archives/CBN38N3MW/p1581619969086000?thread_ts=1581619127.084500&cid=CBN38N3MW

why cannot it be migrated to build01?

* NOT cmd: ci-operator but LITERAL $CONFIG_SPEC is used 

https://coreos.slack.com/archives/GB7NB0CUC/p1581705804023800


* NOT cmd: ci-operator but $CONFIG_SPEC and value from is used 

https://coreos.slack.com/archives/GB7NB0CUC/p1581711444042400?thread_ts=1581633248.464700&cid=GB7NB0CUC

```
pull-ci-kubernetes-descheduler-e2e-gce-3.10 : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
pull-ci-origin-web-console-server-e2e-3.10 : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-okd-machine-os-content-e2e-aws-4.6 : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-okd-machine-os-content-e2e-aws-4.4 : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-okd-machine-os-content-e2e-aws-4.3 : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-okd-machine-os-content-e2e-aws-4.5 : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
pull-ci-image-registry-e2e-3.10 : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
pull-ci-openshift-openshift-ansible-310-gcp-major-upgrade : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
pull-ci-openshift-openshift-ansible-e2e-gcp-310 : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
pull-ci-openshift-openshift-ansible-release-3.10-e2e-atomic : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
pull-ci-openshift-openshift-ansible-release-3.10-e2e-aws : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
pull-ci-openshift-openshift-ansible-release-3.10-e2e-gluster : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
pull-ci-openshift-openshift-ansible-3.11-gcp-major-upgrade : job has valueFrom for $CONFIG_SPEC and does not have ci-operator as the entrypoint, so it needs manual edits
```

* NOT cmd: ci-operator and NO $CONFIG_SPEC is used

NOTHING