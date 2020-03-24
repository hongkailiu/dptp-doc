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

### debug node
$ oc debug node/ip-10-0-133-100.us-east-2.compute.internal -- chroot /host journalctl -u kubelet.service -f


$ oc get prowjob -n ci -o "jsonpath={.items[?(@.spec.cluster==\"ci/api-build01-ci-devcluster-openshift-com:6443\")].metadata.name}"

$ oc set volume -n openshift-image-registry deployment.apps/image-registry --all

###https://github.com/openshift/origin/issues/18449#issuecomment-363516477
$ oc create secret generic --from-file=.dockerconfigjson=/home/hongkliu/Downloads/.dockercfg --type=kubernetes.io/dockerconfigjson pullsecret  --kubeconfig ~/.kube/build01.config

# skopeo copy --src-creds hongkailiu:secret docker://registry.svc.ci.openshift.org/ci-op-v9xbbsn6/pipeline:ci-operator docker://quay.io/hongkailiu/ci-op:ci-operator-009

# publicize the image
oc adm policy add-role-to-group system:image-puller system:unauthenticated

# upgrade
oc --context build01 adm upgrade --allow-explicit-upgrade --to-image registry.svc.ci.openshift.org/ocp/release:4.3.0-0.nightly-2020-02-25-200400 --force=true
# pin the nightly build to avoid being GCed
oc annotate -n ocp istag release:4.3.0-0.nightly-2020-03-23-130439 "release.openshift.io/keep=CI test build"
```

## migration

```bash
//find ./ci-operator/config -type d -depth 2 | head -n 300 | while read i; do echo "\"${i#./ci-operator/config/}/.*\","; done

$ config-migrator --config-dir ./ci-operator/config/

$ find ./ci-operator/config -type d -depth 2 | head -n 30 | while read i; do echo "${i#./ci-operator/config/}"; done > /tmp/repo.txt
$ cat /tmp/repo.txt | while read line; do find /Users/hongkliu/repo/openshift/release/ci-operator/jobs/$line -name "*presubmits.yaml" -print -exec python3 hack/migrate_jobs.py {} \;; done

$ ci-operator-prowgen --from-dir ./ci-operator/config/ --to-dir ./ci-operator/jobs/
```

## git

```bash
$ git branch | grep -ve " master$" | xargs git branch -D
```

## podman

```
$ podman run --entrypoint='["cat", "/etc/shells"]'  -it docker.io/timberio/vector:0.8.2-debian
```
