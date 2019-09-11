I kept thinking about this last night after seeing your msg and do NOT need your answer right away. :)
I just want to understand the idea of bring operator-framework for the task of auto-bumper.

Let us say we will develop prow-operator which reads CRDs for prow-components.
Eg, `oc apply -f plank.yaml`, where plank.yaml defines a deployment (including the plank image version) of plank, like we do for prometheus with crd:
https://github.com/openshift/release/blob/master/cluster/ci/monitoring/prometheus_crd.yaml

Then we apply CRDs (and RBACs if necessary) for all other prow-components.

So we replace the deployment (maybe SVCs and routers as well) yaml files with CRDs by implementing the prow-operator.

*We still need a cmd autobumper to change the images version in the CRDs in the above logic.*, right?

Then what about the upgrade of the operator itself? I can still go with the traditional way: `oc apply -f prow-operator_deployment.yaml`.
But in the operator world, i think the answer is OLM: https://github.com/operator-framework/operator-lifecycle-manager
It uses CSV (https://github.com/operator-framework/operator-lifecycle-manager/blob/master/doc/design/building-your-csv.md) to
control the operator version (and all prow CRDs) and all other k8s-objects (such as RBACs and SVCs and routers) related to the operator.

Eg, the CSV for prometheus:
https://github.com/operator-framework/community-operators/blob/master/community-operators/prometheus/prometheusoperator.0.14.0.clusterserviceversion.yaml

In our monitoring stack on OCP 311 ci-cluster (without OLM installed out of the box), we have prometheus-operator (controlling prometheus and alertmanager) but
we have not used CSV for it.

So let us say our OCP 4 (OLM is installed by default) upgrading plan is implemented already.
Then our CVS for prow-monitor is to control prow-monitor operator.

Then what about the version control for CSV itself?
As far as I understand the eco-system of operator-framework, this is done by pushing the application bundle (CSV yaml and others)
to application repo of quay.io (NOTE not image repo) or publish to community-operators (https://github.com/operator-framework/community-operators/blob/master/community-operators/):
https://github.com/operator-framework/community-operators/blob/master/docs/testing-operators.md
So operator-marketplace (installed by default on OCP 4) or https://operatorhub.io/ has an integration for those operator.

Back to our prow-operator on OCP 4 ci-cluster:
We can go all the way to operatorhub (since OLM and marketplace are out of the box).

For upstream:
1. prow-operator
2. OLM
Those 2 steps seems reasonable to me.
3. operatorhub: It is not clear to me how operator-marketplace(https://github.com/operator-framework/operator-marketplace)
is going to work on a k8s-cluster. To be honest, I might vote No even if I know how to deploy it on k8s-cluster (never worked
well in my previous tests, but we will know very soon i guess).


