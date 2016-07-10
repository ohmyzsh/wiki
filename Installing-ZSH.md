## Zsh?

Oh-My-Zsh is a framework for [Zsh](http://www.zsh.org), the Z shell.

- In order for Oh-My-Zsh to work, Zsh must be installed. 
  - Please run `zsh --version` to confirm.
  - Expected result: `zsh 5.2` or more recent
- Additionally, Zsh should be set as your default shell.
  - Please run `echo $SHELL` from a new terminal to confirm.
  - Expected result: `/bin/zsh`

## Installing Zsh

If necessary, follow these steps to install Zsh:

1. There are two main ways to install Zsh
  - with the package manager of your choice (_e.g._ `sudo apt-get install zsh`) or
  - from [source](http://zsh.sourceforge.net/Arc/source.html), following 
        [instructions from the Zsh FAQ](http://zsh.sourceforge.net/FAQ/zshfaq01.html#l7)
2. Verify installation by running `zsh --version`. Expected result: `zsh 5.2` or more recent. 
3. Make it your default shell: `chsh -s $(which zsh)`
  - Note that this will not work if Zsh is not in your authorized shells list (`/etc/shells`)
    or if you don't have permission to use `chsh`. If that's the case [you'll need to use a different procedure](https://www.google.com/search?q=zsh+default+without+chsh).
4. Log out and login back again to use your new default shell. 
5. Test that it worked with `echo $SHELL`. Expected result: `/bin/zsh`
