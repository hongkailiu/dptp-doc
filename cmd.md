# command

## oc

```
$ oc adm policy add-role-to-user view -n ci <username>

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
```
