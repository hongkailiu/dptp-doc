# [kubernetes/test-infra](https://github.com/kubernetes/test-infra)

## [prow](https://github.com/kubernetes/test-infra/tree/master/prow)

* [getting_started_deploy](https://github.com/kubernetes/test-infra/blob/master/prow/getting_started_deploy.md)

bazel methods: blocked

```
$ bazel run //prow/cmd/takle
Starting local Bazel server and connecting to it...
DEBUG: Rule 'bazel_skylib' modified arguments {"commit": "f83cb8dd6f5658bc574ccd873e25197055265d1c", "shallow_since": "1543273402 -0500"} and dropped ["tag"]
DEBUG: Rule 'build_bazel_rules_nodejs' modified arguments {"commit": "0eb4a19507211ab3863f4d82e9412a33f759abcd", "shallow_since": "1548802468 -0800"} and dropped ["tag"]
DEBUG: Rule 'io_bazel_rules_appengine' modified arguments {"shallow_since": "1498750863 -0400"}
DEBUG: Rule 'io_bazel_rules_python' modified arguments {"shallow_since": "1546820050 -0500"}
ERROR: Skipping '//prow/cmd/takle': no such package 'prow/cmd/takle': BUILD file not found on package path
WARNING: Target pattern parsing failed.
ERROR: no such package 'prow/cmd/takle': BUILD file not found on package path
INFO: Elapsed time: 32.584s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (0 packages loaded)
FAILED: Build did NOT complete successfully (0 packages loaded)

```

### sinker

```
$ go get -d k8s.io/test-infra/prow/cmd/sinker
```

## Others
* github webhook
* bazel
