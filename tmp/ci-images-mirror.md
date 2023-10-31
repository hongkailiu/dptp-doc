# ci-images-mirror

## Prometheus queries

* workqueue depth: how fast/slow the events are reconciled: 13k after restart

> workqueue_depth{namespace="ci",name="quay_io_ci_images_distributor"}

* mirror queue depth:

## CloudWatch

* images to mirror per day:

```
fields datefloor(@timestamp, 24h) as date
| filter(component="ci-images-mirror" and msg="Mirroring")
| stats count(*) as c by date
| sort date desc
| limit 20
```

The corresponding [code](https://github.com/openshift/ci-tools/blob/4ef739fd69dc672de7673fb984d273064e9f27b4/pkg/controller/quay_io_ci_images_distributor/quay_io_ci_images_distributor.go#L178) in the src.

* `msg="Image is up to date"`: images up to date from [code](https://github.com/openshift/ci-tools/blob/e5683bf2bb5b3d11e15f37905e7d72d30bdb8e58/pkg/controller/quay_io_ci_images_distributor/quay_io_ci_images_distributor.go#L197)

* `msg="Mirroring ..."`: `oc-image-mirror` per day from [code](https://github.com/openshift/ci-tools/blob/e5683bf2bb5b3d11e15f37905e7d72d30bdb8e58/pkg/controller/quay_io_ci_images_distributor/oc_quay_io_image_helper.go#L127)

* `msg="Mirrored successfully"`: successes of `oc-image-mirror` per day from [code](https://github.com/openshift/ci-tools/blob/e5683bf2bb5b3d11e15f37905e7d72d30bdb8e58/pkg/controller/quay_io_ci_images_distributor/oc_quay_io_image_helper.go#L138)

* failures of `oc-image-mirror` per day

  * `msg="Failed to mirror"`: with retries from [code](https://github.com/openshift/ci-tools/blob/e5683bf2bb5b3d11e15f37905e7d72d30bdb8e58/pkg/controller/quay_io_ci_images_distributor/oc_quay_io_image_helper.go#L135)
  * `msg="Failed to mirror even with retries"`: without retires from [code](https://github.com/openshift/ci-tools/blob/e5683bf2bb5b3d11e15f37905e7d72d30bdb8e58/pkg/controller/quay_io_ci_images_distributor/mirror.go#L116)
 

## Errors

```
fields @timestamp,msg, @message, @logStream, @log
| filter(component="ci-images-mirror" and msg="Running command failed." and (args like /image mirror.*/))
| sort @timestamp desc 
| limit 20
```

> oc -n ci extract secret/registry-push-credentials-ci-images-mirror --to=- | jq > /tmp/p.c

### schema version 1

```console
$ oc image mirror --keep-manifest-list --registry-config=/tmp/p.c --continue-on-error=true --max-per-registry=20 --dry-run=false registry.ci.openshift.org/openshift/release@sha256:09e51ff46de9707cab1d34b1c0d3ee40388f610de21ce30b51153a26c70473b7=quay.io/openshift/ci:openshift_release_tectonic-console-builder-v19 
...
I1030 18:22:12.293011   72990 manifest.go:550] warning: Digests are not preserved with schema version 1 images. Support for schema version 1 images will be removed in a future release
...

$ oc image info registry.ci.openshift.org/openshift/release@sha256:09e51ff46de9707cab1d34b1c0d3ee40388f610de21ce30b51153a26c70473b7 -o json -a /tmp/p.c | jq -r '.mediaType'
application/vnd.docker.distribution.manifest.v1+prettyjws

$ oc image info registry.ci.openshift.org/openshift/release@sha256:09e51ff46de9707cab1d34b1c0d3ee40388f610de21ce30b51153a26c70473b7 -o json -a /tmp/p.c | jq -r '.digest'
sha256:09e51ff46de9707cab1d34b1c0d3ee40388f610de21ce30b51153a26c70473b7
$ oc image info quay.io/openshift/ci:openshift_release_tectonic-console-builder-v19 -o json -a /tmp/p.c | jq -r '.digest'
sha256:a97051f6ee6c5372c7bee11f6eda922d01351028c24f90273e4662b9dbb87ad3

$ oc image info registry.ci.openshift.org/openshift/release@sha256:09e51ff46de9707cab1d34b1c0d3ee40388f610de21ce30b51153a26c70473b7 -o json -a /tmp/p.c | jq -r '.config.created'
2020-01-17T14:58:27.4844326Z
```

### unknown blob

```console
$ oc image mirror --keep-manifest-list --registry-config=/tmp/p.c --continue-on-error=true --max-per-registry=20 --dry-run=false registry.ci.openshift.org/ci/namespace-ttl-controller@sha256:cfd40eaa6282ae5cc93d87f74f7fa9af9459be7b497cb0c334f4408b81a5142f=quay.io/openshift/ci:20231030_sha256_cfd40eaa6282ae5cc93d87f74f7fa9af9459be7b497cb0c334f4408b81a5142f
...
error: unable to open source layer sha256:e30853ed228ffef1bb93a5ead95e0002eb7ad6eba0178d30da4585d1d10aa5df to copy to quay.io/openshift/ci: unknown blob
error: unable to push manifest to quay.io/openshift/ci:20231030_sha256_cfd40eaa6282ae5cc93d87f74f7fa9af9459be7b497cb0c334f4408b81a5142f: manifest invalid: manifest invalid
info: Mirroring completed in 650ms (0B/s)
error: one or more errors occurred

$ oc image info registry.ci.openshift.org/ci/namespace-ttl-controller@sha256:cfd40eaa6282ae5cc93d87f74f7fa9af9459be7b497cb0c334f4408b81a5142f -o json -a /tmp/p.c | jq -r '.config.created'
2020-10-21T12:00:48.051759197Z
```

We do not use `is/namespace-ttl-controller` any more which is from [build-config](https://github.com/openshift/ci-ns-ttl-controller/blob/f2f2470c99b91667604a7593601e21dd1add4b01/deploy/controller-build.yaml#L21C13-L21C37). The one in our production is from `is/ci-ns-ttl-controller`.

Backup and delete:

```console
$ oc --context app.ci get is namespace-ttl-controller -n ci > namespace-ttl-controller.is.yaml
$ oc --context app.ci delete is namespace-ttl-controller -n ci
imagestream.image.openshift.io "namespace-ttl-controller" deleted
```

Another broken image:

```
$ oc image mirror --keep-manifest-list --registry-config=/tmp/p.c --continue-on-error=true --max-per-registry=20 --dry-run=false registry.ci.openshift.org/openshift/ansible-runner@sha256:bd09ef403f2f90f2c6bd133d7533e939058903f69223c5f12557a49e3aed14bb

$ oc get is -n openshift ansible-runner -o yaml
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"image.openshift.io/v1","kind":"ImageStream","metadata":{"annotations":{},"name":"ansible-runner","namespace":"openshift"},"spec":{"tags":[{"from":{"kind":"DockerImage","name":"docker.io/ansible/ansible-runner:latest"},"importPolicy":{"scheduled":false},"name":"latest"}]}}
    openshift.io/image.dockerRepositoryCheck: "2021-06-03T16:24:42Z"
  creationTimestamp: "2020-05-29T13:52:00Z"
  generation: 3366
  name: ansible-runner
  namespace: openshift
  resourceVersion: "2932387480"
  uid: ff02b090-c77d-441a-a60c-d5a26de66300
spec:
  lookupPolicy:
    local: true
  tags:
  - annotations: null
    from:
      kind: DockerImage
      name: docker.io/ansible/ansible-runner:latest
    generation: 3365
    importPolicy:
      importMode: Legacy
    name: latest
    referencePolicy:
      type: Local
status:
  dockerImageRepository: image-registry.openshift-image-registry.svc:5000/openshift/ansible-runner
  publicDockerImageRepository: registry.ci.openshift.org/openshift/ansible-runner
  tags:
  - conditions:
    - generation: 3365
      lastTransitionTime: "2021-06-03T16:24:42Z"
      message: 'Internal error occurred: docker.io/ansible/ansible-runner:latest:
        toomanyrequests: You have reached your pull rate limit. You may increase the
        limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit'
      reason: InternalError
      status: "False"
      type: ImportSuccess
    items:
    - created: "2020-06-02T11:50:06Z"
      dockerImageReference: docker.io/ansible/ansible-runner@sha256:bd09ef403f2f90f2c6bd133d7533e939058903f69223c5f12557a49e3aed14bb
      generation: 3364
      image: sha256:bd09ef403f2f90f2c6bd133d7533e939058903f69223c5f12557a49e3aed14bb
    tag: latest

$ oc get istag -n openshift ansible-runner:latest -o yaml
apiVersion: image.openshift.io/v1
conditions:
- generation: 3365
  lastTransitionTime: "2021-06-03T16:24:42Z"
  message: 'Internal error occurred: docker.io/ansible/ansible-runner:latest: toomanyrequests:
    You have reached your pull rate limit. You may increase the limit by authenticating
    and upgrading: https://www.docker.com/increase-rate-limit'
  reason: InternalError
  status: "False"
  type: ImportSuccess
generation: 3364
```
