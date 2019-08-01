# [ci-tools](https://github.com/openshift/ci-tools)

Practice this `ci-tools` with [ci-secret-mirroring-controller](https://github.com/openshift/ci-secret-mirroring-controller):

* Enable `tide` for the repo: [release/pull/4601](https://github.com/openshift/release/pull/4601)
* Configure `OWNERS` of the repo: [ci-secret-mirroring-controller/pull/5](https://github.com/openshift/ci-secret-mirroring-controller/pull/5)
* Enable `approve`-plugin for the repo: [release/pull/4603](https://github.com/openshift/release/pull/4603)
* Follow [ONBOARD.md](https://github.com/openshift/ci-tools/blob/master/ONBOARD.md) to configure prowJobs for the repo: [release/pull/4583](https://github.com/openshift/release/pull/4583): `config` first, then [generate](https://github.com/openshift/ci-tools/blob/master/ONBOARD.md#add-prow-jobs) the jobs and `OWNERS` files.

Deprecated

* [ci-operator](https://github.com/openshift/ci-operator)
* [ci-operator-prowgen](https://github.com/openshift/ci-operator-prowgen)


