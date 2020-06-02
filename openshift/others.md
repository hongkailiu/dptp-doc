# others

* [red-hat-universal-base-image](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image)

## openshift config

* openshift-kube-apiserver: [event-ttl](https://github.com/openshift/origin/blob/0d7fb2d769d631054ec9ac0721aee623c96c1001/vendor/k8s.io/kubernetes/openshift-kube-apiserver/openshiftkubeapiserver/flags.go#L120): 3h

```
oc --as system:admin --context build01 exec -n openshift-kube-apiserver kube-apiserver-ip-10-0-140-81.ec2.internal -- ps auxwww
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  9.0  7.4 4023836 2379716 ?     Ssl  May02 827:53 kube-apiserver --openshift-config=/etc/kubernetes/static-pod-resources/configmaps/config/config.yaml --advertise-address=10.0.140.81 -v=2
```

* [ImageContentSourcePolicy](https://github.com/openshift/installer/blob/a1e76fa7a463af701e5771406c039af36de6e99b/docs/dev/alternative_release_image_sources.md#L51): [slack](https://coreos.slack.com/archives/CHY2E1BL4/p1589906227135500?thread_ts=1589905905.129300&cid=CHY2E1BL4)

```bash
oc --context build01 get ImageContentSourcePolicy  production-fallback -o yaml
apiVersion: operator.openshift.io/v1alpha1
kind: ImageContentSourcePolicy
metadata:
  annotations:
  name: production-fallback
spec:
  repositoryDigestMirrors:
  - mirrors:
    - registry.svc.ci.openshift.org/ocp/4.4-art-latest
    source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
```
