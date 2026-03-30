# service

* [The Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/html/rfc8446)

* [3.3. Securing service traffic using service serving certificate secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/security_and_compliance/configuring-certificates#add-service-serving)

Example: CVO:

* [service](https://github.com/openshift/cluster-version-operator/blob/90fd30316ae61cded9785ea969e575b7b155803a/install/0000_00_cluster-version-operator_40_service.yaml#L12) is with the annotation `service.beta.openshift.io/serving-cert-secret-name: cluster-version-operator-serving-cert`.

* [deployment](https://github.com/openshift/cluster-version-operator/blob/90fd30316ae61cded9785ea969e575b7b155803a/install/0000_00_cluster-version-operator_30_deployment.yaml#L113-L115) mounts the secret onto the pod. [CVO hosts a HTTP server](https://github.com/openshift/cluster-version-operator/blob/0a6ec71a0b1519dff9559af0ada738da288f343d/pkg/cvo/metrics.go#L279), as [a Prometheus endpoint](https://prometheus.io/docs/instrumenting/clientlibs/), with TLS configuration based on the cert file and the key file. This is how a HTTP client identifies the server.

Moreover, the HTTP server uses the CA bundle to verify the identity of a HTTP request. It is the best practice according to [Red Hat Monitoring Group Handbook](https://rhobs-handbook.netlify.app/products/openshiftmonitoring/collecting_metrics.md/).

There are different ways to get CA bundle. [CVO](https://github.com/openshift/cluster-version-operator/blob/0a6ec71a0b1519dff9559af0ada738da288f343d/pkg/cvo/metrics.go#L325-L330) takes it from ConfigMap `kube-system/extension-apiserver-authentication` via the key `client-ca-file`.
