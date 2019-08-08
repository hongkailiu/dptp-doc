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

## Automate build-cop report

```
Hongkai Liu   [2 minutes ago]
another crazy thinking ... we could automate the build-cop report since we have the stack ready ... we could ask prometheus/grafana (maybe rest api) for the data ... like you did today ... 3 times / day ... 3h/12h/24h ... can send the email out

Steve Kuznetsov   [< 1 minute ago]
Maybe even more useful would be to set up alerts on the tests when they do not pass the threshold we want

```

Pointer or not

```
Steve Kuznetsov [11:13 AM]
so the idea was this

1. `omitempty` is useful for people, not robots
2. `nil` is nice when you want to tell the difference between a zero-value `struct{}` and nothing
3. in a perfect world, all `struct`s work with their zero values
for instance, the `rerun_auth_config` has a `allow_all` boolean
when you have a `new(rerun_auth_config)` that will be `false`
so the struct is functional in the zero state -- you don't need to check if it's `nil` and then not allow everyone
so we did _not_ want to have a pointer on the ProwJob since that means _everyone_ has to always check if this thing is `nil` -- but it works fine if it is never `nil`
```
