# build

* [docker.image.best.practice@atomic](http://www.projectatomic.io/docs/docker-image-author-guidance/)
* [creating_images@oc](https://docs.openshift.com/container-platform/3.11/creating_images/index.html) and [managing-images@oc](https://docs.openshift.com/container-platform/3.11/dev_guide/managing_images.html#dev-guide-managing-images)
* [builds_and_image_streams@oc](https://docs.openshift.com/container-platform/3.11/architecture/core_concepts/builds_and_image_streams.html) and [builds@oc](https://docs.openshift.com/container-platform/3.11/dev_guide/builds/index.html)
* [build@svt-doc](https://github.com/hongkailiu/svt-case-doc/blob/master/learn/build.md) and [is@svt-doc](https://github.com/hongkailiu/svt-case-doc/blob/master/learn/image_stream.md)
* [s2i@oc](https://docs.openshift.com/container-platform/3.11/creating_images/s2i.html), [s2i_testing](https://docs.openshift.com/container-platform/3.11/creating_images/s2i_testing.html): the key is the S2I Image (used in the `bc.spec.strategy.sourceStrategy.from` of `bc`)

## bc

Use `yaml` files in test-go repo:

```
$ git clone https://github.com/hongkailiu/test-go.git
$ cd test-go
```

Create `bc` and start-build:

```
$ oc apply -n hongkliu-test -f ./openshift-assets/test-go_bc.yaml
$ oc get bc
NAME                       TYPE      FROM      LATEST
test-go-build-dockerfile   Docker    Git       2
###create `is` the build pushes image to
$ oc create is ci-staging
$ oc start-build test-go-build-dockerfile 
$ oc get build
NAME                         TYPE      FROM          STATUS     STARTED         DURATION
test-go-build-dockerfile-2   Docker    Git@77c4fe4   Complete   5 minutes ago   1m58s
### build logs is the logs from the build pod
$ oc logs build/test-go-build-dockerfile-2 -f
$ oc get pod
NAME                               READY     STATUS      RESTARTS   AGE
test-go-build-dockerfile-2-build   0/1       Completed   0          5m
$ oc get is ci-staging -o json | jq -r .status.tags[].tag
testctl-bc

### podman login for both registries
$ skopeo copy docker://registry.svc.ci.openshift.org/hongkliu-test/ci-staging:testctl-bc docker://quay.io/hongkailiu/ci-staging:testctl-bc

$ skopeo inspect docker://quay.io/hongkailiu/ci-staging:testctl-bc

```

If we do not have the multi-stage in the Dockerfile, we could use [chaining-builds](https://docs.openshift.com/container-platform/3.11/dev_guide/builds/advanced_build_operations.html#dev-guide-chaining-builds) to achieve the same goal.

## s2i

```
###https://blog.openshift.com/create-s2i-builder-image/
$ cd ~/bin
$ wget https://github.com/openshift/source-to-image/releases/download/v1.1.14/source-to-image-v1.1.14-874754de-linux-amd64.tar.gz
$ tar -xvf source-to-image-v1.1.14-874754de-linux-amd64.tar.gz

$ cd ~/test-go
$ s2i create docker.io/golang:1.12 s2i-test-go
### editing ...
$ make -C s2i-test-go/ build
$ buildah push quay.io/hongkailiu/test-go:s2i-1.0.0
$ buildah push --creds=hongkailiu quay.io/hongkailiu/test-go:s2i-1.0.0

### test locally
$ podman run --entrypoint "/bin/bash" -it --rm quay.io/hongkailiu/test-go:s2i-1.0.0
1001@ceb36659f5e0:~$ ls /usr/local/s2i/
assemble  run  save-artifacts  usage
1001@ceb36659f5e0:~$ tar --version
tar (GNU tar) 1.30
...
1001@ceb36659f5e0:~$ which sh
/bin/sh

```

Use the build image in a `bc`:

```
$ oc create is ci-staging
imagestream.image.openshift.io/ci-staging created
$ cd ~/test-go
$ oc apply -f ./deploy/testctl_http/test-go_bc.yaml 
buildconfig.build.openshift.io/test-go-build-s2i created
$ oc get bc test-go-build-s2i
NAME                TYPE      FROM      LATEST
test-go-build-s2i   Source    Git       0
$ oc start-build test-go-build-s2i 
build.build.openshift.io/test-go-build-s2i-1 started
$ oc get build
NAME                  TYPE      FROM          STATUS    STARTED          DURATION
test-go-build-s2i-1   Source    Git@9c76b0d   Running   58 seconds ago   
$ oc logs build/test-go-build-s2i-1
### OOM now
### TODO since the production is image is from another base: alpine
### we need another build-image, and then copy bin from first one
### https://docs.openshift.com/container-platform/3.11/dev_guide/builds/build_inputs.html#image-source
### All of this would not be necessary if dockerStrategy is allowed on openshift-online
```

TODO: incremental build, artifacts
