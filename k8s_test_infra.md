# [kubernetes/test-infra](https://github.com/kubernetes/test-infra)

## [prow](https://github.com/kubernetes/test-infra/tree/master/prow)

* [getting_started_deploy](https://github.com/kubernetes/test-infra/blob/master/prow/getting_started_deploy.md)


```
$ go version
go version go1.11.5 linux/amd64
$ bazel version
Build label: 0.23.1- (@non-git)
...


```
`tackle` binary method:

```
$ /home/liu/go/bin/tackle
Existing kubernetes contexts:
* 0: abc/ec2-34-209-72-132-us-west-2-compute-amazonaws-com:8443/redhat (current)
  1: admin
  2: default/192-168-122-65:8443/
  3: default/ec2-34-209-72-132-us-west-2-compute-amazonaws-com:8443/redhat
  4: minikube

Choose context or [create new]: 0
Applying admin role bindings (to create RBAC rules)...
FATA[0020] Failed to apply cluster role binding to abc/ec2-34-209-72-132-us-west-2-compute-amazonaws-com:8443/redhat  error="current account: exec: \"gcloud\": executable file not found in $PATH"
```

bazel methods: blocked: Should be different by now. Let debug the add-hook problem first.

```
$ bazel run //prow/cmd/tackle
...
Error applying patch @io_bazel_rules_go//third_party:org_golang_x_tools-gazelle.patch:
bash: patch: command not found

```

manual steps: Need to debug why it does not work.

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
   --hmac-path=/home/liu/abc/hmac-token \
   --github-token-path=/home/liu/abc/ci-oauth-token \
   --hook-url http://hook-abc.apps.hongkliu1.qe.devcluster.openshift.com \
   --repo dev-tool-index
...
INFO[0000] ListOrgHooks(dev-tool-index)                  client=github
FATA[0007] Could not apply hook to dev-tool-index: list: return code not 2XX: 404 Not Found

```

### sinker

```
$ go get -d k8s.io/test-infra/prow/cmd/sinker
$ cd ${GOPATH}/src/k8s.io/test-infra
$ go build ./prow/cmd/sinker/

### oc login: ready
$ ./sinker --kubeconfig=/home/hongkliu/.kube/config --config-path=/home/hongkliu/go/src/k8s.io/test-infra/prow/config.yaml

$ ./sinker --kubeconfig=/home/hongkliu/.kube/config --config-path=/home/hongkliu/go/src/k8s.io/test-infra/prow/config.yaml --job-config-path=/home/hongkliu/go/src/k8s.io/test-infra/config/jobs

```

Run tests:

```
$ go test ./prow/cmd/sinker/ -v
```

## tide

```
### https://stackoverflow.com/questions/13195110/matlab-kalman-usr-bin-ld-cannot-find-lstdc
$ sudo dnf install libstdc++-static
$ bazel build //prow/cmd/tide/...
$ ll bazel-bin/prow/cmd/tide/linux_amd64_pure_stripped/tide
-r-xr-xr-x. 1 hongkliu hongkliu 33392840 Mar 24 09:01 bazel-bin/prow/cmd/tide/linux_amd64_pure_stripped/tide
```

## mkpj

```
### https://coreos.slack.com/archives/GB7NB0CUC/p1556812445275800
$ bazel run //prow/cmd/mkpj -- --help
$ bazel run //prow/cmd/mkpj -- --config-path=/home/hongkliu/go/src/github.com/openshift/release/cluster/ci/config/prow/config.yaml --job-config-path=/home/hongkliu/go/src/github.com/openshift/release/ci-operator/jobs --job=pull-ci-openshift-release-master-generated-dashboards  --base-ref=master --base-sha=b05852c0f7cf57b11be737f433fc1f4d8cf80be1 --pull-sha=bc16979c38cfde24589efac69bd588cbb4f4c326 --pull-author=hongkailiu --pull-number=3664
...
apiVersion: prow.k8s.io/v1
kind: ProwJob
...

### write it to /home/hongkliu/Downloads/abc.yaml
$ bazel run //prow/cmd/mkpod -- --prow-job=/home/hongkliu/Downloads/abc.yaml
...
apiVersion: v1
kind: Pod

### write it to /home/hongkliu/Downloads/abc1.yaml
$ oc apply -n ci -f  /home/hongkliu/Downloads/abc1.yaml
pod/0f609c54-6d1f-11e9-a908-c85b76866133 created

### with container
###presubmit
# podman run --rm --volume "${PWD}:/tmp/release:z" --workdir /tmp/release gcr.io/k8s-prow/mkpj:v20191023-cb1899b6e --config-path core-services/prow/02_config/_config.yaml --job-config-path ci-operator/jobs/ --job pull-ci-openshift-release-master-build01-dry --base-ref=master --base-sha=5fe03dff8 --pull-sha=73cfc197d9c7d526231d8c318b0fb6eab8b5b12e --pull-author=hongkailiu --pull-number=5534

###postsubmit
# podman run --rm --volume "${PWD}:/tmp/release:z" --workdir /tmp/release gcr.io/k8s-prow/mkpj:v20191107-34a664162 --config-path core-services/prow/02_config/_config.yaml --job-config-path ci-operator/jobs/ --job branch-ci-openshift-ci-secret-mirroring-controller-master-images --base-ref=master --base-sha=f235b499aac6d84d9c79cce15df88a3d5c41c255
```

test  Periodics with docker:

```
### https://coreos.slack.com/archives/GB7NB0CUC/p1567761640222700
$ docker run --rm --volume "${PWD}:/tmp/release:z" --workdir /tmp/release gcr.io/k8s-prow/mkpj:v20190827-70272a1e1 --config-path cluster/ci/config/prow/config.yaml --job-config-path ci-operator/jobs/ --job YOUR_JOB_HERE

# podman run --rm --volume "${PWD}:/tmp/release:z" --workdir /tmp/release gcr.io/k8s-prow/mkpj:v20190918-7672de02b --config-path core-services/prow/02_config/_config.yaml --job-config-path ci-operator/jobs/ --job periodic-prow-image-autoowners


```

## branchprotector

[src](https://github.com/kubernetes/test-infra/tree/master/prow/cmd/branchprotector)

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

## Others
* github webhook
* bazel
