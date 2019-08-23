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
$ oc adm policy add-role-to-group admin ci-admins --as system:admin
role "admin" added: "ci-admins"

### print out the token of a service-account
$ oc sa get-token -n ci ipi-deprovisioner
### use the sa token to oc-login
$ oc login https://api.ci.openshift.org --token=<sa_token>

### user to become a project admin
### https://docs.openshift.com/container-platform/3.11/admin_guide/manage_rbac.html
### https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#roles
### https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding
### eg, https://github.com/openshift/release/pull/4520

### output pod logs
$ oc get pod -n openshift-sdn --no-headers | awk '{print $1}' | while read pod; do oc logs -n openshift-sdn $pod >> ~/Downloads/20190820network/pods-${pod}.log; done

### list users
$ oc get user
### list groups ... the users in the group are in the output
$ oc get group
```
