# Mar 12, 2025

In Petr's previous demo, we have seen `ClusterVersion/version` in the status api (currently stored in a CM):

The CM [status-api-cm-prototype.yaml](https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/test-platform-results/pr-logs/pull/openshift_cluster-version-operator/1164/pull-ci-openshift-cluster-version-operator-main-e2e-agnostic-usc-devpreview/1899151748635824128/artifacts/e2e-agnostic-usc-devpreview/e2e-test/artifacts/status-api-cm-prototype.yaml)
is taken from
[ProwJob/pull-ci-openshift-cluster-version-operator-main-e2e-agnostic-usc-devpreview](https://prow.ci.openshift.org/view/gs/test-platform-results/pr-logs/pull/openshift_cluster-version-operator/1164/pull-ci-openshift-cluster-version-operator-main-e2e-agnostic-usc-devpreview/1899151748635824128)

```console
$ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/test-platform-results/pr-logs/pull/openshift_cluster-version-operator/1164/pull-ci-openshift-cluster-version-operator-main-e2e-agnostic-usc-devpreview/1899151748635824128/artifacts/e2e-agnostic-usc-devpreview/e2e-test/artifacts/status-api-cm-prototype.yaml | yq -r '.data."usc.cpi.cv-version"' | yq -y
uid: cv-version
acquiredat: '2025-03-10T18:46:44.180206779Z'
controlplaneinsightunion:
  type: ClusterVersion
  clusterversionstatusinsight:
    conditions:
      - type: Updating
        status: 'False'
        observedgeneration: 0
        lasttransitiontime: '2025-03-10T18:46:44.180206779Z'
        reason: ClusterVersionNotProgressing
        message: ClusterVersion has Progressing=False(Reason=) | Message='Cluster
          version is 4.19.0-0.ci.test-2025-03-10-174412-ci-op-jbg3iv3k-latest'
    resource:
      group: config.openshift.io
      resource: clusterversions
      name: version
      namespace: ''
    assessment: Completed
    versions:
      previous:
        version: ''
        metadata: []
      target:
        version: 4.19.0-0.ci.test-2025-03-10-174412-ci-op-jbg3iv3k-latest
        metadata:
          - key: Installation
            value: ''
    completion: 100
    startedat: '2025-03-10T18:17:18Z'
    completedat: '2025-03-10T18:43:50Z'
    estimatedcompletedat: '2025-03-10T19:17:18Z'
  clusteroperatorstatusinsight: null
  machineconfigpoolstatusinsight: null
  nodestatusinsight: null
  healthinsight: null
```

In the last couple of sprints, more information about upgrade-status has been moved to the sever side (USC):

- ClusterOperators
- Nodes

```console
$ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/test-platform-results/pr-logs/pull/openshift_cluster-version-operator/1164/pull-ci-openshift-cluster-version-operator-main-e2e-agnostic-usc-devpreview/1899151748635824128/artifacts/e2e-agnostic-usc-devpreview/e2e-test/artifacts/status-api-cm-prototype.yaml | yq -r '.data|keys[]' | grep 'usc.cpi.co-'
usc.cpi.co-authentication
usc.cpi.co-baremetal
usc.cpi.co-cloud-controller-manager
...

$ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/test-platform-results/pr-logs/pull/openshift_cluster-version-operator/1164/pull-ci-openshift-cluster-version-operator-main-e2e-agnostic-usc-devpreview/1899151748635824128/artifacts/e2e-agnostic-usc-devpreview/e2e-test/artifacts/status-api-cm-prototype.yaml | yq -r '.data."usc.cpi.co-authentication"' | yq -y
uid: co-authentication
acquiredat: '2025-03-10T18:46:44.180580187Z'
controlplaneinsightunion:
  type: ClusterOperator
  clusterversionstatusinsight: null
  clusteroperatorstatusinsight:
    conditions:
      - type: Updating
        status: 'False'
        observedgeneration: 0
        lasttransitiontime: '2025-03-10T18:46:44.180580187Z'
        reason: Updated
        message: ''
      - type: Healthy
        status: 'True'
        observedgeneration: 0
        lasttransitiontime: '2025-03-10T18:46:44.180580187Z'
        reason: AsExpected
        message: ''
    name: authentication
    resource:
      group: config.openshift.io
      resource: clusteroperators
      name: authentication
      namespace: ''
  machineconfigpoolstatusinsight: null
  nodestatusinsight: null
  healthinsight: null

$ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/test-platform-results/pr-logs/pull/openshift_cluster-version-operator/1164/pull-ci-openshift-cluster-version-operator-main-e2e-agnostic-usc-devpreview/1899151748635824128/artifacts/e2e-agnostic-usc-devpreview/e2e-test/artifacts/status-api-cm-prototype.yaml | yq -r '.data|keys[]' | grep 'usc.ni.node-'
usc.ni.node-ci-op-jbg3iv3k-8c750-cmpdh-master-0
usc.ni.node-ci-op-jbg3iv3k-8c750-cmpdh-master-1
usc.ni.node-ci-op-jbg3iv3k-8c750-cmpdh-master-2
usc.ni.node-ci-op-jbg3iv3k-8c750-cmpdh-worker-eastus21-vx5n5
usc.ni.node-ci-op-jbg3iv3k-8c750-cmpdh-worker-eastus22-fc8kl
usc.ni.node-ci-op-jbg3iv3k-8c750-cmpdh-worker-eastus23-lnw8z

$ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/test-platform-results/pr-logs/pull/openshift_cluster-version-operator/1164/pull-ci-openshift-cluster-version-operator-main-e2e-agnostic-usc-devpreview/1899151748635824128/artifacts/e2e-agnostic-usc-devpreview/e2e-test/artifacts/status-api-cm-prototype.yaml | yq -r '.data."usc.ni.node-ci-op-jbg3iv3k-8c750-cmpdh-master-0"' | yq -y
uid: node-ci-op-jbg3iv3k-8c750-cmpdh-master-0
acquiredat: '2025-03-10T18:48:35.005300795Z'
workerpoolinsightunion:
  type: Node
  machineconfigpoolstatusinsight: null
  nodestatusinsight:
    conditions:
      - type: Updating
        status: 'False'
        observedgeneration: 0
        lasttransitiontime: '2025-03-10T18:48:35.005300795Z'
        reason: Completed
        message: The node is updated
      - type: Available
        status: 'True'
        observedgeneration: 0
        lasttransitiontime: '2025-03-10T18:48:35.005300795Z'
        reason: AsExpected
        message: The node is available
      - type: Degraded
        status: 'False'
        observedgeneration: 0
        lasttransitiontime: '2025-03-10T18:48:35.005300795Z'
        reason: AsExpected
        message: The node is not degraded
    name: ci-op-jbg3iv3k-8c750-cmpdh-master-0
    resource:
      group: ''
      resource: nodes
      name: ci-op-jbg3iv3k-8c750-cmpdh-master-0
      namespace: ''
    poolresource:
      resourceref:
        group: machineconfiguration.openshift.io
        resource: machineconfigpools
        name: master
        namespace: ''
    scope: ControlPlane
    version: 4.19.0-0.ci.test-2025-03-10-174412-ci-op-jbg3iv3k-latest
    esttocomplete:
      duration: 0s
    message: ''
  healthinsight: null
```


# Dec 4

* builds by cluster-bot for [cvo#1093](https://github.com/openshift/oc/pull/1933)
  1. `build 4.19,openshift/cluster-version-operator#1093`: [job](https://prow.ci.openshift.org/view/gs/test-platform-results/logs/release-openshift-origin-installer-launch-aws-modern/1863693760852922368)
  2. `build 4.18,openshift/cluster-version-operator#1093`: [job](https://prow.ci.openshift.org/view/gs/test-platform-results/logs/release-openshift-origin-installer-launch-aws-modern/1863690003989663744)


* [OTA-1224](https://issues.redhat.com/browse/OTA-1224): status: simplify worker status line. [diff](https://github.com/openshift/oc/pull/1915/files#diff-a760b693ddc0884c0a608b1d65d263b25d94ef2afe6943ba8a56e8445848b1daR17)

  1. Move Outdated and Total to COMPLETION
  2. Hide zero non-happy values: Degraded/Excluded
  
* [OTA-1393](https://issues.redhat.com/browse/OTA-1393): status: recognize the process of migration to multi-arch. [asciinema demo](https://asciinema.org/a/vpYdHGGko6XvPdFh0wJQEvr1i)

  1. `00m45s`: `oc adm upgrade --to-multi-arch`
  2. `01m03s`: upgrade detected
  3. `01m48s`: MCO update started
  4. `02m45s`: nodes restarting
  5. `06m28s`: [OTA-960](https://issues.redhat.com/browse/OTA-960) `oc adm upgrade` showing the process of migration to multi-arch
  6. `23m15s`: upgrade completed

Issues: 
* Worker Pool: Completion 67% (2/3). WIP: [oc#1933](https://github.com/openshift/oc/pull/1933).
