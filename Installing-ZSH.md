## Zsh?

Oh-My-Zsh is a framework for [Zsh](http://www.zsh.org), the Z shell.

- In order for Oh-My-Zsh to work, Zsh must be installed (v4.3.9 or more recent).
  - Please run `zsh --version` to confirm.
- Additionally, Zsh should be set as your default shell.
  - Please run `echo $SHELL` from a new terminal to confirm.

## Installing oh-my-zsh

If you need to, follow the following step to make it work:

1. Install Zsh
  - with your package manager of choice (_ie_: `sudo apt-get install zsh`)
  - from [source](http://zsh.sourceforge.net/Arc/source.html), following 
        [instructions from the Zsh FAQ](http://zsh.sourceforge.net/FAQ/zshfaq01.html#l7)
2. Make sure it installed by running `zsh --version`
3. Make it your default shell: `chsh -s  $(chsh -l | grep "zsh" -m 1)`
  - Note that this will not work if Zsh is not in your authorized shells list (`/etc/shells`)
4. Re-open all terminals and make sure it worked by running `echo $SHELL`
