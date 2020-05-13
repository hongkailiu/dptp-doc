# AWS CloudWatch

## Insights
[QuerySyntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)

```
fields @timestamp, @message, level
| sort @timestamp desc
| filter(level = "error" or level = "warning" or level = "fatal")
| filter(component != "entrypoint" and component != "sidecar" and component != "clonerefs" and component != "initupload" and component != "checkconfig" and component != "image")
| filter(not (msg=~"Failed to GET ." or 
              msg=~"The following repos define a policy or require context" or 
              msg=~"Trequested job is unknown to prow: rehearse" or 
              msg=~"requested job is unknown to prow: promote" or
              msg=~"Not enough reviewers found in OWNERS files for files touched by this PR" or
              msg=~"failed to get path: failed to resolve sym link: failed to read" or
              msg=~"nil pointer evaluating *v1.Refs.Repo" or
              msg=~"unrecognized directory name (expected int64)" or
              msg=~"failed to get reader for GCS object: storage: object doesn't exist" or
              error=~"failed to get reader for GCS object: storage: object doesn't exist" or
              error=~"googleapi: Error 401: Anonymous caller does not have storage.objects.list access to origin-ci-private., required" or
              msg=~"has required jobs but has protect: false" or
              msg=~"Couldn't find/suggest approvers for each files." or
              msg=~"remote error: upload-pack: not our ref" or
              msg=~"fatal: remote error: upload-pack: not our ref" or
              msg=~"Error getting ProwJob name for source" or
              msg=~"the cache is not started, can not read objects" or
              msg=~"owner mismatch request by" or
              msg=~"Get : unsupported protocol scheme" or
              msg=~"No available resource" or
              error=~"context deadline exceeded" or
              #msg=~"The `pr_status_base_url` setting is deprecated and it has been replaced by `pr_status_base_urls`. It will be removed in June 2020" or
              error=~"owner mismatch request by ci-op"
              )  )
```
