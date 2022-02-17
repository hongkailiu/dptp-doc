## Summary

- accounts on AWS/GCP and what each of them is for.
- the cloud services TP uses often
- AWS CloudWatch and Cloud DNS


## Cluster Topology

oc-cli is sufficient except outages!

<img width="1051" alt="Screen Shot 2022-02-15 at 5 50 14 PM" src="https://user-images.githubusercontent.com/4013349/154168942-9de16f51-3460-424f-9099-d661a519af6b.png">

## AWS
AWS accounts: `https://<account>.signin.aws.amazon.com/console`
  
- openshift-ci-infra: [build farm clusters](https://docs.ci.openshift.org/docs/getting-started/useful-links/#clusters), such as build01, build03; DPP also uses it.
- openshift-ci: ephemeral clusters provisioned for CI tests
- openshift-ci-pools: ephemeral clusters provisioned for CI tests with [cluster claims](https://docs.ci.openshift.org/docs/architecture/ci-operator/#testing-with-a-cluster-from-a-cluster-pool)

Services: EC2, VPC, Route53, CloudWatch, etc.

CloudWatch: Prow logs, API server audit logs for build0{1|2} (openshift-ci-infra)

## CloudWatch

Upload via [vector](https://github.com/openshift/release/blob/62dce99f006bfa6625a5b2b19ee278ea3babb4b0/clusters/build-clusters/01_cluster/openshift/api_audit_log/vector-audit-log_daemonset.yaml#L4).

### Prow Logs

What Prow did to my PR.

```code
...
| filter(pr="827")
```

### Audit logs (build01 and build02)

Aggregation:

```
fields @timestamp, @message 
| limit 20 
| stats count() as count by user.username, objectRef.resource
| sort count desc
```

Moving Prometheus data between servers at outtages are not practical/possible: 80G for build02.

## GCP

GCP accounts: https://console.cloud.google.com/

- openshift-ci-build-farm: build farm clusters, such as build02, build04
- openshift-ci-infra: Prow and (decommissioned 3.11) cluster api.ci
- openshift-gce-devel-ci: ephemeral clusters provisioned for CI tests

Services: Compute Engine, VPC Network, Cloud DNS, Logging, etc.

  Cloud DNS: Manage domain "ci.openshift.org" (openshift-ci-infra)


## Cloud DNS

- Own `ci.openshift.org`
- Cert-Manager: manage TLS certificates, e.g., [prow-ingress](https://github.com/openshift/release/blob/62dce99f006bfa6625a5b2b19ee278ea3babb4b0/clusters/app.ci/cert-manager/prow_ingress.yaml#L2)

  `CNAME` or `A` record to the ingress on the cluster:

  ```console
  oc --context app.ci get svc -n openshift-ingress router-default
  NAME             TYPE           CLUSTER-IP      EXTERNAL-IP                                                              PORT(S)                      AGE
  router-default   LoadBalancer   REDACTED   REDACTED.us-east-1.elb.amazonaws.com   80:REDACTED/TCP,443:REDACTED/TCP   671d
  ```

- Base domain of an OCP cluster: `gcp.ci.openshift.org`
- Domain ownership and TLS certificates
