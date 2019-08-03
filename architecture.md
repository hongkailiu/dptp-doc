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

## [ci-tools](https://github.com/openshift/ci-tools)
## ci-operator
## build-cop
## ci-search