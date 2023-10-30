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
 



