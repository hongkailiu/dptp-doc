# Dec 4

* builds by cluster-bot for [cvo#1093](https://github.com/openshift/oc/pull/1933)
  1. `build 4.19,openshift/cluster-version-operator#1093`: [job](https://prow.ci.openshift.org/view/gs/test-platform-results/logs/release-openshift-origin-installer-launch-aws-modern/1863693760852922368)
  2. `build 4.18,openshift/cluster-version-operator#1093`: [job](https://prow.ci.openshift.org/view/gs/test-platform-results/logs/release-openshift-origin-installer-launch-aws-modern/1863690003989663744)


* [OTA-1224](https://issues.redhat.com/browse/OTA-1224): status: simplify worker status line. [diff](https://github.com/openshift/oc/pull/1915/files#diff-62ba76b905a1f503936bc1d24ffb4e585fddfe75f1a4d4092a5b0257bac212b2R17)

  1. Move Outdated and Total to COMPLETION
  2. Hide zero non-happy values: Degraded/Excluded
  
* [OTA-1393](https://issues.redhat.com/browse/OTA-1393): status: recognize the process of migration to multi-arch. [asciinema demo](https://asciinema.org/a/vpYdHGGko6XvPdFh0wJQEvr1i)

  1. `00m45s`: `oc adm upgrade --to-multi-arch`
  2. `01m03s`: MCO update started
  3. `01m45s`: nodes restarting
  4. `06m28s`: [OTA-960](https://issues.redhat.com/browse/OTA-960) `oc adm upgrade` recognize the process of migration to multi-arch
  5. `23m15s`: upgrade completed

Issues: 
* Worker Pool: Completion 67% (2/3). WIP: [oc#1933](https://github.com/openshift/oc/pull/1933).
