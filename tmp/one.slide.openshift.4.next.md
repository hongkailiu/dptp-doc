Choosing the CI build farm cluster build02 to run with nightly builds of OpenShift master branch is a story of the epic "OpenShift 4 Next".
We have done 2 spritntly upgrades and you can see the most recent one was a couple of days ago to a 4.12 nightly.

We have the supports from TRT for the issues that we cannot handle during the upgrades.
The results and findings can provide evidence for TRT to accept or reject the nightly.

From the two upgrades we have executed, we indeed found bugs and regressions of OpenShift.
Build02 was burn with OCP 4.5.6. The version was too ancient that our normal CI upgrade tests usually does not cover, and however we do have bugs there and customer's clusters in similar situation.

Another type of issues is regression.
Here is an example. We lost the compatibility of an annotation.
It is not easy to spot and identify it if build02 was not in CI production, or users did not report errors in their tests.
It only happened to a smaller set of jobs.
