# dpcp architecture

[test-infra](https://github.com/kubernetes/test-infra); [elder's diagram](https://elder.dev/posts/prow/)

## [prow](https://github.com/kubernetes/test-infra/tree/master/prow)

Upstream cluster: [config.yaml](https://github.com/kubernetes/test-infra/blob/master/prow/config.yaml); [plugin.yaml](https://github.com/kubernetes/test-infra/blob/master/prow/plugins.yaml); [job config folder](https://github.com/kubernetes/test-infra/tree/master/config/jobs)

### deck

histogram on the UI: [Petr@slack](https://coreos.slack.com/archives/GB7NB0CUC/p1558533700292600).

### hook

`hook` receives [events](https://developer.github.com/webhooks/) from `github`.

```
$ oc get deploy -n ci hook
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
hook      2         2         2            2           216d
```

[plugins](https://github.com/kubernetes/test-infra/tree/master/prow/plugins)

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

[Q&A@slack](https://coreos.slack.com/archives/GB7NB0CUC/p1562767143290700) and [proxy lawyers in ghproxy](https://coreos.slack.com/archives/GB7NB0CUC/p1565793345353000).

Check `--github-endpoint` flag in the production to see which components use `ghproxy`. It should be _all of them_.

Understanding ghproxy: Steve: we have [the following layers](https://github.com/kubernetes/test-infra/blob/af1a26bf30f5f3776dba3b171899f400d3fe22ad/ghproxy/ghcache/ghcache.go#L205-L216):

> request --> http cache --> output throttle --> request coaleser --> github

In our production, [deployment](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/openshift/ghproxy.yaml#L59) indicates we use
[`NewDiskCache`](https://github.com/kubernetes/test-infra/blob/master/ghproxy/ghproxy.go#L135-L142).
So we cache the requests by [`diskcache.NewWithDiskv`](https://github.com/kubernetes/test-infra/blob/af1a26bf30f5f3776dba3b171899f400d3fe22ad/ghproxy/ghcache/ghcache.go#L205-L216).

So let us start with [`cacheTransport := httpcache.NewTransport(cache)`](https://github.com/kubernetes/test-infra/blob/af1a26bf30f5f3776dba3b171899f400d3fe22ad/ghproxy/ghcache/ghcache.go#L227)
which returns a [`httpcache.Transport`](https://github.com/gregjones/httpcache/blob/master/httpcache.go#L99). We can also [customize](https://github.com/gregjones/httpcache/blob/master/httpcache.go#L102) its own `Transport` behavior:

> cacheTransport.Transport = newThrottlingTransport(maxConcurrency, upstreamTransport{delegate: delegate})

At last, the `http.RoundTripper`, `requestCoalescer` uses the `cacheTransport`.

A cache is an implementation of [http.RoundTripper](https://lanre.wtf/blog/2017/07/24/roundtripper-go/). In ghproxy, the customized cache is defined by `requestCoalescer`.

How do we tell our cache not to cache for a request?

`throttlingTransport` takes care of the connection to github.
So the logic should be embedded into its `RoundTrip` [function](https://github.com/kubernetes/test-infra/blob/af1a26bf30f5f3776dba3b171899f400d3fe22ad/ghproxy/ghcache/ghcache.go#L160).

[The way](https://github.com/kubernetes/test-infra/blob/af1a26bf30f5f3776dba3b171899f400d3fe22ad/ghproxy/ghcache/ghcache.go#L183-L185) to do it:

> resp.Header.Set("Cache-Control", "no-store")

where the meaning of the head is defined in [http protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#Cacheability). So our cache lib "github.com/gregjones/httpcache" will use that header.


## OpenShift CI

### Prow

All prow components and prowjobs [are running in namespace](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/config.yaml#L618-L619) `ci`.

* [configuration](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/config.yaml) for prow-components: 
    > oc get configmaps -n ci config
* [prow plugins](https://deck-ci.svc.ci.openshift.org/plugins) and its [configurations](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/plugins.yaml): eg, [approve](https://github.com/kubernetes/test-infra/blob/master/prow/plugins/approve/approvers/README.md):
    > oc get configmaps -n ci plugins

### [ci-tools](https://github.com/openshift/ci-tools)

> Steve: flow of information is prow --> prowjob pod (running ci-operator) --> job pod (created by ci-operator, runs tests)

#### [ci-operator](https://github.com/openshift/ci-tools/tree/master/cmd/ci-operator)

[ci-operator readme on release repo](https://github.com/openshift/release/tree/master/ci-operator).

Starting from a config file for `ci-operator` under [`ci-operator/config/**/`](https://github.com/openshift/release/tree/master/ci-operator/config):


The config file is used in `configMap` [`ci-operator-master-configs`](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/plugins.yaml#L1111-L1114) in `ns` `ci`:

```
$ oc get configmap -n ci ci-operator-master-configs -o yaml | grep openshift-ci-secret-mirroring-controller-master.yaml -A1
  openshift-ci-secret-mirroring-controller-master.yaml: |
    base_images:
```

`ci-operator-master-configs` will be used in the prowjobs defined in the [`ci-operator/jobs/**/`](https://github.com/openshift/release/tree/master/ci-operator/jobs).

### [ci-operator-prowgen](https://github.com/openshift/ci-tools/tree/master/cmd/ci-operator-prowgen)
The prowjobs configuration (they are NOT prowjob CRs) yaml files (`OWNERS` files as well) are generated by `ci-operator-prowgen`. See more [how2](https://github.com/openshift/ci-tools/blob/master/CI_OPERATOR_PROWGEN.md#tldr).

```
###https://github.com/openshift/release/tree/master/ci-operator#ci-operator
$ docker pull registry.svc.ci.openshift.org/ci/ci-operator-prowgen:latest
$ docker run -it -v $(pwd)/ci-operator:/ci-operator:z           \
  registry.svc.ci.openshift.org/ci/ci-operator-prowgen:latest \
  --from-dir /ci-operator/config/ --to-dir /ci-operator/jobs
```

Those generated job configuration files will be mounted to the pods of prow-components via configMap:

* `config-uploader` sync the changes on those files and the configMaps, eg, [`job-config-master-postsubmits`](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/plugins.yaml#L1075-L1077).
* the configMaps, eg, `job-config-master-postsubmits` is [mounted to hook's pod](https://github.com/openshift/release/blob/master/cluster/ci/config/prow/openshift/hook.yaml#L105-L107).

Take a presubmit job [instance](https://prow.svc.ci.openshift.org/prowjob?prowjob=183d5e64-b9ee-11e9-a5f9-0a58ac10330c) for `ci-tools` itself: This prow job and its pod running in `ns` `ci`.
The pod runs `ci-operator`.


```
$ oc get prowjob -n ci 183d5e64-b9ee-11e9-a5f9-0a58ac10330c
NAME                                   JOB                                      BUILDID   TYPE        ORG         REPO       PULLS     STARTTIME   COMPLETIONTIME
183d5e64-b9ee-11e9-a5f9-0a58ac10330c   pull-ci-openshift-ci-tools-master-lint   197       presubmit   openshift   ci-tools   58        39m         38m

$ oc get pod -n ci 183d5e64-b9ee-11e9-a5f9-0a58ac10330c
NAME                                   READY     STATUS      RESTARTS   AGE
183d5e64-b9ee-11e9-a5f9-0a58ac10330c   0/2       Completed   0          35m
```

The job's [log](https://prow.svc.ci.openshift.org/view/gcs/origin-ci-test/pr-logs/pull/openshift_ci-tools/58/pull-ci-openshift-ci-tools-master-lint/197) has
`Using namespace ci-op-gp46wlf7`: The `ci-operator` creates
`ns` `ci-op-gp46wlf7` and does its task in it.

```
$ oc get all -n ci-op-gp46wlf7
NAME                                READY     STATUS      RESTARTS   AGE
pod/applyconfig-build               0/1       Completed   0          10m
pod/bin-build                       0/1       Completed   0          12m
pod/breaking-changes                0/2       Completed   0          10m
pod/ci-operator-build               0/1       Completed   0          10m
pod/ci-operator-checkconfig-build   0/1       Completed   0          10m
pod/ci-operator-prowgen-build       0/1       Completed   0          10m
pod/config-brancher-build           0/1       Completed   0          10m
pod/config-shard-validator-build    0/1       Completed   0          10m
pod/determinize-ci-operator-build   0/1       Completed   0          10m
pod/determinize-prow-jobs-build     0/1       Completed   0          10m
pod/format                          0/2       Completed   0          12m
pod/integration                     0/2       Completed   0          10m
pod/ipi-deprovision-build           0/1       Completed   0          12m
pod/lint                            0/2       Completed   0          12m
pod/pj-rehearse-build               0/1       Completed   0          10m
pod/repo-brancher-build             0/1       Completed   0          10m
pod/src-build                       0/1       Completed   0          12m
pod/unit                            0/2       Completed   0          12m

NAME                                               TYPE      FROM         STATUS     STARTED          DURATION
build.build.openshift.io/src                       Docker    Dockerfile   Complete   12 minutes ago   30s
build.build.openshift.io/bin                       Docker    Dockerfile   Complete   12 minutes ago   1m29s
build.build.openshift.io/ipi-deprovision           Docker                 Complete   12 minutes ago   1m4s
build.build.openshift.io/config-shard-validator    Docker                 Complete   10 minutes ago   58s
build.build.openshift.io/ci-operator-prowgen       Docker                 Complete   10 minutes ago   29s
build.build.openshift.io/config-brancher           Docker                 Complete   10 minutes ago   32s
build.build.openshift.io/ci-operator-checkconfig   Docker                 Complete   10 minutes ago   30s
build.build.openshift.io/determinize-ci-operator   Docker                 Complete   10 minutes ago   33s
build.build.openshift.io/determinize-prow-jobs     Docker                 Complete   10 minutes ago   33s
build.build.openshift.io/ci-operator               Docker                 Complete   10 minutes ago   1m3s
build.build.openshift.io/pj-rehearse               Docker                 Complete   10 minutes ago   1m2s
build.build.openshift.io/repo-brancher             Docker                 Complete   10 minutes ago   31s
build.build.openshift.io/applyconfig               Docker                 Complete   10 minutes ago   34s

NAME                                      DOCKER REPO                                             TAGS                                                          UPDATED
imagestream.image.openshift.io/pipeline   registry.svc.ci.openshift.org/ci-op-gp46wlf7/pipeline   ci-operator,pj-rehearse,config-shard-validator + 15 more...   9 minutes ago
imagestream.image.openshift.io/stable     registry.svc.ci.openshift.org/ci-op-gp46wlf7/stable     ci-operator,pj-rehearse,config-shard-validator + 8 more...    9 minutes ago

```

The builds are from the `images` defined in [the job config](https://github.com/openshift/release/blob/master/ci-operator/config/openshift/ci-tools/openshift-ci-tools-master.yaml#L19).

The pods [for tests in th econfig](https://github.com/openshift/release/blob/master/ci-operator/config/openshift/ci-tools/openshift-ci-tools-master.yaml#L129) (`oc get pod -n ci-op-gp46wlf7 | grep -v build`) are generated from the prowjob pod `183d5e64-b9ee-11e9-a5f9-0a58ac10330c` in `ns` `ci`.

Practice this `ci-tools` with [ci-secret-mirroring-controller](https://github.com/openshift/ci-secret-mirroring-controller):

* Enable `tide` for the repo: [release/pull/4601](https://github.com/openshift/release/pull/4601)
* Configure `OWNERS` of the repo: [ci-secret-mirroring-controller/pull/5](https://github.com/openshift/ci-secret-mirroring-controller/pull/5)
* Enable `approve`-plugin for the repo: [release/pull/4603](https://github.com/openshift/release/pull/4603)
* Follow [ONBOARD.md](https://github.com/openshift/ci-tools/blob/master/ONBOARD.md) to configure prowJobs for the repo: [release/pull/4583](https://github.com/openshift/release/pull/4583): `config` first, then [generate](https://github.com/openshift/ci-tools/blob/master/ONBOARD.md#add-prow-jobs) the jobs and `OWNERS` files.

```
$ JOB_SPEC='{"type":"periodic","job":"periodic-ci-azure-e2e-applysecurityupdates","buildid":"21","prowjobid":"ec28bec2-b7a4-11e9-af8e-0a58ac108dbc","extra_refs":[{"org":"openshift","repo":"openshift-azure","base_ref":"master"}]}' ./ci-operator --config /home/hongkliu/go/src/github.com/openshift/release/ci-operator/config/openshift/ci-secret-mirroring-controller/openshift-ci-secret-mirroring-controller-master.yaml --git-ref openshift/ci-secret-mirroring-controller@master --dry-run

```

[Templates](https://github.com/openshift/ci-tools/blob/master/TEMPLATES.md) and [how2use it for e2e tests with ci-operator](https://github.com/openshift/release/tree/master/ci-operator#end-to-end-tests)

TODO: practice testing with templates

### Others

Inspect the current `ci-operator` image

```
# podman inspect registry.svc.ci.openshift.org/ci/ci-operator:latest | jq -r '.[0].ContainerConfig.Labels["io.openshift.build.commit.id"]' 
7087de11e0ce91d949e9ea6b00cbc1d7fb0561de
```

### build-cop

### ci-search

### others

* [image-mirror setup requests](https://coreos.slack.com/archives/GB7NB0CUC/p1558533720293300)

Deprecated

* [ci-operator](https://github.com/openshift/ci-operator)
* [ci-operator-prowgen](https://github.com/openshift/ci-operator-prowgen)
