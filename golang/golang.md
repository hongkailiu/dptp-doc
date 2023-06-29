# [GoLang](https://golang.org/)

## Tutorial

* [golangbot.com](https://golangbot.com/learn-golang-series/)

## Installation

### [from binary](https://golang.org/doc/install)

```sh
$ cd ~/tool
$ wget https://dl.google.com/go/go1.9.3.linux-amd64.tar.gz
$ tar -xzf go1.9.3.linux-amd64.tar.gz
$ mv go go1.9.3
$ ln -s go1.9.3 go

### Append ~/.bashrc
...
export GOROOT=$HOME/tool/go
export PATH=$PATH:$GOROOT/bin
export GOPATH=$HOME/repo/go
export PATH=$GOPATH/bin:$PATH

$ go version
go version go1.9.3 linux/amd64
```

### from dnf
Follow [those steps](README.md#prerequisites).

## Cli

## IDE
* Intellij Ultimate Edition + go plugin
* vscode
* goland: [installation](https://www.jetbrains.com/help/go/installation-guide.html#first-run)
  * M2 (apple silicon): with "aarch64" in the filename, e.g., goland-2023.1.3-aarch64.dmg, on [the download page](https://www.jetbrains.com/go/download/?#section=mac)
  * [version-control-local-changes](https://dirask.com/posts/IntelliJ-IDEA-show-version-control-local-changes-1bdzMp)

### Dep. Management

## awesome
https://github.com/avelino/awesome-go

https://github.com/gostor/awesome-go-storage

### logging

* [sirupsen/logrus](https://github.com/sirupsen/logrus)
* [op/go-logging](https://github.com/op/go-logging)

### goroutine pool

* [go-playground/pool](https://github.com/go-playground/pool)

### cli

* [spf13/cobra](https://github.com/spf13/cobra)

## Libs

go template:

https://godoc.org/text/template#pkg-subdirectories
https://blog.gopheracademy.com/advent-2017/using-go-templates/

code-generator:

https://github.com/kubernetes/code-generator
https://kubernetes.io/docs/contribute/generate-ref-docs/kubernetes-api/

swagger:

https://swagger.io/docs/specification/about/

database:

https://flaviocopes.com/golang-sql-database/
https://github.com/golang-migrate/migrate
https://github.com/pressly/goose

http:

* [`Client`](https://github.com/golang/go/blob/master/src/net/http/client.go#L56): has a [`Transport`](https://github.com/golang/go/blob/master/src/net/http/client.go#L60) field which is `RoundTrip`.

* `Transport`: If we use [`DefaultClient`](https://github.com/golang/go/blob/master/src/net/http/client.go#L108), it uses [DefaultTransport](https://github.com/golang/go/blob/master/src/net/http/transport.go#L42) which does caching as well.

* `RoundTrip`: is an interface defining only one method: [`RoundTrip`](https://github.com/golang/go/blob/master/src/net/http/client.go#L115-L141). A `Transport` usually implements `RoundTrip`, eg, `DefaultClient`.

So [blog](https://lanre.wtf/blog/2017/07/24/roundtripper-go/) shows
that how a http client is made by a [customized](https://github.com/adelowo/rounder/blob/master/client/main.go#L27-L30) `Transport` to do caching. It uses a chain of `Transport`: `cachedTransport` for caching and
`http.DefaultTransport` for connecting the server.
In other words, a customized client can use a `RoundTrip` which
is usually a `Transport` which chains up a `http.DefaultTransport` and embedding its own logic by its own implementation of `RoundTrip`.

http reverse proxy: [1](https://hackernoon.com/writing-a-reverse-proxy-in-just-one-line-with-go-c1edfa78c84b), [2](https://blog.charmes.net/post/reverse-proxy-go/)

## Test
* [gomega](https://onsi.github.io/gomega/) and [ginkgo](https://onsi.github.io/ginkgo/)
* [testify](https://github.com/stretchr/testify/) and [mockery](https://github.com/vektra/mockery): [examples](https://blog.lamida.org/mocking-in-golang-using-testify/)
* [gomock](https://github.com/golang/mock/): [examples](https://blog.codecentric.de/en/2017/08/gomock-tutorial/)

## godoc

[godoc.org](https://godoc.org/) generates and hosts api docs for
 go project hosted eg, at github.com.
See [how to write doc for golang](https://blog.golang.org/godoc-documenting-go-code).
[Here](https://godoc.org/github.com/hongkailiu/test-go) is the doc for svt-go.

[Generate and view goDoc locally](https://godoc.org/golang.org/x/tools/cmd/godoc).


## CICD

## Good practice

* https://github.com/golang/go/wiki/CodeReviewComments


## [migrating-from-glide-to-dep](https://golang.github.io/dep/docs/migrating.html)

Install `dep`:

```
$ curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
$ dep version
dep:
 version     : v0.5.0
 build date  : 2018-07-26
 git hash    : 224a564
 go version  : go1.10.3
 go compiler : gc
 platform    : linux/amd64
 features    : ImportDuringSolve=false

```

Generate dep files: NOT work for my test-go repo (does not return over several hours). Had to remove all go file, `dep init`, and add it back one by one.

```
$ dep init
```

## [go mod](https://github.com/golang/go/wiki/Modules)

[migrating-from-dep-to-go-mod](https://blog.callr.tech/migrating-from-dep-to-go-1.11-modules/)

```
$ echo $GOPATH
/home/hongkliu/go
$ pwd
/home/hongkliu/repo/me
$ cp -r ~/go/src/github.com/hongkailiu/test-go/ .
$ cd ./test-go
$ go mod init
go: creating new go.mod: module github.com/hongkailiu/test-go
go: copying requirements from Gopkg.lock
$ go mod tidy

### some error: solution: https://github.com/go-gormigrate/gormigrate/pull/27/files
### bazel still need the vendor folder

### update a single dep.
$ go get -u github.com/gin-gonic/gin
$ go mod vendor

```

k8s: [go-modules](https://github.com/kubernetes/enhancements/blob/master/keps/sig-architecture/2019-03-19-go-modules.md); [go-mod-with-vendor](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/vendor.md);
k8s/client-go: [go-modules](https://github.com/kubernetes/client-go/blob/master/INSTALL.md#go-modules)


k8s as module: [go/issues/32776](https://github.com/golang/go/issues/32776), [kubernetes/issues/79384](https://github.com/kubernetes/kubernetes/issues/79384).


Ref:
* [daily-workflow](https://github.com/golang/go/wiki/Modules#daily-workflow)
* [GO111MODULE](https://tip.golang.org/cmd/go/#hdr-Module_support)
* [Golang Module Vs Dep: Pros & Cons](https://www.activestate.com/blog/golang-module-vs-dep-pros-cons/)
* [vendoring-with-modules?](https://github.com/golang/go/wiki/Modules#how-do-i-use-vendoring-with-modules-is-vendoring-going-away)
* [Intellij with go-mod support](https://www.jetbrains.com/help/go/create-a-project-with-vgo-integration.html)
* [goproxy](https://goproxy.io/)
* [vgo-mvs](https://research.swtch.com/vgo-mvs)
* [The_go_mod_file](https://golang.org/cmd/go/#hdr-The_go_mod_file)
