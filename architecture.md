# dpcp architecture

## prow

Prowjobs:

* [prow plugins](https://deck-ci.svc.ci.openshift.org/plugins) and its [configurations](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/plugins.yaml): eg, [approve](https://github.com/kubernetes/test-infra/blob/master/prow/plugins/approve/approvers/README.md).
* prowJobs: [definitions](https://github.com/openshift/release/tree/master/ci-operator/jobs)
* [image-mirror setup requests](https://coreos.slack.com/archives/GB7NB0CUC/p1558533720293300)

### deck
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

```
$ oc get deploy -n ci ghproxy
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
ghproxy   1         1         1            1           218d

```

[Q&A@slack](https://coreos.slack.com/archives/GB7NB0CUC/p1562767143290700).

## [ci-tools](https://github.com/openshift/ci-tools)
## ci-operator
## build-cop
## ci-search