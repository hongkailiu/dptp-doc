# TODOs for prow-monitoring stack

## need confirmation

### Route protection from the public access

* oauth-proxy is added as an additional container into prometheus/alert-manager pods.
    * http ports for prometheus and alert-manager are still open in `svc` and used only for internal communication.
    * routes only proxy https ports.

Qs:

* how to communication an oauth-proxied port? Not related to Prom.-Opr. I saw that more certificates injected via secret while sometimes an `internal` user (eg between grafana and prometheus) is used.
* neither `label-proxy` nor `kube-rbac-proxy` is used. Is this OK? (kind of confirmed by _Lucas Serven_ via slack)

## need suggestion


* PVC as Storage (avoiding data lost when recreating the crds): I saw [storageSpec](https://github.com/coreos/prometheus-operator/blob/master/pkg/apis/monitoring/v1/types.go#L285). Example and doc would be nice. Which version of prom.-opr? We have `quay.io/coreos/prometheus-operator:v0.29.0` right now deployed on OCP 311.
* HA (avoiding downtime when updating config or version): 
    * [prometheus and alert-manager should be HA already out of the box](https://coreos.com/operators/prometheus/docs/latest/high-availability.html).
    The status of shading implementation?
    * grafana: via [helm](https://github.com/helm/charts/tree/master/stable/grafana)? Convert it into an opr? 
        * sidecar: config-reloader.
        * ha: replica