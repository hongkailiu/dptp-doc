# bazel


* [bazelbuild/rules_go](https://github.com/bazelbuild/rules_go)
* [starlark-language](https://docs.bazel.build/versions/master/skylark/language.html#starlark-language)


[Installation](https://docs.bazel.build/versions/master/install-redhat.html):

```
$ cat /etc/*release | head -n 1
Fedora release 29 (Twenty Nine)

# dnf install dnf-plugins-core
# dnf copr enable vbatts/bazel
# dnf install bazel

$ bazel version
...
Build label: 0.23.1- (@non-git)


### https://github.com/bazelbuild/rules_go/issues/1807#issuecomment-436491815
$ sudo dnf install patch
### https://stackoverflow.com/questions/13195110/matlab-kalman-usr-bin-ld-cannot-find-lstdc
$ sudo dnf install libstdc++-static
$ sudo dnf install python2

### https://github.com/bazelbuild/bazelisk
$ curl -OL https://github.com/bazelbuild/bazelisk/releases/download/v0.0.7/bazelisk-linux-amd64
$ sudo mv /usr/bin/bazel /usr/bin/bazel.origin
$ sudo mv bazelisk-linux-amd64 /usr/bin/bazel
$ sudo chmod +x /usr/bin/bazel
$ bazel version
Bazelisk version: v0.0.7
...
Build label: 0.26.1
...

$ bazel clean --expunge

```

## bazel and golang

Examples: [1](https://filipnikolovski.com/managing-go-monorepo-with-bazel/) and [2](https://chrislovecnm.com/golang/bazel/bazel-hello-world/)

```
$ cat WORKSPACE 
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "io_bazel_rules_go",
    urls = ["https://github.com/bazelbuild/rules_go/releases/download/0.18.0/rules_go-0.18.0.tar.gz"],
    sha256 = "301c8b39b0808c49f98895faa6aa8c92cbd605ab5ad4b6a3a652da33a1a2ba2e",
)
http_archive(
    name = "bazel_gazelle",
    urls = ["https://github.com/bazelbuild/bazel-gazelle/releases/download/0.17.0/bazel-gazelle-0.17.0.tar.gz"],
    sha256 = "3c681998538231a2d24d0c07ed5a7658cb72bfb5fd4bf9911157c0e9ac6a2687",
)
load("@io_bazel_rules_go//go:deps.bzl", "go_rules_dependencies", "go_register_toolchains")
go_rules_dependencies()
go_register_toolchains()
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
gazelle_dependencies()

$ cat BUILD.bazel 
load("@bazel_gazelle//:def.bzl", "gazelle")

gazelle(
    name = "gazelle",
    prefix = "github.com/hongkailiu/test-go",
    external = "vendored",
)

### generate build files with "gazelle"
$ bazel run //:gazelle

### build http
$ bazel build //cmd/http

$ bazel test //...
$ bazel clean
###
$ bazel build //prow/cmd/deck/...

```
