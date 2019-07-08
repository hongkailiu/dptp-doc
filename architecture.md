# dpcp architecture

## prow

Prowjobs:

* [prow plugins](https://deck-ci.svc.ci.openshift.org/plugins) and its [configurations](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/plugins.yaml): eg, [approve](https://github.com/kubernetes/test-infra/blob/master/prow/plugins/approve/approvers/README.md).
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


## ci-operator
## build-cop
## ci-search