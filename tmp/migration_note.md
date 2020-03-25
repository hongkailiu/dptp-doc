In order to improve our ability to provide a stable and performant set of CI services and to allow us to dog-food the product that we all work on, DPTP is migrating CI jobs from a 3.11 cluster to a 4.3 cluster this week.

We have attempted a migration in the past and were met with failure; however, as of today a subset of all jobs have been duplicated and running on both clusters for three weeks. We have assured that the 4.3 cluster is stable and that the jobs running there succeed as expected. During this process, we've been able to identify and report a number of bugs in the performance and functionality of the product and we're happy to note that all of these bugs have been fixed and that it's simple for us to upgrade to a newer verstion to consume those fixes.

In the next couple of days, we are going to:

 - remove the duplicated jobs from the new build farm
 - migrate existing jobs that had duplicates to the build farm


This may impact your workflow. For migrated jobs, if you previously logged into the [api.ci cluster](https://api.ci.openshift.org) in order to debug a job, you will now follow the same workflow as before but log in to the [new console](https://console-openshift-console.apps.build01.ci.devcluster.openshift.com). Today, you can tell if a job is migrated by looking at the `cluster` field for the job udner `ci-operator/jobs` in the `openshift/release` repository.

Eventually, all jobs will be on the new build farm and you will be able to use one console, but during the migration process we will have a combination of build farms in play at any one time.

We plan for the following steps to happen as we migrate all jobs:

 - migration of jobs that had not yet been duplicated but are generated from config
 - migration of hand-written jobs; if the migration causes them to fail we may reach out to affected teams for help here
 - migration of presubmits, including image publication and image mirroring
 - migration of periodics, including release gates and infrastructure jobs
 
Contact @dptp-helpdesk in #forum-testplatform if you found a job that behaves differently the new build farm.
