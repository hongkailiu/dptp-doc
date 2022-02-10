## Summary

- accounts on AWS/GCP and what each of them is for.
- the services TP uses often
- Dive into AWS CloudWatch and Cloud DNS


## AWS
AWS accounts: `https://<account>.signin.aws.amazon.com/console`
  
- openshift-ci-infra: build farm clusters, such as build01, build03
- openshift-ci: ephemeral clusters provisioned for CI tests
- openshift-ci-pools: ephemeral clusters provisioned for CI tests with cluster claims

Services: EC2, VPC, Route53, CloudWatch, etc.

CloudWatch: Prow logs, API server audit logs for build0{1|2} (openshift-ci-infra)

cli: aws

## GCP
GCP accounts: https://console.cloud.google.com/

- openshift-ci-build-farm: build farm clusters, such as build02, build04
- openshift-ci-infra: Prow and (decommissioned 3.11) cluster api.ci
- openshift-gce-devel-ci: ephemeral clusters provisioned for CI tests

Services: Compute Engine, VPC Network, Cloud DNS, Logging, etc.

  Cloud DNS: Manage domain "ci.openshift.org" (openshift-ci-infra)

cli: gcloud
