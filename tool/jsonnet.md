# [jsonnet](https://jsonnet.org/)

* [syntax](https://jsonnet.org/learning/tutorial.html)
* [tooling](https://jsonnet.org/learning/tools.html)
    * IDE plugin available: tested with intellij
* [ksonnet-lib](https://github.com/ksonnet/ksonnet-lib)
* [jsonnet-bundler](https://github.com/jsonnet-bundler/jsonnet-bundler)

## install

```
### not working
### https://copr.fedorainfracloud.org/coprs/randomvariable/jsonnet/
$ sudo dnf copr enable randomvariable/jsonnet
$ sudo dnf install jsonnet

### https://github.com/google/go-jsonnet
$ go get github.com/google/go-jsonnet/cmd/jsonnet
$ jsonnet --version
Jsonnet commandline interpreter v0.12.1
$ go get github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb

```

c++ version, compile from src:

```
###https://github.com/openshift/release/pull/3730/commits/8269527a73eb9457efec416bfff6a0d73d16ba3e
$ sudo dnf groupinstall 'Development Tools'
$ sudo dnf install gcc-c++
$ git clone https://github.com/google/jsonnet.git
$ cd jsonnet && make && cp jsonnet ~/bin/

```

## start

```
$ cd ${GOPATH}/src/github.com/hongkailiu/test-go/test-go-mixin
$ jb init
$ jb install https://github.com/kubernetes-monitoring/kubernetes-mixin
$ jb install https://github.com/grafana/grafonnet-lib/grafonnet

```
