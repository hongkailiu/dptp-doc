# TODO

## GOLang

* Book: The Go Programming Language
* [go-tooling-workshop](https://github.com/campoy/go-tooling-workshop)
* [go-delve](https://github.com/go-delve/delve)

## Tool

* strace
* jaeger

* jsonnet
* https://jenkins-x.io/, [gke-vs-aks-vs-eks](https://blog.hasura.io/gke-vs-aks-vs-eks-411f080640dc/), [jenkins-x and prow](https://technologyconversations.com/2019/04/15/going-serverless-with-jenkins-x-exploring-prow-jenkins-x-pipeline-operator-and-tekton/)
* https://draft.sh/
* https://tekton.dev/

* https://sentry.io/
* https://www.datadoghq.com/
* https://cloud.google.com/stackdriver/

* [testgrid](https://github.com/kubernetes/test-infra/tree/master/testgrid)
    * [talk.by.Michelle.Shepardson](https://www.youtube.com/watch?v=jm2l2SLq_yE)

## books

* https://landing.google.com/sre/books/

## slack
Steve Kuznetsov [7:18 PM]
@Petr Muller @nmoraitis @bbguimaraes @hongkliu we now have all logs from Prow in Stackdriver for the GCE "origin-ci-infra" project -- they are parsed out into JSON from the logs, so you can search by key-value pairs like URL or github comment ID, etc -- let me know how it works for y'all

Katharine [1:30 PM]
replied to a thread:
I recommend installing bazelisk (`go get github.com/bazelbuild/bazelisk`) and just symlinking bazel to that

## jira

templating cards based on this [gdoc](https://docs.google.com/document/d/11jvb7yWNVQ3-fXwjpfVDAIY6BRVFjroDoDMcGwR57js/edit).

## bump up prow component version

```
Steve Kuznetsov   [2 hours ago]
do the bump: https://github.com/openshift/release/pull/3898
I just run the `hack/bump-prow-images.sh` script  and have it merge, while running `hack/prow-monitor.py` in a different console (I always have that running)

$ gcloud config list
[core]
account = <kerberos_id>@redhat.com
disable_usage_reporting = True
project = openshift-ci-infra


Steve Kuznetsov   [2 hours ago]
these days we should be able to also get alerts on error messages from stackdriver


```

## Automate build-cop report

```
Hongkai Liu   [2 minutes ago]
another crazy thinking ... we could automate the build-cop report since we have the stack ready ... we could ask prometheus/grafana (maybe rest api) for the data ... like you did today ... 3 times / day ... 3h/12h/24h ... can send the email out

Steve Kuznetsov   [< 1 minute ago]
Maybe even more useful would be to set up alerts on the tests when they do not pass the threshold we want

```
