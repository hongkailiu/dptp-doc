# issues with migration

MEM issue on build: [bz1784163](https://bugzilla.redhat.com/show_bug.cgi?id=1784163): Workaround by removing MEM-limits on pod.

* pull-ci-openshift-origin-master-artifacts
* pull-ci-openshift-origin-master-images

Time issue on build: [bz1799674](https://bugzilla.redhat.com/show_bug.cgi?id=1799674): Fixed after upgrade to `4.3.0-0.nightly-2020-02-25-200400`.

* [pull-ci-openshift-windows-machine-config-bootstrapper-master-e2e-wsu](https://coreos.slack.com/archives/CBN38N3MW/p1581619969086000?thread_ts=1581619127.084500&cid=CBN38N3MW)

why cannot it be migrated to build01? Fixed by [pull/7186](https://github.com/openshift/release/pull/7186/files#diff-077d243d475d019fc8db8a0adece8f8f)


* pull-ci-openshift-kni-cnf-features-deploy-master-ci

`${HOME}` issue on build: [bz1804405](https://bugzilla.redhat.com/show_bug.cgi?id=1804405)

* pull-ci-openshift-knative-serving-release-next-4.3-e2e-aws-ocp-43 (Fixed in `4.3.0-0.nightly-2020-02-25-200400`)
* pull-ci-integr8ly-ansible-tower-configuration-master-e2e (email sent to the dev)

`${IMAGE_FORMAT}` issue in the test scripts. Steve sent out email.

`sidecar`: OOMKilled: [jira-comment](https://issues.redhat.com/browse/DPTP-684?focusedCommentId=13984185&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-13984185).

* NOT cmd: ci-operator but LITERAL $CONFIG_SPEC is used 

https://coreos.slack.com/archives/GB7NB0CUC/p1581705804023800

```
promote-release-openshift-machine-os-content-e2e-aws-4.2 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.2-s390x : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-old-rhcos-e2e-aws-4.2 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.2-stable-to-4.2-nightly : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.1-stable-to-4.2-ci : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.1-to-4.2 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.2 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-gcp-upgrade-4.2 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-azure-upgrade-4.2 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
endurance-upgrade-aws-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
endurance-e2e-aws-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
endurance-cluster-maintenance-aws-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.3-s390x : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.3-ppc64le : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-old-rhcos-e2e-aws-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-fips-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.2-to-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.2-nightly-to-4.3-nightly : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.2-to-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-gcp-upgrade-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-azure-upgrade-4.3 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.4 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.4-s390x : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.4-ppc64le : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-old-rhcos-e2e-aws-4.4 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-fips-4.4 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.3-stable-to-4.4-ci : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.3-nightly-to-4.4-nightly : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.3-to-4.4 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.4 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-gcp-upgrade-4.4 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-azure-upgrade-4.4 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.1 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.1-stable-to-4.1-nightly : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.1 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.6 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.6-s390x : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.6-ppc64le : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-old-rhcos-e2e-aws-4.6 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.5-stable-to-4.6-ci : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.5-to-4.6 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.6 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-gcp-upgrade-4.6 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-azure-upgrade-4.6 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.5 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.5-s390x : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
promote-release-openshift-machine-os-content-e2e-aws-4.5-ppc64le : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-old-rhcos-e2e-aws-4.5 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-4.4-stable-to-4.5-ci : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.4-to-4.5 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-aws-upgrade-rollback-4.5 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-gcp-upgrade-4.5 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
release-openshift-origin-installer-e2e-azure-upgrade-4.5 : job uses literal $CONFIG_SPEC but does not have ci-operator as the entrypoint, so it needs manual edits
```


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

Ask Clayton: https://coreos.slack.com/archives/GB7NB0CUC/p1581718975050100?thread_ts=1581633248.464700&cid=GB7NB0CUC

* promote-release-openshift-okd-machine-os-content-e2e-aws-4.{3|4|5|6}


* NOT cmd: ci-operator and NO $CONFIG_SPEC is used

NOTHING
