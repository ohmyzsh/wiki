_Work in progress..._

**TODO**

- [ ] Put instructions on how to migrate from `.bash_profile` / `.bashrc` configurations (see [#3807](https://github.com/robbyrussell/oh-my-zsh/issues/3807)).
- [ ] Fill this up.

---

- [How do I install OMZ and Zsh?](#how-do-i-install-omz-and-zsh)
- [How do I uninstall OMZ and Zsh?](#how-do-i-uninstall-omz-and-zsh)

## How do I install OMZ and Zsh?

Please see [[Installing Zsh]] for instructions to install Zsh.

Please see [[Contribution Technical Practices]] for instructions to set up a fork for contributing.

To manually install OMZ in a custom directory, run

```shell
git clone git@github.com:robbyrussell/oh-my-zsh.git /my/custom/directory
```

You will need to add `export ZSH=/my/custom/directory` and `source $ZSH/oh-my-zsh.sh` to your `~/.zshrc`.

## How do I uninstall OMZ and Zsh?

Run `$ZSH/tools/uninstall.sh` to remove OMZ. This will backup your `~/.zshrc` and remove your OMZ install entirely. Then:
- if you have `~/.zshrc.pre-oh-my-zsh`, it is assumed that you had Zsh in use prior to installing OMZ, so your `~/.zshrc.pre-oh-my-zsh` is simply restored
- otherwise it is assumed that you were using Bash, so the default shell will be set to `/bin/bash` and `/etc/profile` will be sourced

Then simply reopen your shells. You must have OMZ installed in the default directory (_ie_ `~/.oh-my-zsh`) for this to work.

Alternatively, to manually remove OMZ do `rm -rf $ZSH` — you will also have to edit your `~/.zshrc`. To manually set a new default shell, do `chsh -s /my/new/shell`, _eg_ `chsh -s /bin/bash`. Then simply reopen your shells.
