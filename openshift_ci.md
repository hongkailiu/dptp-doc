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

Deprecated

* [ci-operator](https://github.com/openshift/ci-operator)
* [ci-operator-prowgen](https://github.com/openshift/ci-operator-prowgen)