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
Extracting Bazel installation...
WARNING: --batch mode is deprecated. Please instead explicitly shut down your Bazel server using the command "bazel shutdown".
Build label: 0.23.1- (@non-git)
Build target: bazel-out/k8-opt/bin/src/main/java/com/google/devtools/build/lib/bazel/BazelServer_deploy.jar
Build time: Mon Mar 4 13:46:01 2019 (1551707161)
Build timestamp: 1551707161
Build timestamp as int: 1551707161

### https://github.com/bazelbuild/rules_go/issues/1807#issuecomment-436491815
$ sudo dnf install patch

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


```
