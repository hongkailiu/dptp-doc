# centos


## centos9 stream

Guest OS on Mac:

```console
$ cat ~/.zshrc |grep centos9
alias centos9='ssh -p 3022 liu@localhost'

$ ssh-copy-id -p 3022 -i ~/.ssh/id_rsa.pub liu@localhost

```


```console
### disable GUI on startup
# systemctl set-default multi-user.target

### enable GUI on startup
# systemctl set-default graphical.target
```
