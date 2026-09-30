# Selective mirroring of related images — current design (core)

**Feature:** [OCPSTRAT-3755](https://redhat.atlassian.net/browse/OCPSTRAT-3755) (formerly OCPSTRAT-3350)  
**Design source:** [OPRUN-4725](https://redhat.atlassian.net/browse/OPRUN-4725) (metadata), [OPRUN-4764](https://redhat.atlassian.net/browse/OPRUN-4764) (CSV), [CLID-717](https://redhat.atlassian.net/browse/CLID-717) (oc-mirror)  
**Status:** Proposed; not yet SME-approved or implemented

---

## Problem (one line)

Disconnected users must mirror every related image an operator declares, even for product features they will never enable.

## Core idea

1. **Authors** attach optional Kubernetes **labels** to related images (in the bundle / CSV).
2. **Administrators** choose which labeled images to mirror with Kubernetes **label selectors** in `ImageSetConfiguration`.

There is no separate “group” object and no explicit mandatory/optional flag.  
**Labeled ⇒ skippable. Unlabeled ⇒ always required.**

## Operator Author — metadata

Optional field on each related image: `labels` (`map[string]string`), Kubernetes label syntax. Example: [serverless-operator PR #4186](https://github.com/openshift-knative/serverless-operator/pull/4186/changes#diff-5a9371d1cdfd376365aba4ae0d4297d8d9d4e0fd85cc6d8886a4b79059b66f73).

Same field in:

- FBC `olm.bundle` `relatedImages[]` (catalog)
- CSV `spec.relatedImages[]` (authoring)

```yaml
schema: olm.bundle
package: foo
name: foo.v0.3.0
image: quay.io/example-com/foo-bundle:v0.3.0
relatedImages:
  - name: operator
    image: quay.io/example-com/foo-operator:v0.3.0
    # labels are optional

  - name: shared-operand
    image: quay.io/example-com/shared:v0.3.0
    labels:
      CoolFeatureA: "true"
      GreatFeatureB: "true"   # one image, multiple features
```

**Rules**

| Rule | Meaning |
|------|---------|
| Field is optional | Bundles without `labels` behave exactly as today |
| Existing fields unchanged | `name` / `image` keep their current meaning |
| Multi-label OK | An image can belong to several features |
| Semantics for consumers | Labels are opaque to OLM; tools (e.g. oc-mirror) interpret them |

---

## Administrator side — oc-mirror selection

Per package in `ImageSetConfiguration`, optional `selectors` (`[]metav1.LabelSelector`).

```yaml
apiVersion: mirror.openshift.io/v2alpha1
mirror:
  operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.18
    packages:
    # Include path: CoolFeatureA OR (GreatFeatureB AND tier=frontend AND version=1.2.3)
    - name: aws-load-balancer-operator
      selectors:
      - matchExpressions:
        - key: CoolFeatureA
          operator: Exists
      - matchLabels:
          version: "1.2.3"
        matchExpressions:
        - key: GreatFeatureB
          operator: Exists
        - key: tier
          operator: In
          values: ["frontend"]

    # Exclude path: everything except CoolFeatureC
    - name: 3scale-operator
      selectors:
      - matchExpressions:
        - key: CoolFeatureC
          operator: DoesNotExist

    # No selectors: only unlabeled images
    - name: node-observability-operator
```

**Selection rules**

| Rule | Meaning |
|------|---------|
| Within one selector | AND (`matchLabels` + `matchExpressions`) |
| Across selectors on a package | OR (union) |
| Image with **no** labels | Always selected |
| Image with labels | Selected only if a package selector matches it |
| **No selectors** on a package | Mirror **only unlabeled** related images for that package |
| Across bundles | If any selected bundle needs the image, it is mirrored |
| Skip logging | Log each skipped image (pull spec required; reason nice-to-have) |

---

## Gaps and Impact

**Out of this iteration**

- Named group objects with human-readable title / description per feature
- Explicit mandatory flag on an image
- Built-in discovery CLI for available features ([CLID-723](https://redhat.atlassian.net/browse/CLID-723))
- CI check: warn when Red Hat operator bundles declare no image labels ([OPRUN-4729](https://redhat.atlassian.net/browse/OPRUN-4729))

**Impact:** Once an operator *starts* labeling images, existing ImageSetConfigurations that omit `selectors` will **stop** mirroring those labeled images until selectors are added. Catalogs that never adopt labels stay fully compatible.

---

## PoC with 2 operators

Proxy measurement: related images from a catalog bundle were listed as `additionalImages` in ImageSetConfigurations (all vs unlabeled/mandatory only), then mirrored with oc-mirror v2. Catalog: `registry.redhat.io/redhat/redhat-operator-index:v4.22`.

Sources: [OPRUN-4765](https://redhat.atlassian.net/browse/OPRUN-4765) (CNV), [OPRUN-4766](https://redhat.atlassian.net/browse/OPRUN-4766) (Serverless).

| Operator | Bundle (images) | Label source | Images (all → mandatory) | Disk (all → mandatory) | Savings |
|----------|-----------------|--------------|--------------------------|------------------------|---------|
| CNV (kubevirt-hyperconverged) | `kubevirt-hyperconverged-operator.v4.22.8` | [CNV labeling scheme](https://docs.google.com/spreadsheets/d/1QoJOlcAfd0hFhJRubabrbj7wVBOcxo9l2XD5mejiYwQ/edit?usp=sharing) used for the test ISCs | 69 → 52 | 12G → 9.5G | ~2.5G (~21%) |
| Serverless | `serverless-operator.v1.35.0` | Labels from [CSV v1.38.0](https://raw.githubusercontent.com/dsimansk/serverless-operator/339b2ec32dfd992d86ef92064e9e0aa3c25c6771/olm-catalog/serverless-operator/manifests/serverless-operator.clusterserviceversion.yaml) | 50 → 9 | 10G → 3.0G | ~7G (~70%) |

No data yet from the operator authors for the typical/realistic selectors.


**Concerns** (CNV team): operational overhead on operator authors from labeling the images, and risk of missing images at runtime; skipping versions wisely is a more natural solution but it turns out technically difficult.

## Future size
OCPSTRAT-3755 t-shirt size: L (3-4 Sprint).

Closed children excluded. Epic SP is the sum of open children’s story points (Jira value used only when an epic has no open children).

```
OCPSTRAT-3755 SP=—  [Spike OPRUN-4753] OLM/Operator Metadata: Mandatory vs Optional Classification of Related Images for Selective Disconnected Mirroring
├─ CLID-716 SP=9  Extend oc-mirror v2's ImageSetConfiguration to choose optional images
│  ├─ CLID-717 SP=8  Extend oc-mirror v2's ImageSetConfiguration to choose images
│  └─ CLID-719 SP=1  Update oc-mirror ImageSetConfiguration example to demo label selectors on related images
├─ OPRUN-4724 SP=17  Support the metadata structure for classification of related images by labels
│  ├─ OPRUN-4725 SP=5  Define the metadata structure for classification of related images
│  ├─ OPRUN-4727 SP=8  Implement the relatedImages.labels schema extension in operator-registry (alpha/declcfg + opm validate)
│  ├─ OPRUN-4728 SP=2  Document related image labels in the OLM file-based catalog olm.bundle reference
│  └─ OPRUN-4764 SP=2  Extend RelatedImage in CSV.spec with labels
├─ OPRUN-4726 SP=5  End-to-end tests for classification of related images
├─ OPRUN-4730 SP=6  Operator 1 (kubevirt-hyperconverged): adopt optional-related-image feature
│  ├─ OPRUN-4732 SP=3  Label related images by product features
│  └─ OPRUN-4733 SP=3  Generate olm bundle with labels on related images
├─ OPRUN-4731 SP=6  Operator 2 (serverless-operator): adopt optional-related-image feature
├─ OSDOCS-20296 SP=3  Docs for OCPSTRAT-3350 OLM/Operator Metadata: Labeling Related Images for Selective Disconnected Mirroring
│  ├─ OSDOCS-21715 SP=3  Document selective mirroring of operator images (oc-mirror v2)
│  └─ OSDOCS-22742 SP=—  Document the labels field of relatedImages in the olm.bundle schema reference
└─ SRVCOM-5208 SP=—  [Serverless] Spike - Serverless Operator Mandatory vs. Optional images for OLM
```

Epic SP sum: 46.