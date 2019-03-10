# [kubernetes/test-infra](https://github.com/kubernetes/test-infra)

## [prow](https://github.com/kubernetes/test-infra/tree/master/prow)

[getting_started_deploy.md](https://github.com/kubernetes/test-infra/blob/master/prow/getting_started_deploy.md)

```
$ go version
go version go1.11.5 linux/amd64
$ bazel version
Build label: 0.23.1- (@non-git)
Build target: bazel-out/k8-opt/bin/src/main/java/com/google/devtools/build/lib/bazel/BazelServer_deploy.jar
Build time: Mon Mar 4 13:46:01 2019 (1551707161)
Build timestamp: 1551707161
Build timestamp as int: 1551707161

```

* [getting_started_deploy](https://github.com/kubernetes/test-infra/blob/master/prow/getting_started_deploy.md)

bazel methods: blocked

```
$ bazel run //prow/cmd/tackle
INFO: SHA256 (https://codeload.github.com/golang/tools/zip/bf090417da8b6150dcfe96795325f5aa78fff718) = 11629171a39a1cb4d426760005be6f7cb9b4182e4cb2756b7f1c5c2b6ae869fe
DEBUG: Rule 'io_kubernetes_build' modified arguments {"shallow_since": "1517262872 -0800"}
ERROR: /home/liu/go/src/k8s.io/test-infra/BUILD.bazel:15:1: no such package '@org_golang_x_tools//go/analysis/passes/unusedresult': Traceback (most recent call last):
	File "/home/liu/.cache/bazel/_bazel_liu/dfa086725f77f9c3976de48d68ce12a2/external/bazel_tools/tools/build_defs/repo/http.bzl", line 55
		patch(ctx)
	File "/home/liu/.cache/bazel/_bazel_liu/dfa086725f77f9c3976de48d68ce12a2/external/bazel_tools/tools/build_defs/repo/utils.bzl", line 84, in patch
		fail(("Error applying patch %s:\n%s%s...)))
Error applying patch @io_bazel_rules_go//third_party:org_golang_x_tools-gazelle.patch:
bash: patch: command not found
 and referenced by '//:nogo_vet'
ERROR: Analysis of target '//prow/cmd/tackle:tackle' failed; build aborted: no such package '@org_golang_x_tools//go/analysis/passes/unusedresult': Traceback (most recent call last):
	File "/home/liu/.cache/bazel/_bazel_liu/dfa086725f77f9c3976de48d68ce12a2/external/bazel_tools/tools/build_defs/repo/http.bzl", line 55
		patch(ctx)
	File "/home/liu/.cache/bazel/_bazel_liu/dfa086725f77f9c3976de48d68ce12a2/external/bazel_tools/tools/build_defs/repo/utils.bzl", line 84, in patch
		fail(("Error applying patch %s:\n%s%s...)))
Error applying patch @io_bazel_rules_go//third_party:org_golang_x_tools-gazelle.patch:
bash: patch: command not found
INFO: Elapsed time: 2.213s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (1 packages loaded, 1 target configured)
FAILED: Build did NOT complete successfully (1 packages loaded, 1 target configured)
    Fetching @org_golang_x_tools; Patching repository


```

manual steps: blocked

```
$ oc new-project abc
$ kubectl create secret generic hmac-token --from-file=hmac=/home/liu/abc/hmac-token
$ kubectl create secret generic oauth-token --from-file=oauth=/home/liu/abc/ci-oauth-token
### replace default with abc
$ vi prow/cluster/starter.yaml
$ oc create -f prow/cluster/starter.yaml

### no address for the ingress ing
# oc get ingress ing
NAME      HOSTS     ADDRESS   PORTS     AGE
ing       *                   80        26m
### tried to use routes
# oc expose svc deck
# oc expose svc hook

$ bazel run //experiment/add-hook -- \
>   --hmac-path=/home/liu/abc/hmac-token \
>   --github-token-path=/home/liu/abc/ci-oauth-token \
>   --hook-url http://hook-abc.apps.34.209.72.132.xip.io/hook \
>   --repo dev-tool-index
Starting local Bazel server and connecting to it...
DEBUG: Rule 'io_kubernetes_build' modified arguments {"shallow_since": "1517262872 -0800"}
INFO: SHA256 (https://codeload.github.com/golang/tools/zip/bf090417da8b6150dcfe96795325f5aa78fff718) = 11629171a39a1cb4d426760005be6f7cb9b4182e4cb2756b7f1c5c2b6ae869fe
ERROR: /home/liu/go/src/k8s.io/test-infra/BUILD.bazel:15:1: no such package '@org_golang_x_tools//go/analysis/passes/unusedresult': Traceback (most recent call last):
	File "/home/liu/.cache/bazel/_bazel_liu/dfa086725f77f9c3976de48d68ce12a2/external/bazel_tools/tools/build_defs/repo/http.bzl", line 55
		patch(ctx)
	File "/home/liu/.cache/bazel/_bazel_liu/dfa086725f77f9c3976de48d68ce12a2/external/bazel_tools/tools/build_defs/repo/utils.bzl", line 84, in patch
		fail(("Error applying patch %s:\n%s%s...)))
Error applying patch @io_bazel_rules_go//third_party:org_golang_x_tools-gazelle.patch:
bash: patch: command not found
 and referenced by '//:nogo_vet'
ERROR: Analysis of target '//experiment/add-hook:add-hook' failed; build aborted: no such package '@org_golang_x_tools//go/analysis/passes/unusedresult': Traceback (most recent call last):
	File "/home/liu/.cache/bazel/_bazel_liu/dfa086725f77f9c3976de48d68ce12a2/external/bazel_tools/tools/build_defs/repo/http.bzl", line 55
		patch(ctx)
	File "/home/liu/.cache/bazel/_bazel_liu/dfa086725f77f9c3976de48d68ce12a2/external/bazel_tools/tools/build_defs/repo/utils.bzl", line 84, in patch
		fail(("Error applying patch %s:\n%s%s...)))
Error applying patch @io_bazel_rules_go//third_party:org_golang_x_tools-gazelle.patch:
bash: patch: command not found
INFO: Elapsed time: 46.052s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (265 packages loaded, 7597 targets configured)
FAILED: Build did NOT complete successfully (265 packages loaded, 7597 targets configured)
    Fetching @org_golang_x_tools; Patching repository

```

### sinker

```
$ go get -d k8s.io/test-infra/prow/cmd/sinker
```

## Others
* github webhook
* bazel
