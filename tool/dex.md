# dex

https://dexidp.io/

## run

```console
$ ll dex/
-rwxrwx--- 1 root vboxsf 4449 May 14 16:03 config-dev.yaml

$ podman run --user=${UID} -v "./dex:/data:z" --entrypoint "dex"  --rm ghcr.io/dexidp/dex:v2.28.1 serve /data/config-dev.yaml


```
