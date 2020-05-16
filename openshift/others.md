# others

* [red-hat-universal-base-image](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image)

## openshift config

* openshift-kube-apiserver: [event-ttl](https://github.com/openshift/origin/blob/0d7fb2d769d631054ec9ac0721aee623c96c1001/vendor/k8s.io/kubernetes/openshift-kube-apiserver/openshiftkubeapiserver/flags.go#L120): 3h

```
oc --as system:admin --context build01 exec -n openshift-kube-apiserver kube-apiserver-ip-10-0-140-81.ec2.internal -- ps auxwww
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  9.0  7.4 4023836 2379716 ?     Ssl  May02 827:53 kube-apiserver --openshift-config=/etc/kubernetes/static-pod-resources/configmaps/config/config.yaml --advertise-address=10.0.140.81 -v=2
```
