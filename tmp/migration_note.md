We are migrating prow jobs from `api.ci` cluster (3.11) to `build01` cluster (4.3).

For each prow controlled (presubmit) job (with label `ci-operator.openshift.io/prowgen-controlled: "true"`), there has been a duplicated one running
on build01. See the presubmits for this PR history for example:
https://prow.svc.ci.openshift.org/pr-history/?org=openshift&repo=origin&pr=24758 job
`pull-ci-openshift-origin-release-4.3-verify` runs on api.ci and `pull-ci-openshift-origin-release-4.3-verify-build01` is the duplicated
one on build01.
We have been testing the performance of build01 this way for weeks and found bugs (of both ci tools and cluster) which got fixed.

In the next couple of days, we are going to
* remove the duplicated jobs
* migrate those prow controlled jobs from api.ci to build01

console:
* api.ci: https://api.ci.openshift.org/console/catalog
* build01: https://console-openshift-console.apps.build01.ci.devcluster.openshift.com/dashboards

How the change impacts the dev's workflow:

When debugging a failing job, we need to find out where it runs by `cluster` field of the job definition. 
If `cluster: api.ci`, then it means the job still runs on api.ci cluster.
If `cluster: ci/api-build01-ci-devcluster-openshift-com:6443`, it is on build01.

Then we login to right cluster's console (links above) and obtain the token for oc-cli. We can find the `ci-op-XXXX` namespace ONLY on the cluster where the job runs.

Eventually, all jobs will be on build01 but they might run in different places during the migration process.

The plan of migration:
* prow controlled presubmits: We are in the process of this now.
* all presubmits
* periodics
* postsubmits

Contact @dptp-helpdesk in #forum-testplatform if you found a job which behaves differently on build01 from api.ci.

