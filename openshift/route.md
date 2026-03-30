# Route

## Secure routes

* [Secure routes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/ingress_and_load_balancing/routes#securing-routes) and a [blog](https://www.redhat.com/en/blog/encryption-secure-routes-openshift) about it.

* An web app on an OpenShift cluster that handles encription by itself

Example: [ci-tools/qci-appci](https://github.com/openshift/ci-tools/blob/cc83eb1a89a484e10e3f22b293740ec4b4f0476e/cmd/qci-appci/main.go#L136)

It needs the cert files: the tls cert file and the tls key file.

A CA issues those two files.

In pracitce, they are done automatically by [cert-manager](https://cert-manager.io/docs/usage/ingress/#how-it-works) with [the annotation](https://github.com/openshift/release/blob/89212cc598fe26615c06d3f54ab6739e04869adf/clusters/app.ci/assets/admin_qci-appci.yaml#L55) on the relevant ingress manifest.

Then a HTTPS client such as `curl` or a web browser can verify the server's identity.
