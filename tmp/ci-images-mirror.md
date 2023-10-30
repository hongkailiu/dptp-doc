# ci-images-mirror

## Prometheus queries

* workqueue depth: how fast/slow the events are reconciled: 13k after restart

> workqueue_depth{namespace="ci",name="quay_io_ci_images_distributor"}

* mirror queue depth:

## CloudWatch

* images to mirror per day: 100k

```
fields datefloor(@timestamp, 24h) as date
| filter(component="ci-images-mirror" and msg="Mirroring ...")
| stats count(*) as c by date
| sort date desc
| limit 20
```

* failures of `oc-image-mirror` per day

  * with retries
  * without retires
 
* a


