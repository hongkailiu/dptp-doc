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
