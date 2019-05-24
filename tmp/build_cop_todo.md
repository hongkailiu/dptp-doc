## build-cop dashboard

[PR3810](https://github.com/openshift/release/pull/3810)
and 
[DPTP-404](https://jira.coreos.com/browse/DPTP-404)

* Do we still need the first panel (basically what we are using now for build-cop report) with the rest of them present?

* release qualification vs pull request:
release-* vs pull-ci-*

    Q: no include e2e in the keyword?

* infrastructure failures vs other types

    Remark: Not failured information saved (by prow) for the noment.

* `job_name1` and `job_name2` are used only in the last panel for the case that none of the predefined panel satisfies your request, try the last one.

    Q: Do we need this?

Review [the current board](https://grafana-prow-monitoring-stage.svc.ci.openshift.org/d/6829209d59479d48073d09725ce807fa/build-cop-dashboard?orgId=1):

```
$ oc get deployment -n prow-monitoring-stage grafana -o yaml | grep ": GF_SECURITY_ADMIN_PASSWORD" -A1 -B2
```
