# demo: July 09

Vanity URLs: E.g., https://search.ci.openshift.org/

DSN set up: `A` or `CNAME` record

> oc get svc -n openshift-ingress router-default 

Cert-Manager: [search_ingress.yaml](https://github.com/openshift/release/blob/master/clusters/app.ci/cert-manager/search_ingress.yaml)

* Route: Not first class citizen of cert-manager

* Ingress: support only `termination: reencryption`

* Application awareness: console (4.5+) and openshit-monitoring (not supported yet)

# demo: May 07

A `hidden` periodic [periodic-ci-secret-bootstrap](https://github.com/openshift/release/blob/8c7eb0a281ed46d42cc88a9ca29103025bb30531/ci-operator/jobs/infra-periodics.yaml#L1205-L1209) by a _Read-Only_ BitWarden user.

```
$ make job JOB=periodic-ci-secret-bootstrap
```

# demo: Apr. 16

yamls: [release/pull/7789](https://github.com/openshift/release/pull/7789)

```
oc --context build01 get pod -n api-audit-log
NAME                     READY   STATUS    RESTARTS   AGE
vector-audit-log-mmdkk   1/1     Running   0          11s
vector-audit-log-r8xtr   1/1     Running   0          11s
vector-audit-log-wznkz   1/1     Running   0          11s
```

aws cloudwatch console: https://openshift-ci-infra.signin.aws.amazon.com


# demo: Mar 04

* [periodic-ci-image-import-to-build01](https://prow.svc.ci.openshift.org/?job=periodic-ci-image-import-to-build01)

```bash
$ oc --context build01 get is -n ci ci-operator -o yaml | yq -r -y '.spec.tags'
- annotations: null
  from:
    kind: DockerImage
    name: registry.svc.ci.openshift.org/ci/ci-operator:latest
  generation: 120
  importPolicy:
    scheduled: true ### importing scheduled every 15 mins
  name: latest
  referencePolicy:
    type: Source
```

We do it more often (every minute) by [periodic-ci-image-import-to-build01](https://github.com/openshift/release/blob/c3a1d6906e21a1a80288dd1dc7528182127ea830/ci-operator/jobs/infra-periodics.yaml#L11).

* Prowjobs on [default](https://prometheus-k8s-openshift-monitoring.svc.ci.openshift.org/graph?g0.range_input=1w&g0.expr=count(kube_pod_info%7Bnamespace%3D~%22ci.*%22%7D)&g0.tab=0) and [build01](https://prometheus-k8s-openshift-monitoring.apps.build01.ci.devcluster.openshift.com/graph?g0.range_input=1w&g0.expr=count(kube_pod_info%7Bnamespace%3D~%22ci.*%22%7D)&g0.tab=0).

# demo: auto-tools: ci-secret-bootstrap

* populating secrets from BW-items to _default/build01_ clusters
* deprecating `ci-operator/populate-secrets-from-bitwarden.sh`: Not there yet. [config.yaml](https://github.com/openshift/release/blob/master/core-services/ci-secret-bootstrap/_config.yaml)
* detect secret inconsistency
* run:
    * config
    * bw user/pwd
    * kubeconfig with contexts named `build01` and `default`

> make kerberos_id=<your_kerberos_id> dry_run=true ci-secret-bootstrap

# demo: alert on job failures

* [routes](https://alertmanager-prow-monitoring.svc.ci.openshift.org/#/status) on alertmanager
    2 channels before: #ops-teamplatform, #build-cop-alerts; 1 more now: #forum-devex
* [labels](https://prometheus-prow-monitoring.svc.ci.openshift.org/alerts) on alerts for routing: `team: build-cop`
* alerts on job failures: [readme](https://github.com/openshift/release/tree/master/cluster/ci/monitoring#add-an-alert-on-prow-job-failures)


# demo: auto-tools

3 periodic jobs: [`bumper.UpdatePullRequest`](https://github.com/kubernetes/test-infra/blob/master/experiment/autobumper/bumper/bumper.go#L77)

* [periodic-prow-image-autobump](https://github.com/openshift/release/blob/master/ci-operator/jobs/infra-periodics.yaml#L287)
    * search the latest "Prow images" and "k8s-testimages" in gcr.io registry and modify image tags in files
    * commit and pr
* [periodic-prow-auto-owners](https://github.com/openshift/release/blob/master/ci-operator/jobs/infra-periodics.yaml#L366)
    * search the latest OWNERS and OWNERS_ALIASES in repos in `./ci-operator` and sync the content in them
    * ...
* [periodic-prow-auto-config-brancher](https://github.com/openshift/release/blob/master/ci-operator/jobs/infra-periodics.yaml#L326)
    * based on 3 release-tools `determinize-ci-operator`, `config-brancher`, and `ci-operator-prowgen`
    * ...

A job execution: 

* [auto-bumper-log](https://prow.svc.ci.openshift.org/view/gcs/origin-ci-test/logs/periodic-prow-image-autobump/35#0:build-log.txt%3A1)
* find a suitable [PR](https://github.com/openshift/release/pull/5130) or create a new one
