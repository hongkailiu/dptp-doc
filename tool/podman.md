# podman

## installation on mac

Doc: [here](https://podman.io/docs/installation#macos).

```console
➜  ~ brew install podman
➜  ~ podman -v
podman version 4.5.1

### https://medium.com/@butkovic/favoring-podman-over-docker-desktop-33368e031ba0
### mount $HOME/repo/openshift/release to the machine
➜  ~ podman machine init --cpus=4 --disk-size=100 --memory=8192 -v "$HOME/repo/openshift/release:$HOME/repo/openshift/release"
➜  ~ podman machine start
➜  ~ podman info
```


## run x86-64 images on arm64 hosting

Doc: [here](https://edofic.com/posts/2021-09-12-podman-m1-amd64/)

```console
➜  ~ podman machine ssh
➜  ~ sudo -i
➜  ~ rpm-ostree install qemu-user-static
➜  ~ systemctl reboot
```
