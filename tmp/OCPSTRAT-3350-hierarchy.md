# OCPSTRAT-3350 — Hierarchy

**Feature:** OLM/Operator Metadata: Mandatory vs Optional Classification of Related Images for Selective Disconnected Mirroring

Source: [redhat.atlassian.net](https://redhat.atlassian.net/browse/OCPSTRAT-3350) · Feature SP is the roll-up of all epics (50).

| Key | Size | SP | Title |
|---|---|---|---|
| **[OCPSTRAT-3350](https://redhat.atlassian.net/browse/OCPSTRAT-3350)** | L | 50 | OLM/Operator Metadata: Mandatory vs Optional<br>Classification of Related Images for Selective<br>Disconnected Mirroring |
| **[OPRUN-4724](https://redhat.atlassian.net/browse/OPRUN-4724)** | S | 18 | Support the metadata structure for mandatory<br>and optional classification of related images |
| ⤷ [OPRUN-4725](https://redhat.atlassian.net/browse/OPRUN-4725) | | 5 | Define the metadata structure for mandatory and<br>Optional classification of related images |
| ⤷ [OPRUN-4727](https://redhat.atlassian.net/browse/OPRUN-4727) | | 8 | Implement the relatedImageGroups schema extension<br>in operator-registry (alpha/declcfg + opm validate) |
| ⤷ [OPRUN-4728](https://redhat.atlassian.net/browse/OPRUN-4728) | | 2 | Document related image groups in the OLM<br>file-based catalog olm.bundle reference |
| ⤷ [OPRUN-4729](https://redhat.atlassian.net/browse/OPRUN-4729) | | 3 | [optional?] CI check: warn when Red Hat operator<br>bundles declare no optional image groups |
| **[CLID-716](https://redhat.atlassian.net/browse/CLID-716)** | XS | 12 | Extend oc-mirror v2's ImageSetConfiguration<br>to choose optional images |
| ⤷ [CLID-717](https://redhat.atlassian.net/browse/CLID-717) | | 8 | Extend oc-mirror v2's ImageSetConfiguration<br>to choose optional images |
| ⤷ [CLID-719](https://redhat.atlassian.net/browse/CLID-719) | | 1 | Update oc-mirror ImageSetConfiguration example<br>to demo optional image group selection |
| ⤷ [CLID-723](https://redhat.atlassian.net/browse/CLID-723) | | 3 | Extend oc-mirror v2 to discover optional image<br>groups (relatedImageGroups) in a bundle |
| **[OPRUN-4730](https://redhat.atlassian.net/browse/OPRUN-4730)** | XS | 6 | Operator 1: adopt optional-related-image feature |
| ⤷ [OPRUN-4732](https://redhat.atlassian.net/browse/OPRUN-4732) | | 3 | Group optional related images by product<br>features (relatedImageGroups) |
| ⤷ [OPRUN-4733](https://redhat.atlassian.net/browse/OPRUN-4733) | | 3 | Generate olm bundle with the grouped optional<br>related images |
| **[OPRUN-4731](https://redhat.atlassian.net/browse/OPRUN-4731)** | XS | 6 | Operator 2: adopt optional-related-image feature |
| **[OPRUN-4726](https://redhat.atlassian.net/browse/OPRUN-4726)** | XS | 5 | End-to-end tests for mandatory and optional<br>classification of related images |
| **[OSDOCS-20296](https://redhat.atlassian.net/browse/OSDOCS-20296)** | XS | 3 | Docs for OCPSTRAT-3350 OLM/Operator Metadata:<br>Mandatory vs Optional Classification of Related<br>Images for Selective Disconnected Mirroring |
| ⤷ [OSDOCS-21715](https://redhat.atlassian.net/browse/OSDOCS-21715) | | 3 | Document selective mirroring of optional<br>operator image groups (oc-mirror v2) |

## Notes

- Epics are **bold** with a `Size`; child stories/spikes are indented (⤷) with no size.
- Feature SP (50) is a display roll-up: 18 + 12 + 6 + 6 + 5 + 3. The SP field on OCPSTRAT-3350 in Jira is unset.
- `OPRUN-4731` has no `Size` set; `OPRUN-4726` and `OPRUN-4731` have no children yet.
