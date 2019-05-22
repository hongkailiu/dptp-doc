# build cop

* [OpenShift - Build Cop Responsibilities](https://docs.google.com/document/d/117_0UE5jJI_MyI5ugy1psn0Ls6fWCu-Y9jiZZPM4qzw/edit?ts=5c7d4ca0#)
* [OpenShift - Build Cop Triage](https://docs.google.com/document/d/1yMPat99lwqILIytCn-o6ZSEy1AOwTZBRI0jKqLGD2p8/edit#heading=h.i9cwtxk0yza5)

## success rate on deck

![](i/deck_histogram.png)

Thanks to Petr:

* colored bar: 24h (suc: 78, pen: 11, fai: 41, abo: 33). Success rate: 78/(78+41)=65%.
* histogram: 12h (counting the squares ... suc/green: 16; fai/red: 11). Success rate: 16/(16+11)=59%

Those rates match `Success rate over time: 3h: 50%, 12h: 59%, 48h: 66%`. The only issue is the hovering message `Showing 119 builds from last 12h ...` should be `Showing 27 ...`.

`1h40m+` and `50m` are job durations.
