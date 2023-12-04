

* Created Prow jobs: 99 / day
```
fields @timestamp, level,msg,namespace,name,error, @message 
| sort @timestamp desc | filter(component="dptp-controller-manager" and controller="promotionreconciler" and msg="Requesting prowjob creation")
```
