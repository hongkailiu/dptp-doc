# Nov 23: qci-appci

- a reverse-proxy for the image registry `quay.io/openshift/ci`: [qci-appci/README.md](https://github.com/openshift/ci-tools/blob/master/cmd/qci-appci/README.md)
- the face of CI registry: [ci-docs](https://docs.ci.openshift.org/docs/how-tos/use-registries-in-build-farm/#the-ci-image-repository-in-quayio-qci)
- access control delegated to RBACs on `app.ci`

![qci-appci (1)](https://github.com/hongkailiu/dptp-doc/assets/4013349/8fe98b2f-e819-4fb6-ba75-a58e1647c0a6)



# Dev env of ci-docs

* [Hugo Documentation](https://gohugo.io/documentation/): _static_ website engine with the [Docsy](https://themes.gohugo.io/themes/docsy/) theme.

* bineries:

```console
$ hugo version
hugo v0.119.0 ...

$ npm -v
10.1.0
```

* Dependencies

```console
$ make generate
```

* run

```console
$ hugo server         
...
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at //localhost:1313/ (bind address 127.0.0.1) 
Press Ctrl+C to stop
```

Including dynamic content: This is a hacking way. Let us keep it simple and minimal.

```console
$ git --no-pager diff config.yaml 
diff --git a/config.yaml b/config.yaml
index 2ca06e8..1db4771 100644
--- a/config.yaml
+++ b/config.yaml
@@ -8,7 +8,7 @@ params:
   offlineSearch: true
   github_branch: master
   github_repo: "https://github.com/openshift/ci-docs"
-  api_v1_url: "https://cluster-display.ci.openshift.org"
+  api_v1_url: "http://localhost:8090"
 enableGitInfo: true
 menu:
   main:

$ cd ../ci-tools
$ make cluster-display
```

# Moving to quay.io: June 8 2023
The very first step: Promotion to Quay.io in addtion: [DPTP-3452](https://issues.redhat.com/browse/DPTP-3452): 

* An example job [branch-ci-openshift-cluster-image-registry-operator-master-images](https://prow.ci.openshift.org/view/gs/origin-ci-test/logs/branch-ci-openshift-cluster-image-registry-operator-master-images/1666753661004419072) and its [promotion pod](https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/origin-ci-test/logs/branch-ci-openshift-cluster-image-registry-operator-master-images/1666753661004419072/artifacts/build-resources/pods.json)

* Images in [quay.io/openshift/ci](https://quay.io/repository/openshift/ci?tab=tags): tags with `date` (to prune) and `sha` (to keep)

Issues:

* Issue 1 (reported by CI users): cluster-bot's HANDDRAFTED job (promoting to build farm?) and it has been [fixed](https://prow.ci.openshift.org/view/gs/origin-ci-test/logs/release-openshift-origin-installer-launch-aws-modern/1666609610544386048) untentionally.
* Issue 2 (thanks to Bruno): increased time for promotion, e.g., [ci-tools](https://prow.ci.openshift.org/job-history/gs/origin-ci-test/logs/branch-ci-openshift-ci-tools-master-images): `4m` to `8m`. The [fix](https://github.com/openshift/ci-tools/pull/3474) is on the way: A separate step/pod for "promotion-quay".

The next step: syncing other images that are used by CI tests

# oo-testing: March 2023

![Screenshot 2022-11-28 at 8 51 27 AM(1)](https://user-images.githubusercontent.com/4013349/225738093-f18f450d-86ae-4f08-9452-90b1cfa1d701.jpg)

* `operator`: unnamed and named bundles and index. See [our doc](https://docs.ci.openshift.org/docs/how-tos/testing-operator-sdk-operators/). PR-jobs: [unamed](https://prow.ci.openshift.org/view/gs/origin-ci-test/pr-logs/pull/openshift_windows-machine-config-operator/1492/pull-ci-openshift-windows-machine-config-operator-master-ci-index/1637983366806507520) and [named](https://prow.ci.openshift.org/view/gs/origin-ci-test/pr-logs/pull/rh-ecosystem-edge_kernel-module-management/482/pull-ci-rh-ecosystem-edge-kernel-module-management-main-ci-index-hub-operator-bundle/1637929248645713920).
* Interface to steps was the index image: [optional-operators-subscribe](https://steps.ci.openshift.org/reference/optional-operators-subscribe)
* Interface to steps is the bundle image: `operator-sdk run bundle -n my-namespace "$OO_BUNDLE_INIT"` because [operator-sdk has moved to file-based catalogs](https://docs.ci.openshift.org/docs/how-tos/testing-operator-sdk-operators/#moving-to-file-based-catalog)
* Skip the index [WIP] since it is useless: `skip_building_index`. [ci-tools/pull/3331](https://github.com/openshift/ci-tools/pull/3331).

# demo: Feb 2 2023

Status:
- [Enable monitoring user-defined projects](https://github.com/openshift/release/pull/34438):
  * Prometheus/AlertManager: UWM managed by CMO
  * Grafana: [Grafana-Operator](https://github.com/grafana-operator/grafana-operator) managed by OLM
- [Migrated](https://github.com/openshift/release/tree/master/clusters/app.ci/openshift-user-workload-monitoring) the existing mixin-generated metrics, alerts, and dashboards.
- Configure [UWM for Hive](https://github.com/openshift/release/blob/master/clusters/hive/openshift-user-workload-monitoring_cm.yaml): No mixins.

New:
- CR [Probe](https://github.com/openshift/release/blob/master/clusters/app.ci/openshift-user-workload-monitoring/blackbox_probe.yaml#L2) to replace `additionalScrapeConfigs`.
- Grafana: access to prometheus via SVC with [trusted CA certs](https://github.com/openshift/release/pull/34842)
- CR [AlertmanagerConfig](https://github.com/openshift/release/pull/35028/files#diff-92e061dcd79230dcb20cc796befa34a6ab05d73c926f8ba7a1129c25a635cf02R2): Secret references instead of [secret templates](https://github.com/openshift/release/blob/master/clusters/build-clusters/01_cluster/openshift-monitoring/alertmanager-main_secret_template.yaml)

Missing:
- Cannot manage UWM alerts: [OCPBUGS-6740](https://issues.redhat.com/browse/OCPBUGS-6740)


# demo: Jan 10 2023

Improvement of [periodic-ci-secret-bootstrap](https://deck-internal-ci.apps.ci.l2s4.p1.openshiftapps.com/job-history/gs/origin-ci-private/logs/periodic-ci-secret-bootstrap): 35m -> 12m

- Used to be 2m right after we switch from BW to Vault
  * More clusters
  * More user secrets: default on all clusters
- [Mostly](https://github.com/openshift/ci-tools/pull/3225#issuecomment-1372679618) updating secrets (about 3500 in total)
  * [Update secrets only when needed](https://github.com/openshift/ci-tools/pull/3229#issuecomment-1373029275): 35m -> 23m
  * [Reduce #API calls to get namespaces](https://github.com/openshift/ci-tools/pull/3232): 23m -> 12m

# demo: Sep. 29

- I complaint of the complexity of manipulating the kubeconfig file in [oc_sa_create_kubeconfig.sh](https://github.com/openshift/ci-tools/blob/master/images/ci-secret-generator/oc_sa_create_kubeconfig.sh) whenever a new token is requested.
- David [suggested](https://issues.redhat.com/browse/DPTP-3087?focusedCommentId=20919808&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-20919808) to link a [tokenFile](https://github.com/kubernetes/kubernetes/blob/f9afd68e3b3fc05f3607ea7cb90808c3e931ba9c/staging/src/k8s.io/client-go/tools/clientcmd/api/v1/types.go#L113-L115) in the kubeconfig and then the kuebconfig file is static and we need only to refresh the tokenFile.
- Example: `sprint-automation`: `sa.$(service_account).$(cluster).config` and `sa.$(service_account).$(cluster).token.txt`
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
