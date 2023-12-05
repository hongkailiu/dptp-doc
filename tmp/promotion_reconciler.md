# promotion reconciler

* No error or above found in `promotion_job_creator` in the last `24h`:

```
fields @timestamp, level,msg,namespace,name,error, @message 
| sort @timestamp desc | filter(component="dptp-controller-manager" and controller="promotion_job_creator" and level!="debug" and level!="info")
```

* Created Prow jobs: 25 / day
```
fields @timestamp, level,msg,namespace,name,error, @message 
| sort @timestamp desc | filter(component="dptp-controller-manager" and controller="promotion_job_creator" and msg="Successfully created prowjob")
```

Going back to `promotionreconciler`:

* Requesting prowjob creation: 99 / day
```
fields @timestamp, level,msg,namespace,name,error, @message 
| sort @timestamp desc | filter(component="dptp-controller-manager" and controller="promotionreconciler" and msg="Requesting prowjob creation")
```
