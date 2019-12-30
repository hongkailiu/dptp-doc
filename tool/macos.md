# MacOS

## [Set up](https://redhat.service-now.com/help?id=kb_article&sys_id=87e9f72bc91c860076770fb559cc8ad9)
* [Encrypting your drive with FileVault](https://redhat.service-now.com/help?id=kb_article&sysparm_article=KB0000970)
* [python](python.md#on-mac)

## [change default shell](https://www.howtogeek.com/444596/how-to-change-the-default-shell-to-bash-in-macos-catalina/)

iterm2 + zsh + ohmyzsh: [1](https://medium.com/ayuth/iterm2-zsh-oh-my-zsh-the-most-power-full-of-terminal-on-macos-bdb2823fb04c), [2](https://www.freecodecamp.org/news/how-to-configure-your-macos-terminal-with-zsh-like-a-pro-c0ab3f3c1156/);
[auto-completion](https://scriptingosx.com/2019/07/moving-to-zsh-part-5-completions/), [zsh-plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)



```
$ chsh -s /bin/zsh
###change it back
$ chsh -s /bin/bash

```

## brew

```
➜  ~ brew doctor
Your system is ready to brew.

#python-yq: https://pypi.org/project/yq/
#yq: https://mikefarah.github.io/yq/

$ brew install python-yq # not yq
➜  ~ brew install coreutils
```

## golang

```bash
$ brew install go
$ go version
go version go1.13.5 darwin/amd64
```

## Shortcuts

mac keys on windows keyboard
* `⌘`: windows
* `^`: `CTRL`
* `⌥`: `ALT`
* `⇧`: `SHIFT`

### iterm2

**Function** | **Shortcut**
-------- | --------
New tab | `⌘` + `t`
Clear screen | `^` + `l`
Clear buffer | `⌘` + `k`
