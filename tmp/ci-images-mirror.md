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

* failures of `oc-image-mirror` per day

  * with retries
  * without retires
 
* a


