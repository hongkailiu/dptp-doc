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
