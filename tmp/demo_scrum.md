# demo: Sep. 29

- I complaint of the complexity of manipulating the kubeconfig file in [oc_sa_create_kubeconfig.sh](https://github.com/openshift/ci-tools/blob/master/images/ci-secret-generator/oc_sa_create_kubeconfig.sh) whenever a new token is requested.
- David [suggested](https://issues.redhat.com/browse/DPTP-3087?focusedCommentId=20919808&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-20919808) to link a [tokenFile](https://github.com/kubernetes/kubernetes/blob/f9afd68e3b3fc05f3607ea7cb90808c3e931ba9c/staging/src/k8s.io/client-go/tools/clientcmd/api/v1/types.go#L113-L115) in the kubeconfig and then the kuebconfig file is static and we need only to refresh the tokenFile.
- Example: `sprint-automation`: 
  - [ci-secret-generator](https://github.com/openshift/release/blob/5b786ff19b610e3f36566c274f7871ddc178efb5/core-services/ci-secret-generator/_config.yaml#L162-L172)
  - [ci-secret-bootstrap](https://github.com/openshift/release/blob/5b786ff19b610e3f36566c274f7871ddc178efb5/core-services/ci-secret-bootstrap/_config.yaml#L2316-L2332)

- the upstream support of [kubeconfig-suffix](https://github.com/kubernetes/test-infra/pull/27436) and [application to CI producction](https://github.com/openshift/release/pull/32421)
- the new script [oc_create_kubeconfig.sh](https://github.com/openshift/ci-tools/blob/master/images/ci-secret-generator/oc_create_kubeconfig.sh)
- a new requirement of build-farm: [The api-server has to use CA trusted certificates](https://github.com/openshift/release/blob/master/clusters/JoinBuildFarm.md#set-up-applyconfig-against-the-cluster). Handled vsphere [SPLAT-720](https://issues.redhat.com/browse/SPLAT-720).
- ongoing work:
  - release-controller/ci-chat-bot [release/pull/32621](https://github.com/openshift/release/pull/32621) 
  - prow and ci-tools [release/pull/32642](https://github.com/openshift/release/pull/32642)
  - adpotion in cluster-init [DPTP-3152](https://issues.redhat.com/browse/DPTP-3152)

# demo: Nov. 12

* PostSubmits are on `build02`: [sanitize-prow-jobs/_config.yaml](https://github.com/openshift/release/blob/01c5a7e911ec3500564e09c206182373212443b0/core-services/sanitize-prow-jobs/_config.yaml#L1624-L1626)
* [promotion jobs](https://prow.ci.openshift.org/?job=branch-*-images) is implemented by running `oc-image-mirror` in a [pod](https://prow.ci.openshift.org/view/gs/origin-ci-test/logs/branch-ci-codeready-toolchain-host-operator-master-images/1326588620701700096#1:build-log.txt%3A27).

# demo: July 09

Vanity URLs: E.g., https://search.ci.openshift.org/

[DSN set up on GCP](https://console.cloud.google.com/net-services/dns/zones?project=openshift-ci-infra&authuser=1&organizationId=54643501348&dnsManagedZonessize=50): `A` or `CNAME` record

> oc get svc -n openshift-ingress router-default 

Cert-Manager (app.ci, build0{1|2}): [search_ingress.yaml](https://github.com/openshift/release/blob/master/clusters/app.ci/cert-manager/search_ingress.yaml)

* Route: Not first class citizen of cert-manager
* Ingress: support only `termination: edge`

[Application awareness](https://issues.redhat.com/browse/DPTP-1166?focusedCommentId=14167463&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-14167463):

* apps-subdomain, api-server and registry: supported
* console (4.5+) and openshit-monitoring (not supported yet)

Alert on probes and certificates for [all targets in blackbox-exporter](https://github.com/openshift/release/blob/master/clusters/app.ci/prow-monitoring/additional-scrape-configs_secret.yaml)

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
