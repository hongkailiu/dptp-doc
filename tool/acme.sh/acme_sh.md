# acmd.sh

[DPTP-619](https://jira.coreos.com/browse/DPTP-619)

>  podman run -it --rm neilpang/acme.sh /bin/ash

```bash
###https://github.com/Neilpang/acme.sh/issues/331#issuecomment-255573031
# apk add libidn
```


* set up aws IAM user: [doc](https://github.com/Neilpang/acme.sh/wiki/How-to-use-Amazon-Route53-API)

* email: openshift-ci-robot@redhat.com

* `*.apps .build01.ci.devcluster.openshift.com`


```bash
acme.sh --issue --dns dns_aws -d api.build01.ci.devcluster.openshift.com -d '*.apps.build01.ci.devcluster.openshift.com'
...
[Sun Nov 24 18:24:26 UTC 2019] Your cert is in  /acme.sh/*.apps.build01.ci.devcluster.openshift.com/*.apps.build01.ci.devcluster.openshift.com.cer 
[Sun Nov 24 18:24:26 UTC 2019] Your cert key is in  /acme.sh/*.apps.build01.ci.devcluster.openshift.com/*.apps.build01.ci.devcluster.openshift.com.key 
[Sun Nov 24 18:24:26 UTC 2019] The intermediate CA cert is in  /acme.sh/*.apps.build01.ci.devcluster.openshift.com/ca.cer 
[Sun Nov 24 18:24:26 UTC 2019] And the full chain certs is there:  /acme.sh/*.apps.build01.ci.devcluster.openshift.com/fullchain.cer 
...
```

> acme.sh --renew --dns dns_aws -d '*.apps.build01.ci.devcluster.openshift.com'

[This blog](https://blog.openshift.com/requesting-and-installing-lets-encrypt-certificates-for-openshift-4/) tells us to use the `fullchain.cer`:

> $ oc create secret tls app-cert --cert=/home/hongkliu/Downloads/acme.sh/star.apps.build01.ci.devcluster.openshift.com/fullchain.cer --key=/home/hongkliu/Downloads/acme.sh/star.apps.build01.ci.devcluster.openshift.com/star.apps.build01.ci.devcluster.openshift.com.key  -n openshift-ingress


> oc patch ingresscontroller.operator default \
     --type=merge -p \
     '{"spec":{"defaultCertificate": {"name": "app-cert"}}}' \
     -n openshift-ingress-operator