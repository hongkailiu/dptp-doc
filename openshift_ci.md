# OpenShift CI

## Prowjobs

* [prow plugins](https://deck-ci.svc.ci.openshift.org/plugins) and its [configurations](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/plugins.yaml): eg, [approve](https://github.com/kubernetes/test-infra/blob/master/prow/plugins/approve/approvers/README.md).
* prowJobs: [definitions](https://github.com/openshift/release/tree/master/ci-operator/jobs)
* [image-mirror setup requests](https://coreos.slack.com/archives/GB7NB0CUC/p1558533720293300)


## [ci-tools](https://github.com/openshift/ci-tools)

Practice this `ci-tools` with [ci-secret-mirroring-controller](https://github.com/openshift/ci-secret-mirroring-controller):

* Enable `tide` for the repo: [release/pull/4601](https://github.com/openshift/release/pull/4601)
* Configure `OWNERS` of the repo: [ci-secret-mirroring-controller/pull/5](https://github.com/openshift/ci-secret-mirroring-controller/pull/5)
* Enable `approve`-plugin for the repo: [release/pull/4603](https://github.com/openshift/release/pull/4603)
* Follow [ONBOARD.md](https://github.com/openshift/ci-tools/blob/master/ONBOARD.md) to configure prowJobs for the repo: [release/pull/4583](https://github.com/openshift/release/pull/4583): `config` first, then [generate](https://github.com/openshift/ci-tools/blob/master/ONBOARD.md#add-prow-jobs) the jobs and `OWNERS` files.

```
$ JOB_SPEC='{"type":"periodic","job":"periodic-ci-azure-e2e-applysecurityupdates","buildid":"21","prowjobid":"ec28bec2-b7a4-11e9-af8e-0a58ac108dbc","extra_refs":[{"org":"openshift","repo":"openshift-azure","base_ref":"master"}]}' ./ci-operator --config /home/hongkliu/go/src/github.com/openshift/release/ci-operator/config/openshift/ci-secret-mirroring-controller/openshift-ci-secret-mirroring-controller-master.yaml --git-ref openshift/ci-secret-mirroring-controller@master --dry-run

```

Deprecated

* [ci-operator](https://github.com/openshift/ci-operator)
* [ci-operator-prowgen](https://github.com/openshift/ci-operator-prowgen)