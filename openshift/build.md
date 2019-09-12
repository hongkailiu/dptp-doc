# build

* [docker.image.best.practice@atomic](http://www.projectatomic.io/docs/docker-image-author-guidance/)
* [creating_images@oc](https://docs.openshift.com/container-platform/3.11/creating_images/index.html) and [managing-images@oc](https://docs.openshift.com/container-platform/3.11/dev_guide/managing_images.html#dev-guide-managing-images)
* [builds_and_image_streams@oc](https://docs.openshift.com/container-platform/3.11/architecture/core_concepts/builds_and_image_streams.html) and [builds@oc](https://docs.openshift.com/container-platform/3.11/dev_guide/builds/index.html)
* [build@svt-doc](https://github.com/hongkailiu/svt-case-doc/blob/master/learn/build.md) and [is@svt-doc](https://github.com/hongkailiu/svt-case-doc/blob/master/learn/image_stream.md)

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
