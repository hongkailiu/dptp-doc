# dpcp architecture

[elder's diagram](https://elder.dev/posts/prow/)

## prow

### deck

histogram on the UI: [Petr@slack](https://coreos.slack.com/archives/GB7NB0CUC/p1558533700292600).

### hook

`hook` receives [events](https://developer.github.com/webhooks/) from `github`.

```
$ oc get deploy -n ci hook
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
hook      2         2         2            2           216d
```

### plank
### sinker
### tide

`tide` operates `github`'s PRs.

```
$ oc get deploy -n ci tide
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
tide      1         1         1            1           217d
```

### [ghproxy](https://github.com/kubernetes/test-infra/tree/master/ghproxy)

We use `ghproxy` to avoid [rate-limiting of api tokens](https://developer.github.com/v3/#rate-limiting).

```
$ oc get deploy -n ci ghproxy
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
ghproxy   1         1         1            1           218d

```

[Q&A@slack](https://coreos.slack.com/archives/GB7NB0CUC/p1562767143290700).

Check `--github-endpoint` flag in the production to see which components use `ghproxy`. It should be _all of them_.

## OpenShift CI

### Prow

All prow components and prowjobs [are running in namespace](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/config.yaml#L618-L619) `ci`.

* [configuration](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/config.yaml) for prow-components: 
    > oc get configmaps -n ci config
* [prow plugins](https://deck-ci.svc.ci.openshift.org/plugins) and its [configurations](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/plugins.yaml): eg, [approve](https://github.com/kubernetes/test-infra/blob/master/prow/plugins/approve/approvers/README.md):
    > oc get configmaps -n ci plugins

### [ci-tools](https://github.com/openshift/ci-tools)

> Steve: flow of information is prow --> prowjob pod (running ci-operator) --> job pod (created by ci-operator, runs tests)

[ci-operator readme on release repo](https://github.com/openshift/release/tree/master/ci-operator).

Prowjobs' resources:

* namespaces

* config

Practice this `ci-tools` with [ci-secret-mirroring-controller](https://github.com/openshift/ci-secret-mirroring-controller):

* Enable `tide` for the repo: [release/pull/4601](https://github.com/openshift/release/pull/4601)
* Configure `OWNERS` of the repo: [ci-secret-mirroring-controller/pull/5](https://github.com/openshift/ci-secret-mirroring-controller/pull/5)
* Enable `approve`-plugin for the repo: [release/pull/4603](https://github.com/openshift/release/pull/4603)
* Follow [ONBOARD.md](https://github.com/openshift/ci-tools/blob/master/ONBOARD.md) to configure prowJobs for the repo: [release/pull/4583](https://github.com/openshift/release/pull/4583): `config` first, then [generate](https://github.com/openshift/ci-tools/blob/master/ONBOARD.md#add-prow-jobs) the jobs and `OWNERS` files.

```
$ JOB_SPEC='{"type":"periodic","job":"periodic-ci-azure-e2e-applysecurityupdates","buildid":"21","prowjobid":"ec28bec2-b7a4-11e9-af8e-0a58ac108dbc","extra_refs":[{"org":"openshift","repo":"openshift-azure","base_ref":"master"}]}' ./ci-operator --config /home/hongkliu/go/src/github.com/openshift/release/ci-operator/config/openshift/ci-secret-mirroring-controller/openshift-ci-secret-mirroring-controller-master.yaml --git-ref openshift/ci-secret-mirroring-controller@master --dry-run

```



### [ci-tools](https://github.com/openshift/ci-tools)

### build-cop

### ci-search

### others

* [image-mirror setup requests](https://coreos.slack.com/archives/GB7NB0CUC/p1558533720293300)

Deprecated

* [ci-operator](https://github.com/openshift/ci-operator)
* [ci-operator-prowgen](https://github.com/openshift/ci-operator-prowgen)