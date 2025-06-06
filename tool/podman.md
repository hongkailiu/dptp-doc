# podman

## installation on mac

Doc: [here](https://podman.io/docs/installation#macos).

```console
➜  ~ brew install podman
➜  ~ podman -v
podman version 4.5.1

### https://medium.com/@butkovic/favoring-podman-over-docker-desktop-33368e031ba0
### mount $HOME/repo/openshift/release to the machine
➜  ~ podman machine init --cpus=4 --disk-size=100 --memory=8192 -v "$HOME/repo:$HOME/repo"
➜  ~ podman machine start
Starting machine "podman-machine-default"
Waiting for VM ...
Mounting volume... /Users/hongkliu/repo:/Users/hongkliu/repo
...
➜  ~ podman info

➜  ~ podman run -v /Users/hongkliu/repo/openshift/release:/tmp/release ubuntu ls /tmp/release
CONTRIBUTING.md
...

### To delete the machine
➜  ~ podman machine rm
```

```console
$ podman -v
podman version 5.1.1

# default auth path: /Users/hongkliu/.config/containers/auth.json
$ podman login registry.redhat.io -p ${PODMAN_PASSWORD_GMAIL} -u ${PODMAN_USERNAME_GMAIL} -v
Used:  /Users/hongkliu/.config/containers/auth.json
Login Succeeded!
```

## run x86-64 images on arm64 hosting

(Seem no need of those steps for `podman version 5.1.1`)

Doc: [here](https://edofic.com/posts/2021-09-12-podman-m1-amd64/)

```console
➜  ~ podman machine ssh
➜  ~ sudo -i
➜  ~ rpm-ostree install qemu-user-static
➜  ~ systemctl reboot
```


## troubleshooting

Sometimes, we need to restart the machine to make the volume accessible to the container

```
➜  ~ podman machine stop
➜  ~ podman machine start
```

The volume bind option SELinux `:z` and `:Z` for example, `--volume "$PWD:/tmp/release:z"`, has [not been supported on Mac](https://github.com/containers/podman/issues/13631#issuecomment-1077643246). We need to remove it to run the command.
