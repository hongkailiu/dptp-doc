Followed [go/issues/32776](https://github.com/golang/go/issues/32776), [kubernetes/issues/79384](https://github.com/kubernetes/kubernetes/issues/79384).

Applied to repo `k8s.io/test-infra`. Could we use it as a mod?

```
# go version
go version go1.12.5 linux/amd64
# go env
GOARCH="amd64"
GOBIN=""
GOCACHE="/go/.cache"
GOEXE=""
GOFLAGS=""
GOHOSTARCH="amd64"
GOHOSTOS="linux"
GOOS="linux"
GOPATH="/go"
GOPROXY=""
GORACE=""
GOROOT="/usr/local/go"
GOTMPDIR=""
GOTOOLDIR="/usr/local/go/pkg/tool/linux_amd64"
GCCGO="gccgo"
CC="gcc"
CXX="g++"
CGO_ENABLED="1"
GOMOD="/aaa/go.mod"
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build716361819=/tmp/go-build -gno-record-gcc-switches"


# mkdir demo
# go mod init demo
# vi demo/main.go 
package main

import (
        _ "k8s.io/test-infra/prow/pod-utils/downwardapi"
)

func main() {

}

# go get -v -u ./...
Fetching https://golang.org/x/crypto?go-get=1
Fetching https://google.golang.org/genproto?go-get=1
Parsing meta tags from https://golang.org/x/crypto?go-get=1 (status code 200)
get "golang.org/x/crypto": found meta tag get.metaImport{Prefix:"golang.org/x/crypto", VCS:"git", RepoRoot:"https://go.googlesource.com/crypto"} at https://golang.org/x/crypto?go-get=1
Parsing meta tags from https://google.golang.org/genproto?go-get=1 (status code 200)
get "google.golang.org/genproto": found meta tag get.metaImport{Prefix:"google.golang.org/genproto", VCS:"git", RepoRoot:"https://github.com/google/go-genproto"} at https://google.golang.org/genproto?go-get=1
go: finding github.com/alecthomas/template latest
Fetching https://golang.org/x/sync?go-get=1
Fetching https://gopkg.in/alecthomas/kingpin.v2?go-get=1
Parsing meta tags from https://golang.org/x/sync?go-get=1 (status code 200)
get "golang.org/x/sync": found meta tag get.metaImport{Prefix:"golang.org/x/sync", VCS:"git", RepoRoot:"https://go.googlesource.com/sync"} at https://golang.org/x/sync?go-get=1
go: finding github.com/eapache/go-xerial-snappy latest
Fetching https://sigs.k8s.io/controller-runtime?go-get=1
go: finding github.com/mattbaird/jsonpatch latest
Fetching https://google.golang.org/grpc?go-get=1
Parsing meta tags from https://google.golang.org/grpc?go-get=1 (status code 200)
get "google.golang.org/grpc": found meta tag get.metaImport{Prefix:"google.golang.org/grpc", VCS:"git", RepoRoot:"https://github.com/grpc/grpc-go"} at https://google.golang.org/grpc?go-get=1
go: finding google.golang.org/genproto latest
Parsing meta tags from https://gopkg.in/alecthomas/kingpin.v2?go-get=1 (status code 200)
get "gopkg.in/alecthomas/kingpin.v2": found meta tag get.metaImport{Prefix:"gopkg.in/alecthomas/kingpin.v2", VCS:"git", RepoRoot:"https://gopkg.in/alecthomas/kingpin.v2"} at https://gopkg.in/alecthomas/kingpin.v2?go-get=1
Parsing meta tags from https://sigs.k8s.io/controller-runtime?go-get=1 (status code 200)
get "sigs.k8s.io/controller-runtime": found meta tag get.metaImport{Prefix:"sigs.k8s.io/controller-runtime", VCS:"git", RepoRoot:"https://github.com/kubernetes-sigs/controller-runtime"} at https://sigs.k8s.io/controller-runtime?go-get=1
go: finding golang.org/x/crypto latest
go: finding golang.org/x/sync latest
Fetching https://golang.org/x/tools?go-get=1
Parsing meta tags from https://golang.org/x/tools?go-get=1 (status code 200)
get "golang.org/x/tools": found meta tag get.metaImport{Prefix:"golang.org/x/tools", VCS:"git", RepoRoot:"https://go.googlesource.com/tools"} at https://golang.org/x/tools?go-get=1
Fetching https://gopkg.in/inf.v0?go-get=1
Parsing meta tags from https://gopkg.in/inf.v0?go-get=1 (status code 200)
get "gopkg.in/inf.v0": found meta tag get.metaImport{Prefix:"gopkg.in/inf.v0", VCS:"git", RepoRoot:"https://gopkg.in/inf.v0"} at https://gopkg.in/inf.v0?go-get=1
Fetching https://k8s.io/api?go-get=1
go: finding github.com/google/pprof latest
Fetching https://go.uber.org/atomic?go-get=1
go: finding golang.org/x/tools latest
go: finding github.com/tmc/grpc-websocket-proxy latest
Parsing meta tags from https://k8s.io/api?go-get=1 (status code 200)
get "k8s.io/api": found meta tag get.metaImport{Prefix:"k8s.io/api", VCS:"git", RepoRoot:"https://github.com/kubernetes/api"} at https://k8s.io/api?go-get=1
go: finding github.com/golang/glog latest
Parsing meta tags from https://go.uber.org/atomic?go-get=1 (status code 200)
get "go.uber.org/atomic": found meta tag get.metaImport{Prefix:"go.uber.org/atomic", VCS:"git", RepoRoot:"https://github.com/uber-go/atomic"} at https://go.uber.org/atomic?go-get=1
go: finding github.com/jmespath/go-jmespath latest
go: finding github.com/Azure/azure-sdk-for-go v32.3.0+incompatible
Fetching https://k8s.io/test-infra?go-get=1
Parsing meta tags from https://k8s.io/test-infra?go-get=1 (status code 200)
get "k8s.io/test-infra": found meta tag get.metaImport{Prefix:"k8s.io/test-infra", VCS:"git", RepoRoot:"https://github.com/kubernetes/test-infra"} at https://k8s.io/test-infra?go-get=1
Fetching https://golang.org/x/lint?go-get=1
Parsing meta tags from https://golang.org/x/lint?go-get=1 (status code 200)
get "golang.org/x/lint": found meta tag get.metaImport{Prefix:"golang.org/x/lint", VCS:"git", RepoRoot:"https://go.googlesource.com/lint"} at https://golang.org/x/lint?go-get=1
go: finding github.com/knative/pkg latest
go: finding k8s.io/api latest
Fetching https://mvdan.cc/xurls/v2?go-get=1
go: finding golang.org/x/lint latest
Parsing meta tags from https://mvdan.cc/xurls/v2?go-get=1 (status code 200)
get "mvdan.cc/xurls/v2": found meta tag get.metaImport{Prefix:"mvdan.cc/xurls", VCS:"git", RepoRoot:"https://github.com/mvdan/xurls"} at https://mvdan.cc/xurls/v2?go-get=1
get "mvdan.cc/xurls/v2": verifying non-authoritative meta tag
Fetching https://mvdan.cc/xurls?go-get=1
Parsing meta tags from https://mvdan.cc/xurls?go-get=1 (status code 200)
go: finding k8s.io/test-infra latest
Fetching https://golang.org/x/sys?go-get=1
Fetching https://go.uber.org/multierr?go-get=1
go: finding github.com/aws/aws-k8s-tester latest
Parsing meta tags from https://golang.org/x/sys?go-get=1 (status code 200)
get "golang.org/x/sys": found meta tag get.metaImport{Prefix:"golang.org/x/sys", VCS:"git", RepoRoot:"https://go.googlesource.com/sys"} at https://golang.org/x/sys?go-get=1
Fetching https://golang.org/x/net?go-get=1
Parsing meta tags from https://go.uber.org/multierr?go-get=1 (status code 200)
get "go.uber.org/multierr": found meta tag get.metaImport{Prefix:"go.uber.org/multierr", VCS:"git", RepoRoot:"https://github.com/uber-go/multierr"} at https://go.uber.org/multierr?go-get=1
go: finding github.com/shurcooL/go latest
Parsing meta tags from https://golang.org/x/net?go-get=1 (status code 200)
get "golang.org/x/net": found meta tag get.metaImport{Prefix:"golang.org/x/net", VCS:"git", RepoRoot:"https://go.googlesource.com/net"} at https://golang.org/x/net?go-get=1
go: finding golang.org/x/sys latest
Fetching https://k8s.io/code-generator?go-get=1
go: finding golang.org/x/net latest
Parsing meta tags from https://k8s.io/code-generator?go-get=1 (status code 200)
get "k8s.io/code-generator": found meta tag get.metaImport{Prefix:"k8s.io/code-generator", VCS:"git", RepoRoot:"https://github.com/kubernetes/code-generator"} at https://k8s.io/code-generator?go-get=1
Fetching https://k8s.io/apimachinery?go-get=1
Parsing meta tags from https://k8s.io/apimachinery?go-get=1 (status code 200)
get "k8s.io/apimachinery": found meta tag get.metaImport{Prefix:"k8s.io/apimachinery", VCS:"git", RepoRoot:"https://github.com/kubernetes/apimachinery"} at https://k8s.io/apimachinery?go-get=1
Fetching https://k8s.io/gengo?go-get=1
Parsing meta tags from https://k8s.io/gengo?go-get=1 (status code 200)
get "k8s.io/gengo": found meta tag get.metaImport{Prefix:"k8s.io/gengo", VCS:"git", RepoRoot:"https://github.com/kubernetes/gengo"} at https://k8s.io/gengo?go-get=1
go: finding github.com/denisenkom/go-mssqldb latest
Fetching https://go.uber.org/zap?go-get=1
Parsing meta tags from https://go.uber.org/zap?go-get=1 (status code 200)
get "go.uber.org/zap": found meta tag get.metaImport{Prefix:"go.uber.org/zap", VCS:"git", RepoRoot:"https://github.com/uber-go/zap"} at https://go.uber.org/zap?go-get=1
go: finding k8s.io/apimachinery latest
go: finding k8s.io/code-generator latest
Fetching https://k8s.io/utils?go-get=1
Parsing meta tags from https://k8s.io/utils?go-get=1 (status code 200)
get "k8s.io/utils": found meta tag get.metaImport{Prefix:"k8s.io/utils", VCS:"git", RepoRoot:"https://github.com/kubernetes/utils"} at https://k8s.io/utils?go-get=1
go: finding github.com/gregjones/httpcache latest
go: finding k8s.io/gengo latest
Fetching https://go.opencensus.io?go-get=1
go: finding github.com/rcrowley/go-metrics latest
Parsing meta tags from https://go.opencensus.io?go-get=1 (status code 200)
get "go.opencensus.io": found meta tag get.metaImport{Prefix:"go.opencensus.io", VCS:"git", RepoRoot:"https://github.com/census-instrumentation/opencensus-go"} at https://go.opencensus.io?go-get=1
go: finding k8s.io/utils latest
go: finding github.com/golang/groupcache latest
go: finding github.com/modern-go/concurrent latest
Fetching https://gopkg.in/errgo.v2?go-get=1
Fetching https://go.etcd.io/etcd?go-get=1
Parsing meta tags from https://gopkg.in/errgo.v2?go-get=1 (status code 200)
get "gopkg.in/errgo.v2": found meta tag get.metaImport{Prefix:"gopkg.in/errgo.v2", VCS:"git", RepoRoot:"https://gopkg.in/errgo.v2"} at https://gopkg.in/errgo.v2?go-get=1
Fetching https://k8s.io/repo-infra?go-get=1
Parsing meta tags from https://go.etcd.io/etcd?go-get=1 (status code 200)
get "go.etcd.io/etcd": found meta tag get.metaImport{Prefix:"go.etcd.io/etcd", VCS:"git", RepoRoot:"https://github.com/etcd-io/etcd"} at https://go.etcd.io/etcd?go-get=1
Parsing meta tags from https://k8s.io/repo-infra?go-get=1 (status code 200)
get "k8s.io/repo-infra": found meta tag get.metaImport{Prefix:"k8s.io/repo-infra", VCS:"git", RepoRoot:"https://github.com/kubernetes/repo-infra"} at https://k8s.io/repo-infra?go-get=1
go: finding github.com/xlab/handysort latest
Fetching https://gopkg.in/tomb.v1?go-get=1
Parsing meta tags from https://gopkg.in/tomb.v1?go-get=1 (status code 200)
get "gopkg.in/tomb.v1": found meta tag get.metaImport{Prefix:"gopkg.in/tomb.v1", VCS:"git", RepoRoot:"https://gopkg.in/tomb.v1"} at https://gopkg.in/tomb.v1?go-get=1
go: finding k8s.io/repo-infra latest
go: finding github.com/shurcooL/graphql latest
Fetching https://gopkg.in/check.v1?go-get=1
Fetching https://google.golang.org/appengine?go-get=1
Fetching https://honnef.co/go/tools?go-get=1
Parsing meta tags from https://google.golang.org/appengine?go-get=1 (status code 200)
get "google.golang.org/appengine": found meta tag get.metaImport{Prefix:"google.golang.org/appengine", VCS:"git", RepoRoot:"https://github.com/golang/appengine"} at https://google.golang.org/appengine?go-get=1
Parsing meta tags from https://gopkg.in/check.v1?go-get=1 (status code 200)
get "gopkg.in/check.v1": found meta tag get.metaImport{Prefix:"gopkg.in/check.v1", VCS:"git", RepoRoot:"https://gopkg.in/check.v1"} at https://gopkg.in/check.v1?go-get=1
go: finding github.com/prometheus/client_model latest
go: finding gopkg.in/tomb.v1 latest
Parsing meta tags from https://honnef.co/go/tools?go-get=1 (status code 200)
get "honnef.co/go/tools": found meta tag get.metaImport{Prefix:"honnef.co/go/tools", VCS:"git", RepoRoot:"https://github.com/dominikh/go-tools"} at https://honnef.co/go/tools?go-get=1
Fetching https://gopkg.in/robfig/cron.v2?go-get=1
Parsing meta tags from https://gopkg.in/robfig/cron.v2?go-get=1 (status code 200)
get "gopkg.in/robfig/cron.v2": found meta tag get.metaImport{Prefix:"gopkg.in/robfig/cron.v2", VCS:"git", RepoRoot:"https://gopkg.in/robfig/cron.v2"} at https://gopkg.in/robfig/cron.v2?go-get=1
go: finding gopkg.in/check.v1 latest
Fetching https://google.golang.org/api?go-get=1
go: finding github.com/shurcooL/githubv4 latest
Fetching https://vbom.ml/util?go-get=1
Parsing meta tags from https://google.golang.org/api?go-get=1 (status code 200)
get "google.golang.org/api": found meta tag get.metaImport{Prefix:"google.golang.org/api", VCS:"git", RepoRoot:"https://code.googlesource.com/google-api-go-client"} at https://google.golang.org/api?go-get=1
go: finding github.com/andygrunwald/go-gerrit latest
Fetching https://gopkg.in/resty.v1?go-get=1
go: finding gopkg.in/robfig/cron.v2 latest
Parsing meta tags from https://gopkg.in/resty.v1?go-get=1 (status code 200)
get "gopkg.in/resty.v1": found meta tag get.metaImport{Prefix:"gopkg.in/resty.v1", VCS:"git", RepoRoot:"https://gopkg.in/resty.v1"} at https://gopkg.in/resty.v1?go-get=1
Parsing meta tags from https://vbom.ml/util?go-get=1 (status code 200)
get "vbom.ml/util": found meta tag get.metaImport{Prefix:"vbom.ml/util", VCS:"git", RepoRoot:"https://github.com/fvbommel/util"} at https://vbom.ml/util?go-get=1
go: finding github.com/mailru/easyjson latest
Fetching https://k8s.io/client-go?go-get=1
Fetching https://sigs.k8s.io/testing_frameworks?go-get=1
go: finding vbom.ml/util latest
Parsing meta tags from https://k8s.io/client-go?go-get=1 (status code 200)
get "k8s.io/client-go": found meta tag get.metaImport{Prefix:"k8s.io/client-go", VCS:"git", RepoRoot:"https://github.com/kubernetes/client-go"} at https://k8s.io/client-go?go-get=1
Parsing meta tags from https://sigs.k8s.io/testing_frameworks?go-get=1 (status code 200)
get "sigs.k8s.io/testing_frameworks": found meta tag get.metaImport{Prefix:"sigs.k8s.io/testing_frameworks", VCS:"git", RepoRoot:"https://github.com/kubernetes-sigs/testing_frameworks"} at https://sigs.k8s.io/testing_frameworks?go-get=1
go: finding github.com/alecthomas/units latest
go: finding github.com/mitchellh/ioprogress latest
Fetching https://golang.org/x/xerrors?go-get=1
Parsing meta tags from https://golang.org/x/xerrors?go-get=1 (status code 200)
get "golang.org/x/xerrors": found meta tag get.metaImport{Prefix:"golang.org/x/xerrors", VCS:"git", RepoRoot:"https://go.googlesource.com/xerrors"} at https://golang.org/x/xerrors?go-get=1
go: finding github.com/coreos/pkg latest
go: finding github.com/PuerkitoBio/urlesc latest
Fetching https://gomodules.xyz/jsonpatch/v2?go-get=1
go: finding golang.org/x/xerrors latest
Fetching https://gopkg.in/gemnasium/logrus-airbrake-hook.v2?go-get=1
Fetching https://golang.org/x/time?go-get=1
Parsing meta tags from https://golang.org/x/time?go-get=1 (status code 200)
get "golang.org/x/time": found meta tag get.metaImport{Prefix:"golang.org/x/time", VCS:"git", RepoRoot:"https://go.googlesource.com/time"} at https://golang.org/x/time?go-get=1
Parsing meta tags from https://gomodules.xyz/jsonpatch/v2?go-get=1 (status code 200)
get "gomodules.xyz/jsonpatch/v2": found meta tag get.metaImport{Prefix:"gomodules.xyz/jsonpatch", VCS:"git", RepoRoot:"https://github.com/gomodules/jsonpatch"} at https://gomodules.xyz/jsonpatch/v2?go-get=1
get "gomodules.xyz/jsonpatch/v2": verifying non-authoritative meta tag
Fetching https://gomodules.xyz/jsonpatch?go-get=1
Parsing meta tags from https://gopkg.in/gemnasium/logrus-airbrake-hook.v2?go-get=1 (status code 200)
get "gopkg.in/gemnasium/logrus-airbrake-hook.v2": found meta tag get.metaImport{Prefix:"gopkg.in/gemnasium/logrus-airbrake-hook.v2", VCS:"git", RepoRoot:"https://gopkg.in/gemnasium/logrus-airbrake-hook.v2"} at https://gopkg.in/gemnasium/logrus-airbrake-hook.v2?go-get=1
Parsing meta tags from https://gomodules.xyz/jsonpatch?go-get=1 (status code 200)
go: finding github.com/mwitkow/go-conntrack latest
Fetching https://gonum.org/v1/netlib?go-get=1
go: finding golang.org/x/time latest
Parsing meta tags from https://gonum.org/v1/netlib?go-get=1 (status code 404)
get "gonum.org/v1/netlib": found meta tag get.metaImport{Prefix:"gonum.org/v1/netlib", VCS:"git", RepoRoot:"https://github.com/gonum/netlib"} at https://gonum.org/v1/netlib?go-get=1
Fetching https://gopkg.in/yaml.v2?go-get=1
Parsing meta tags from https://gopkg.in/yaml.v2?go-get=1 (status code 200)
get "gopkg.in/yaml.v2": found meta tag get.metaImport{Prefix:"gopkg.in/yaml.v2", VCS:"git", RepoRoot:"https://gopkg.in/yaml.v2"} at https://gopkg.in/yaml.v2?go-get=1
go: finding gonum.org/v1/netlib latest
Fetching https://golang.org/x/exp?go-get=1
Parsing meta tags from https://golang.org/x/exp?go-get=1 (status code 200)
get "golang.org/x/exp": found meta tag get.metaImport{Prefix:"golang.org/x/exp", VCS:"git", RepoRoot:"https://go.googlesource.com/exp"} at https://golang.org/x/exp?go-get=1
Fetching https://gopkg.in/airbrake/gobrake.v2?go-get=1
Fetching https://k8s.io/klog?go-get=1
Fetching https://k8s.io/kube-openapi?go-get=1
Parsing meta tags from https://k8s.io/klog?go-get=1 (status code 200)
get "k8s.io/klog": found meta tag get.metaImport{Prefix:"k8s.io/klog", VCS:"git", RepoRoot:"https://github.com/kubernetes/klog"} at https://k8s.io/klog?go-get=1
Parsing meta tags from https://gopkg.in/airbrake/gobrake.v2?go-get=1 (status code 200)
get "gopkg.in/airbrake/gobrake.v2": found meta tag get.metaImport{Prefix:"gopkg.in/airbrake/gobrake.v2", VCS:"git", RepoRoot:"https://gopkg.in/airbrake/gobrake.v2"} at https://gopkg.in/airbrake/gobrake.v2?go-get=1
go: finding github.com/google/go-containerregistry latest
Fetching https://gopkg.in/cheggaaa/pb.v1?go-get=1
Parsing meta tags from https://k8s.io/kube-openapi?go-get=1 (status code 200)
get "k8s.io/kube-openapi": found meta tag get.metaImport{Prefix:"k8s.io/kube-openapi", VCS:"git", RepoRoot:"https://github.com/kubernetes/kube-openapi"} at https://k8s.io/kube-openapi?go-get=1
Parsing meta tags from https://gopkg.in/cheggaaa/pb.v1?go-get=1 (status code 200)
get "gopkg.in/cheggaaa/pb.v1": found meta tag get.metaImport{Prefix:"gopkg.in/cheggaaa/pb.v1", VCS:"git", RepoRoot:"https://gopkg.in/cheggaaa/pb.v1"} at https://gopkg.in/cheggaaa/pb.v1?go-get=1
go: finding github.com/armon/consul-api latest
go: finding golang.org/x/exp latest
go: finding k8s.io/kube-openapi latest
Fetching https://cloud.google.com/go?go-get=1
Fetching https://modernc.org/xc?go-get=1
Parsing meta tags from https://modernc.org/xc?go-get=1 (status code 200)
get "modernc.org/xc": found meta tag get.metaImport{Prefix:"modernc.org/xc", VCS:"git", RepoRoot:"https://gitlab.com/cznic/xc"} at https://modernc.org/xc?go-get=1
Parsing meta tags from https://cloud.google.com/go?go-get=1 (status code 200)
get "cloud.google.com/go": found meta tag get.metaImport{Prefix:"cloud.google.com/go", VCS:"git", RepoRoot:"https://code.googlesource.com/gocloud"} at https://cloud.google.com/go?go-get=1
go: finding github.com/BurntSushi/xgb latest
go: finding k8s.io/client-go v2.0.0-alpha.0.0.20190112054256-b831b8de7155+incompatible
go: finding github.com/coreos/go-systemd latest
go: finding github.com/elazarl/goproxy latest
Fetching https://modernc.org/mathutil?go-get=1
Parsing meta tags from https://modernc.org/mathutil?go-get=1 (status code 200)
get "modernc.org/mathutil": found meta tag get.metaImport{Prefix:"modernc.org/mathutil", VCS:"git", RepoRoot:"https://gitlab.com/cznic/mathutil"} at https://modernc.org/mathutil?go-get=1
Fetching https://golang.org/x/text?go-get=1
Parsing meta tags from https://golang.org/x/text?go-get=1 (status code 200)
get "golang.org/x/text": found meta tag get.metaImport{Prefix:"golang.org/x/text", VCS:"git", RepoRoot:"https://go.googlesource.com/text"} at https://golang.org/x/text?go-get=1
Fetching https://go.etcd.io/bbolt?go-get=1
Parsing meta tags from https://go.etcd.io/bbolt?go-get=1 (status code 200)
get "go.etcd.io/bbolt": found meta tag get.metaImport{Prefix:"go.etcd.io/bbolt", VCS:"git", RepoRoot:"https://github.com/etcd-io/bbolt"} at https://go.etcd.io/bbolt?go-get=1
Fetching https://golang.org/x/image?go-get=1
Parsing meta tags from https://golang.org/x/image?go-get=1 (status code 200)
get "golang.org/x/image": found meta tag get.metaImport{Prefix:"golang.org/x/image", VCS:"git", RepoRoot:"https://go.googlesource.com/image"} at https://golang.org/x/image?go-get=1
Fetching https://modernc.org/strutil?go-get=1
Parsing meta tags from https://modernc.org/strutil?go-get=1 (status code 200)
get "modernc.org/strutil": found meta tag get.metaImport{Prefix:"modernc.org/strutil", VCS:"git", RepoRoot:"https://gitlab.com/cznic/strutil"} at https://modernc.org/strutil?go-get=1
Fetching https://modernc.org/cc?go-get=1
Fetching https://golang.org/x/oauth2?go-get=1
go: finding k8s.io/apimachinery v0.0.0-20190111195121-fa6ddc151d63
go: finding github.com/xiang90/probing latest
Parsing meta tags from https://golang.org/x/oauth2?go-get=1 (status code 200)
get "golang.org/x/oauth2": found meta tag get.metaImport{Prefix:"golang.org/x/oauth2", VCS:"git", RepoRoot:"https://go.googlesource.com/oauth2"} at https://golang.org/x/oauth2?go-get=1
Fetching https://sigs.k8s.io/yaml?go-get=1
Parsing meta tags from https://modernc.org/cc?go-get=1 (status code 200)
get "modernc.org/cc": found meta tag get.metaImport{Prefix:"modernc.org/cc", VCS:"git", RepoRoot:"https://gitlab.com/cznic/cc"} at https://modernc.org/cc?go-get=1
Parsing meta tags from https://sigs.k8s.io/yaml?go-get=1 (status code 200)
get "sigs.k8s.io/yaml": found meta tag get.metaImport{Prefix:"sigs.k8s.io/yaml", VCS:"git", RepoRoot:"https://github.com/kubernetes-sigs/yaml"} at https://sigs.k8s.io/yaml?go-get=1
go: finding github.com/bazelbuild/buildtools latest
go: finding github.com/kr/logfmt latest
go: finding golang.org/x/image latest
Fetching https://contrib.go.opencensus.io/exporter/ocagent?go-get=1
go: finding golang.org/x/oauth2 latest
Parsing meta tags from https://contrib.go.opencensus.io/exporter/ocagent?go-get=1 (status code 200)
get "contrib.go.opencensus.io/exporter/ocagent": found meta tag get.metaImport{Prefix:"contrib.go.opencensus.io/exporter/ocagent", VCS:"git", RepoRoot:"https://github.com/census-ecosystem/opencensus-go-exporter-ocagent"} at https://contrib.go.opencensus.io/exporter/ocagent?go-get=1
go: finding github.com/streadway/amqp latest
go: finding github.com/jstemmer/go-junit-report latest
go: finding github.com/erikstmartin/go-testdb latest
Fetching https://golang.org/x/mobile?go-get=1
Parsing meta tags from https://golang.org/x/mobile?go-get=1 (status code 200)
get "golang.org/x/mobile": found meta tag get.metaImport{Prefix:"golang.org/x/mobile", VCS:"git", RepoRoot:"https://go.googlesource.com/mobile"} at https://golang.org/x/mobile?go-get=1
go: finding github.com/mxk/go-flowrate latest
Fetching https://sigs.k8s.io/structured-merge-diff?go-get=1
Parsing meta tags from https://sigs.k8s.io/structured-merge-diff?go-get=1 (status code 200)
get "sigs.k8s.io/structured-merge-diff": found meta tag get.metaImport{Prefix:"sigs.k8s.io/structured-merge-diff", VCS:"git", RepoRoot:"https://github.com/kubernetes-sigs/structured-merge-diff"} at https://sigs.k8s.io/structured-merge-diff?go-get=1
Fetching https://gonum.org/v1/gonum?go-get=1
go: finding github.com/munnerz/goautoneg latest
Parsing meta tags from https://gonum.org/v1/gonum?go-get=1 (status code 404)
get "gonum.org/v1/gonum": found meta tag get.metaImport{Prefix:"gonum.org/v1/gonum", VCS:"git", RepoRoot:"https://github.com/gonum/gonum"} at https://gonum.org/v1/gonum?go-get=1
Fetching https://istio.io/gogo-genproto?go-get=1
go: finding k8s.io/apimachinery v0.0.0-20190802060556-6fa4771c83b3
Fetching https://k8s.io/apiextensions-apiserver?go-get=1
go: finding github.com/docker/spdystream latest
Parsing meta tags from https://k8s.io/apiextensions-apiserver?go-get=1 (status code 200)
get "k8s.io/apiextensions-apiserver": found meta tag get.metaImport{Prefix:"k8s.io/apiextensions-apiserver", VCS:"git", RepoRoot:"https://github.com/kubernetes/apiextensions-apiserver"} at https://k8s.io/apiextensions-apiserver?go-get=1
Fetching https://golang.org/x/mod?go-get=1
go: finding golang.org/x/mobile latest
Parsing meta tags from https://golang.org/x/mod?go-get=1 (status code 200)
get "golang.org/x/mod": found meta tag get.metaImport{Prefix:"golang.org/x/mod", VCS:"git", RepoRoot:"https://go.googlesource.com/mod"} at https://golang.org/x/mod?go-get=1
Parsing meta tags from https://istio.io/gogo-genproto?go-get=1 (status code 200)
get "istio.io/gogo-genproto": found meta tag get.metaImport{Prefix:"istio.io/gogo-genproto", VCS:"git", RepoRoot:"https://github.com/istio/gogo-genproto"} at https://istio.io/gogo-genproto?go-get=1
Fetching https://gopkg.in/jcmturner/gokrb5.v7?go-get=1
go: finding sigs.k8s.io/structured-merge-diff latest
go get: upgrading modernc.org/cc@v1.0.0: git fetch -f https://gitlab.com/cznic/cc refs/tags/v2.0.0:refs/tags/v2.0.0 in /go/pkg/mod/cache/vcs/3dac616a9d80602010c4792ef9c0e9d9812a1be8e70453e437e9792978075db6: exit status 128:
	error: RPC failed; result=22, HTTP code = 404
	fatal: The remote end hung up unexpectedly
Parsing meta tags from https://gopkg.in/jcmturner/gokrb5.v7?go-get=1 (status code 200)
get "gopkg.in/jcmturner/gokrb5.v7": found meta tag get.metaImport{Prefix:"gopkg.in/jcmturner/gokrb5.v7", VCS:"git", RepoRoot:"https://gopkg.in/jcmturner/gokrb5.v7"} at https://gopkg.in/jcmturner/gokrb5.v7?go-get=1
go: finding gonum.org/v1/gonum latest
go: finding github.com/golang/lint latest
go: finding k8s.io/apiextensions-apiserver latest
Fetching https://modernc.org/golex?go-get=1
Fetching https://gopkg.in/jcmturner/rpc.v1?go-get=1
go: finding istio.io/gogo-genproto latest
Parsing meta tags from https://modernc.org/golex?go-get=1 (status code 200)
get "modernc.org/golex": found meta tag get.metaImport{Prefix:"modernc.org/golex", VCS:"git", RepoRoot:"https://gitlab.com/cznic/golex"} at https://modernc.org/golex?go-get=1
Parsing meta tags from https://gopkg.in/jcmturner/rpc.v1?go-get=1 (status code 200)
get "gopkg.in/jcmturner/rpc.v1": found meta tag get.metaImport{Prefix:"gopkg.in/jcmturner/rpc.v1", VCS:"git", RepoRoot:"https://gopkg.in/jcmturner/rpc.v1"} at https://gopkg.in/jcmturner/rpc.v1?go-get=1
go: finding github.com/xdg/scram latest
Fetching https://gopkg.in/jcmturner/aescts.v1?go-get=1
Parsing meta tags from https://gopkg.in/jcmturner/aescts.v1?go-get=1 (status code 200)
get "gopkg.in/jcmturner/aescts.v1": found meta tag get.metaImport{Prefix:"gopkg.in/jcmturner/aescts.v1", VCS:"git", RepoRoot:"https://gopkg.in/jcmturner/aescts.v1"} at https://gopkg.in/jcmturner/aescts.v1?go-get=1
Fetching https://rsc.io/binaryregexp?go-get=1
Fetching https://k8s.io/kubernetes?go-get=1
Parsing meta tags from https://k8s.io/kubernetes?go-get=1 (status code 200)
get "k8s.io/kubernetes": found meta tag get.metaImport{Prefix:"k8s.io/kubernetes", VCS:"git", RepoRoot:"https://github.com/kubernetes/kubernetes"} at https://k8s.io/kubernetes?go-get=1
Fetching https://gonum.org/v1/plot?go-get=1
Parsing meta tags from https://gonum.org/v1/plot?go-get=1 (status code 404)
get "gonum.org/v1/plot": found meta tag get.metaImport{Prefix:"gonum.org/v1/plot", VCS:"git", RepoRoot:"https://github.com/gonum/plot"} at https://gonum.org/v1/plot?go-get=1
Parsing meta tags from https://rsc.io/binaryregexp?go-get=1 (status code 200)
get "rsc.io/binaryregexp": found meta tag get.metaImport{Prefix:"rsc.io/binaryregexp", VCS:"git", RepoRoot:"https://github.com/rsc/binaryregexp"} at https://rsc.io/binaryregexp?go-get=1
Fetching https://gopkg.in/jcmturner/dnsutils.v1?go-get=1
Parsing meta tags from https://gopkg.in/jcmturner/dnsutils.v1?go-get=1 (status code 200)
get "gopkg.in/jcmturner/dnsutils.v1": found meta tag get.metaImport{Prefix:"gopkg.in/jcmturner/dnsutils.v1", VCS:"git", RepoRoot:"https://gopkg.in/jcmturner/dnsutils.v1"} at https://gopkg.in/jcmturner/dnsutils.v1?go-get=1
go: finding gonum.org/v1/plot latest
go: finding github.com/census-instrumentation/opencensus-proto v0.1.0-0.20181214143942-ba49f56771b8
Fetching https://rsc.io/pdf?go-get=1
Parsing meta tags from https://rsc.io/pdf?go-get=1 (status code 200)
get "rsc.io/pdf": found meta tag get.metaImport{Prefix:"rsc.io/pdf", VCS:"git", RepoRoot:"https://github.com/rsc/pdf"} at https://rsc.io/pdf?go-get=1
go: finding github.com/golang/freetype latest
go: github.com/golang/lint@v0.0.0-20190409202823-959b441ac422: parsing go.mod: unexpected module path "golang.org/x/lint"
go get: error loading module requirements


```