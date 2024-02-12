# command

## oc

api.ci: `admin.kubeconfig` on api.ci masters: `KUBECONFIG=/etc/origin/master/admin.kubeconfig`

```
### node logs
#4.3 cluster (crio log is included)
$ node=ip-10-0-157-97.ec2.internal
$ oc --context build01 adm node-logs ${node} --since='2020-03-30 02:12:51' > ${node}.log
$ oc --context build01 adm node-logs ${node} --since="$(gdate -u +"%Y-%m-%d %H:%M:%S" -d "1 hour ago")" > ${node}.log
$ oc --context build01 adm node-logs ${node} -u crio.service -u kubelet.service > ${node}.log

#crio log only with rsync
#crio log: debug node; chroot /host
#journalctl --all --lines all --no-pager --unit crio.service  > /tmp/crio.hongkliu.all.log
$ oc --context build01 rsync ip-10-0-172-226ec2internal-debug:/host/tmp ./abc.tmp

### debug node
$ oc debug node/ip-10-0-133-100.us-east-2.compute.internal -- chroot /host journalctl -u kubelet.service -f

### gather debugging information for namespace/openshift-image-registry
$ oc --context build02 adm inspect namespace/openshift-image-registry

### check kubeconfig
$ oc --as system:admin --context build01 debug node/ip-10-0-130-137.ec2.internal -- chroot /host cat /etc/kubernetes/kubelet.conf

#311 cluster
$ node=origin-ci-ig-n-7mlq
$ gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" $node -- "sudo journalctl --all --lines all --no-pager --unit origin-node.service --since '24 hours ago'" > ${node}.node.log
$ gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" $node -- "sudo journalctl --all --lines all --no-pager --unit docker.service --since '24 hours ago'" > ${node}.docker.log

# restart docker and node service on 311 cluster
$ gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" $node -- "sudo systemctl restart docker.service origin-node.service"

### show internal/external IPs of the nodes
$ oc get node -o wide

###delete pods on a node
# cmd1
$ oc get pods --all-namespaces -o=jsonpath='{range .items[?(@.spec.nodeName=="origin-ci-ig-n-7mlq")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}' | while read ns name; do oc --as system:admin delete pod -n $ns $name --force --wait=false --grace-period=0; done
# cmd2
$ oc get pods --all-namespaces -o "jsonpath={range .items[?(@.spec.nodeName==\"origin-ci-ig-n-d4fs\")]}{\"oc delete --force --grace-period 0 pod \"}{.metadata.name}{\" --namespace \"}{.metadata.namespace}{\"\\n\"}{end}"
# cmc3
$ oc get pod --all-namespaces -o wide --no-headers |  awk '{ if ($8 == "origin-ci-ig-n-0rlt") { print $1, $2} }' | xargs -l oc get pod -o wide -n

### drain a node
$ bad_node=origin-ci-ig-n-6nhx
$ oc adm cordon "${bad_node}" --as system:admin --loglevel 4 | tee "${HOME}/Downloads/cordon-${bad_node}.log"
$ oc --as system:admin adm drain "${bad_node}"  --delete-local-data --ignore-daemonsets --loglevel 4 | tee "${HOME}/Downloads/drain-${bad_node}.log"
###no need for this when autoscaler is running
$ oc --as system:admin delete node "${bad_node}"

### taint a node
$ kubectl taint node ${node} dptp-debug=true:NoSchedule
### remove the taint
$ kubectl taint node ${node} dptp-debug:NoSchedule-

### label a node
$ oc label node ${node} node-role.kubernetes.io/debug=
### remove a label
$ oc label node ${node} node-role.kubernetes.io/debug-

### must-gather
oc --as system:admin --context build01 adm must-gather --dest-dir=./aaa

### RBAC-related cmds
#user wking want to login on the UI of monitoring stack
#https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#configuring-etcd-monitoring
$ oc adm policy add-cluster-role-to-user cluster-monitoring-view wking --as system:admin

$ oc adm policy who-can patch configmaps -n prow-monitoring

### list users
$ oc get user
### list groups ... the users in the group are in the output
$ oc get group

$ oc get group ci-admins
##ci-admins as cluster admins
$ oc adm policy add-cluster-role-to-group cluster-admin ci-admins
##ci-admins as project admins
### https://docs.openshift.com/container-platform/3.11/admin_guide/manage_rbac.html
### https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#roles
### https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding
### eg, https://github.com/openshift/release/pull/4520
$ oc adm policy add-role-to-group admin ci-admins --as system:admin
$ oc adm policy add-role-to-user admin deads2k --namespace somalley

# publicize the image
oc adm policy add-role-to-group system:image-puller system:unauthenticated

### print out the token of a service-account
$ oc sa get-token -n ci ipi-deprovisioner
### use the sa token to oc-login
$ oc login https://api.ci.openshift.org --token=<sa_token>

### output pod logs
$ oc get pod -n default | grep docker-registry | awk '{print $1}' | while read pod; do oc logs -n default $pod --since 8h --timestamps > $pod.log; done

###https://coreos.slack.com/archives/CMC5URNEM/p1566327819028500
###retag the latest of an image
###### find out the desired image, e.g., the 2nd last built image
$ oc --context api.ci get is -n ci ci-operator -o json | jq -r '.status.tags[] | select(.tag == "latest") | .items[1].image'
sha256:92f12a6f82fc07ddfd88a20bcbbc14550fd5f6cf4b3ad7cb3986e219227e2715

###### check if the commit id is the one desired
$ podman inspect registry.svc.ci.openshift.org/ci/ci-operator@sha256:92f12a6f82fc07ddfd88a20bcbbc14550fd5f6cf4b3ad7cb3986e219227e2715 | jq -r '.[0].Labels["io.openshift.build.commit.id"]'
6eb6b2b8cd9b98e792f83a8d541f1c48696105bf

######re-tag the image
$ oc tag ci/ci-operator@sha256:92f12a6f82fc07ddfd88a20bcbbc14550fd5f6cf4b3ad7cb3986e219227e2715 ci/ci-operator:latest

######With docker
$ docker inspect registry.svc.ci.openshift.org/ci/ci-operator@sha256:947332cac382548ed99dd193be2674af8a5eba81881a6d6fde54e5cb75e5e96b | jq ".[0].Config.Labels[\"io.openshift.build.commit.id\"]"
"b04de66e58ababf901783140acd3e8510309f1f2"

### approve certificate
# oc get csr -o name | xargs oc adm certificate approve

### jsonpath https://kubernetes.io/docs/reference/kubectl/jsonpath/
$ oc get prowjob -n ci -o "jsonpath={.items[?(@.spec.cluster==\"ci/api-build01-ci-devcluster-openshift-com:6443\")].metadata.name}"

### list volumes
$ oc set volume -n openshift-image-registry deployment.apps/image-registry --all

### secret
###https://github.com/openshift/origin/issues/18449#issuecomment-363516477
$ oc create secret generic --from-file=.dockerconfigjson=/home/hongkliu/Downloads/.dockercfg --type=kubernetes.io/dockerconfigjson pullsecret  --kubeconfig ~/.kube/build01.config

### upgrade
oc --context build01 adm upgrade --allow-explicit-upgrade --to-image registry.svc.ci.openshift.org/ocp/release:4.3.0-0.nightly-2020-02-25-200400 --force=true
# pin the nightly build to avoid being GCed
oc annotate -n ocp istag release:4.3.0-0.nightly-2020-03-23-130439 "release.openshift.io/keep=CI test build"
# cancel upgrade
oc --as system:admin --context build02 adm upgrade --clear

###https://10.0.146.81:10250/metrics/cadvisor
oc --context build01 get --raw  /api/v1/nodes/ip-10-0-146-81.ec2.internal/proxy/metrics/cadvisor

###
oc --context build02 -n hongkliu-test run -i -t debug --image=quay.io/centos/centos:stream8 --restart=Never --rm=true
oc exec -it -n ci deck-internal-7b5cb98cc9-6fh69 -c deck -- sh

### port-forward alert manager UI
oc --as system:admin --context hive port-forward -n openshift-user-workload-monitoring alertmanager-user-workload-0 9093:9093


### rsh
oc --as system:admin --context build01 rsh -n openshift-monitoring -c prometheus prometheus-k8s-1
### exec
oc --as system:admin --context build01 exec -n openshift-monitoring prometheus-k8s-1 -- rm -rf wal/

### list pods on a specific node
oc --context build02 get pod -A -o wide --field-selector spec.nodeName=build0-gstfj-m-1.c.openshift-ci-build-farm.internal
```

## gcloud

```
### some command
$ gcloud compute ssh "origin-ci-ig-n-t48j" --command "ls -al"
$ gcloud compute ssh "origin-ci-ig-m-428p" --command "sudo cat /etc/origin/master/master-config.yaml"

### interactive ssh login
$ gcloud compute ssh origin-ci-ig-m-428p -- -L 2222:localhost:8888

### scp https://cloud.google.com/sdk/gcloud/reference/compute/scp
gcloud compute scp --recurse ~/Downloads/api.ci.cert.1209/upload/ origin-ci-ig-m-428p:~/20191209/


### restart master api on f3g1
### Bruno: https://prometheus-k8s-openshift-monitoring.svc.ci.openshift.org/graph?g0.range_input=2h&g0.expr=container_memory_usage_bytes%7Bnamespace%3D%22kube-system%22%2Ccontainer_name%3D%22%22%7D&g0.tab=0
$ gcloud compute ssh origin-ci-ig-m-f3g1 -- sudo /usr/local/bin/master-restart api

### restart master controller
$ for master in origin-ci-ig-m-428p origin-ci-ig-m-f3g1 origin-ci-ig-m-pbj3; do \
    gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" "${master}" -- "sudo /usr/local/bin/master-restart controllers" \
done

### restart instance
$ gcloud compute --project "openshift-ci-infra" ssh --zone "us-east1-c" origin-ci-ig-n-jbbh -- sudo reboot now
(not tested) $ gcloud compute instance stop
$ gcloud compute --project "openshift-ci-infra"  instances start --zone "us-east1-c" origin-ci-ig-n-jbbh

###find PVs attached to an instance
$ gcloud compute disks list  --filter="users:(origin-ci-ig-n-0rlt)"
###also visible on the UI: https://console.cloud.google.com/compute/instancesDetail/zones/us-east1-c/instances/origin-ci-ig-n-0rlt?authuser=1&project=openshift-ci-infra
$ gcloud compute instances describe origin-ci-ig-n-0rlt --format json | jq -r '.disks[].deviceName'
origin-ci-instance-template-node-large-disk

###detach a disk from an instance: https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk
```

```
###https://cloud.google.com/storage/docs/gsutil_install#linux
###Update: gsutl is part of google sdk now. No need to install additionally.

### the bucket is in project "OpenShift GCE Devel"
$ gsutil ls gs://origin-ci-test/

### delete stored logs from google storage
$ gsutil -m rm -r gs://origin-ci-test/pr-logs/pull/openshift_release/5534/pull-ci-openshift-release-master-build01-dry/8/
```

```console
### get-serial-port-output
$ gcloud --project openshift-ci-build-farm --format json compute instances get-serial-port-output --zone us-east1-c build0-gstfj-ci-builds-worker-c-5pbsj > build0-gstfj-ci-builds-worker-c-5pbsj.json
```

## git

```bash
$ git branch | grep -ve " master$" | xargs git branch -D
```

## podman

```
$ podman run --entrypoint='["cat", "/etc/shells"]'  -it docker.io/timberio/vector:0.8.2-debian
```

## skopeo

```bash
# skopeo copy --src-creds hongkailiu:secret docker://registry.svc.ci.openshift.org/ci-op-v9xbbsn6/pipeline:ci-operator docker://quay.io/hongkailiu/ci-op:ci-operator-009

### on mac with apple-silicon chip
$ skopeo inspect --override-os=linux --override-arch amd64 docker://registry.ci.openshift.org/ci/redhat-operator-index:v4.10
```

## failover

``` bash
$ CONTAINER_ENGINE=podman PROMTOKEN_TEMPLATE=/Users/hongkliu/repo/tmp/abc-script.XXXXXX ./hack/failover.sh --enable-cluster=build02
$ CONTAINER_ENGINE=podman VOLUME_MOUNT_FLAGS='' make jobs
$ vi hack/generators/release-controllers/content/osd_rc_deployments.py
$ source ~/tool/p3env/bin/activate && make release-controllers
```

## misc

> oc --context build01 get events --all-namespaces -o json | jq --raw-output '.items[] | select(.message | test(".*context deadline exceeded.")) | .source.host' | sort | uniq -c


```console
### query GitHub in Tide's pod
$ token=$(oc --context app.ci get secret -n ci github-credentials-openshift-merge-robot -o json | jq .data.oauth -r | base64 -d)
$ tide_pod=$(oc get pod -n ci -l app=prow,component=tide --no-headers -o custom-columns=":metadata.name")
$ oc --as system:admin exec -n ci $tide_pod -- wget -O- --header "Authorization: Token $token" --header "Accept: application/vnd.github.v3+json" https://api.github.com/repos/red-hat-storage/kubernetes-csi-addons | jq .allow_merge_commit

```

```console
$ oc get nodes -o json | jq -r '.items[]|(select((.spec.taints != null) and .spec.taints[].key=="manual-provision"))|"\(.metadata.name) \(.metadata.labels."node.kubernetes.io/instance-type")"'
ip-10-0-128-253.ec2.internal r5.2xlarge
ip-10-0-134-82.ec2.internal r5.2xlarge
ip-10-0-136-237.ec2.internal r5.2xlarge
```

```console
$ oc --context build05 adm top no -l node-role.kubernetes.io/master
```

## migration

```bash
//find ./ci-operator/config -type d -depth 2 | head -n 300 | while read i; do echo "\"${i#./ci-operator/config/}/.*\","; done

$ config-migrator --config-dir ./ci-operator/config/

$ find ./ci-operator/config -type d -depth 2 | head -n 30 | while read i; do echo "${i#./ci-operator/config/}"; done > /tmp/repo.txt
$ cat /tmp/repo.txt | while read line; do find /Users/hongkliu/repo/openshift/release/ci-operator/jobs/$line -name "*presubmits.yaml" -print -exec python3 hack/migrate_jobs.py {} \;; done

$ ci-operator-prowgen --from-dir ./ci-operator/config/ --to-dir ./ci-operator/jobs/
```


## upgrade progress

oc cli:

```
oc --context build02 get -o json nodes | jq -r '.items[].metadata.annotations | .["machineconfiguration.openshift.io/currentConfig"] + " " + .["machineconfiguration.openshift.io/desiredConfig"] + " " + .["machineconfiguration.openshift.io/state"]' | sort | uniq -c
```


Promethus queries:

```console
count by (kernel_version, kubelet_version) (kube_node_info)

group by (type, from_version, version) (cluster_version{type=~"current|updating"})
```
