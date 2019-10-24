# command

## oc

```
$ oc adm policy add-role-to-user view -n ci <username>
#eg, user wking want to login on the UI of monitoring stack
#https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#configuring-etcd-monitoring
$ oc adm policy add-cluster-role-to-user cluster-monitoring-view wking --as system:admin
cluster role "cluster-monitoring-view" added: "wking"

$ oc adm policy who-can patch configmaps -n prow-monitoring
$ oc get rolebinding author-access -n prow-monitoring
$ oc get groups ci-admins
###ci-admins as project admins
$ oc adm policy add-role-to-group admin ci-admins --as system:admin
role "admin" added: "ci-admins"
###ci-admins as cluster admins
$ oc adm policy add-cluster-role-to-group cluster-admin ci-admins

### print out the token of a service-account
$ oc sa get-token -n ci ipi-deprovisioner
### use the sa token to oc-login
$ oc login https://api.ci.openshift.org --token=<sa_token>

### user to become a project admin
### https://docs.openshift.com/container-platform/3.11/admin_guide/manage_rbac.html
### https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#roles
### https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding
### eg, https://github.com/openshift/release/pull/4520
### OR, do it via cli, eg,
$ oc adm policy add-role-to-user admin deads2k --namespace somalley

### output pod logs
$ oc get pod -n openshift-sdn --no-headers | awk '{print $1}' | while read pod; do oc logs -n openshift-sdn $pod >> ~/Downloads/20190820network/pods-${pod}.log; done
### logs with timestamp and since
$ oc get pod -n default | grep docker-registry | awk '{print $1}' | while read pod; do oc logs -n default $pod --since 8h --timestamps > $pod.log; done

### list users
$ oc get user
### list groups ... the users in the group are in the output
$ oc get group

###retag the latest of an image
#https://coreos.slack.com/archives/CMC5URNEM/p1566327819028500
#steve: get history of sha of images:
$ oc get is -n ci ci-operator -o yaml
$ docker inspect registry.svc.ci.openshift.org/ci/ci-operator@sha256:947332cac382548ed99dd193be2674af8a5eba81881a6d6fde54e5cb75e5e96b | jq ".[0].Config.Labels[\"io.openshift.build.commit.id\"]"
"b04de66e58ababf901783140acd3e8510309f1f2"

###re-tag the image
$ oc tag ci/ci-operator@sha256:b9166ca34f581cb6e513c4824ce34f6d6f511b2bdc837e30325575f2cf5ecc5b ci/ci-operator:latest


###use podman to inspect
$ podman inspect registry.svc.ci.openshift.org/ci/ci-operator:latest | jq -r '.[0].ContainerConfig.Labels["io.openshift.build.commit.id"]' 
7087de11e0ce91d949e9ea6b00cbc1d7fb0561de

### approve certificate
# oc get csr -o name | xargs oc adm certificate approve

```
