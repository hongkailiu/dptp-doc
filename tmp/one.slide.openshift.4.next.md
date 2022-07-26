Choosing the CI build farm cluster build02 to run with nightly builds of OpenShift master branch is a story of the epic "OpenShift 4 Next".
We have done 2 spritntly upgrades and you can see the most recent one was a couple of days ago to a 4.12 nightly.

We have the supports from TRT for the issues that we cannot handle during the upgrades.
The results and findings can provide TRT a source of evidence to accept or reject the nightly.

From the two upgrades we have executed, we indeed found bugs and regression of OpenShift.
Build02 was burn with OCP 4.5.6. The version was too ancient that our normal CI upgrade tests usually do not cover, and we do have bugs there and our customers' clusters might be in the similar situation.

Another type of issue is regression.
Here is an example. We lost the compatibility of an annotation provided by openshift-machine-api.
It is not easy to spot and identify it if build02 was not in CI production, or users did not report errors in their tests.
It only happened to a smaller set of jobs.

I hope that all the sacrifice of UX in CI can be paid off by the improvement of quality of released versions of OpenShift.
