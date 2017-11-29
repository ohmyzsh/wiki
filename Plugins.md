Enable the plugins you want by editing your 
[*~/.zshrc*](https://github.com/robbyrussell/oh-my-zsh/blob/master/templates/zshrc.zsh-template#L48) file.

##### _Example:_
```shell
plugins=(rails git ruby)
```

_Completion plugins_ will let zsh know which arguments the package has so it can autocomplete. For instance, if you have the Homebrew plugin installed and type:

```
brew in
```

.. and then hit tab, the *brew* plugin will enable autocompletion to *brew install*. Completion plugins are not documented further on this page as they only provide better introspection for zsh into the original command. *man* is your friend.

You should always read the source for the plugin before using it to avoid surprises. Plugins are located in ~/.oh-my-zsh/plugins.

Below is a list of bundled plugins

- [apache2-macports](#apache2-macports)
- [archlinux](#archlinux)
- [asdf](#asdf)
- [aterminal](#aterminal)
- [autojump](#autojump)
- [autopep8](#autopep8)
- [aws](#aws)
- [bower](#bower)
- [brew](#brew)
- [bundler](#bundler)
- [cabal](#cabal)
- [cake](#cake)
- [capistrano](#capistrano)
- [cask](#cask)
- [catimg](#catimg)
- [celery](#celery)
- [chruby](#chruby)
- [chucknorris](#chucknorris)
- [command-not-found](#command-not-found)
- [Composer](#composer)
- [cloudapp](#cloudapp)
- [coffee](#coffee)
- [common-aliases](#common-aliases)
- [compleat](#compleat)
- [cpanm](#cpanm)
- [debian](#debian)
- [dircycle](#dircycle)
- [dirhistory](#dirhistory)
- [dirpersist](#dirpersist)
- [django](#django)
- [dnf](#dnf)
- [docker](#docker)
- [encode64](#encode64)
- [fabric](#fabric)
- [fbterm](#fbterm)
- [Forklift](#forklift)
- [fasd](#fasd)
- [gas](#gas)
- [geeknote](#geeknote) 
- [gem](#gem)
- [gpg-agent](#gpg-agent)
- [git](#git)
- [gitfast](#gitfast)
- [git-extras](#git-extras)
- [git-flow](#git-flow)
- [git-flow-avh](#git-flow-avh)
- [git-hubflow](#git-hubflow)
- [git_remote_branch](#git_remote_branch)
- [github](#github)
- [gradle](#gradle)
- [grails](#grails)
- [httpie](#httpie)
- [history](#history)
- [jira](#jira)
- [jsontools](#jsontools)
- [knife](#knife)
- [laravel4](#laravel4)
- [last-working-dir](#last-working-dir)
- [lein](#lein)
- [lighthouse](#lighthouse)
- [lol](#lol)
- [macports](#macports)
- [mercurial](#mercurial)
- [meteor](#meteor)
- [mvn](#mvn)
- [mysql-macports](#mysql-macports)
- [nanoc](#nanoc)
- [ng](#ng)
- [node](#node)
- [npm](#npm)
- [nyan](#nyan)
- [osx](#osx)
- [pass](#pass)
- [per-directory-history](#per-directory-history)
- [perl](#perl)
- [perms](#perms)
- [pep8](#pep8)
- [phing](#phing)
- [pip](#pip)
- [pod](#pod)
- [pow](#pow)
- [powify](#powify)
- [pyenv](#pyenv)
- [pylint](#pylint)
- [python](#python)
- [rails](#rails)
- [rand-quote](#rand-quote)
- [redis-cli](#redis-cli)
- [repo](#repo)
- [ruby](#ruby)
- [rvm](#rvm)
- [sbt](#sbt)
- [scala](#scala)
- [screen](#screen)
- [sprunge](#sprunge)
- [ssh-agent](#ssh-agent)
- [sublime](#sublime)
- [sudo](#sudo)
- [supervisor](#supervisor)
- [suse](#suse)
- [svn](#svn)
- [svn-fast-info](#svn-fast-info)
- [symfony2](#symfony2)
- [systemd](#systemd)
- [taskwarrior](#taskwarrior)
- [terminalapp](#terminalapp)
- [terminitor](#terminitor)
- [textmate](#textmate)
- [tig](#tig)
- [thor](#thor)
- [tmux](#tmux)
- [tmuxinator](#tmuxinator)
- [tugboat](#tugboat)
- [urltools](#urltools)
- [vagrant](#vagrant)
- [vi-mode](#vi-mode)
- [virtualenvwrapper](#virtualenvwrapper)
- [web-search](#web-search)
- [yarn](#yarn)
- [yii](#yii)
- [yii2](#yii2)
- [yum](#yum)
- [zeus](#zeus)
- [wd](#wd)

## apache2-macports

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Enables aliases to control a local Apache2 installed via [Macports](http://www.macports.org/).

| Command          | Description    |
|:-----------------|:---------------|
| _apache2start_   | Start Apache   |
| _apache2stop_    | Stop Apache    |
| _apache2restart_ | Restart Apache |

---

## archlinux

**Maintainer:** [Benjamin Boudreau](https://github.com/seriousben)

Enabled [aliases](https://wiki.archlinux.org/index.php/Pacman_Tips) for `pacman` (replace `pac` by `ya` for `yaourt`)

| Alias     | Description                                                                               |
|:----------|:------------------------------------------------------------------------------------------|
| _pacin_   | Install specific package(s) from the repositories                                         |
| _pacins_  | Install specific package not from the repositories but from a file                        |
| _pacre_   | Remove the specified package(s), retaining its configuration(s) and required dependencies |
| _pacrem_  | Remove the specified package(s), its configuration(s) and unneeded dependencies           |
| _pacrep_  | Display information about a given package in the repositories                             |
| _pacreps_ | Search for package(s) in the repositories                                                 |
| _pacloc_  | Display information about a given package in the local database                           |
| _paclocs_ | Search for package(s) in the local database                                               |
| _pacupd_  | Update and refresh the local package and ABS databases against repositories               |
| _pacupg_  | Update the local database and upgrade packages                                            |
| _pacinsd_ | Install given package(s) as dependencies of another package                               |
| _pacmir_  | Force refresh of all package lists after updating /etc/pacman.d/mirrorlist                |

| Function                 | Description                                                                                                        |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------|
| _paclist_                |  List all installed packages with a short description - [Source](https://bbs.archlinux.org/viewtopic.php?id=93683) |
| _paclsorphans_           | List all orphaned packages                                                                                         | 
| _pacrmorphans_           | Delete all orphaned packages                                                                                       |
| _pacdisowned \| less +F_ | List all disowned files in your system                                                                             |

---

## asdf

A plugin for the _extendable version manager_ [asdf](https://github.com/asdf-vm/asdf).
See the [README](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/asdf) for usage information.

**Maintainer:** [RobLoach](https://github.com/RobLoach)

---

## aterminal

**Maintainer:** [guiferpa](https://github.com/guiferpa)

## Description
This plugin show platforms version

## Support
[Nodejs](https://nodejs.org), [NPM](https://www.npmjs.com), [Docker](https://www.docker.com), [Go](https://golang.org), [Python](https://www.python.org), [Elixir](https://elixir-lang.org) and [Ruby](https://www.ruby-lang.org)

## Demo
![Demo](https://raw.githubusercontent.com/guiferpa/aterminal/master/images/demo.gif)

## Install
1. You need to install [Oh My ZSH](https://github.com/robbyrussell/oh-my-zsh)
2. Clone plugin: `git clone https://github.com/guiferpa/aterminal.git`
3. Move to plugins directory: `mv aterminal $HOME/.oh-my-zsh/plugins/`
4. Add plugin in `nano $HOME/.zshrc`
---

## autojump

Enables [autojump](https://github.com/joelthelion/autojump/wiki/) if installed with homebrew, macports or debian/ubuntu package.

This does not add any commands on its own.

---

## autopep8

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Completion for the python file formatting (PEP8) tool

---

## aws

**Maintainer:** [Cristian Măgherușan-Stanciu](https://github.com/cristim)

Activates the ZSH completion plugin shipped together with the [aws command-line tool](http://aws.amazon.com/cli/)

| Alias | Description                                                                                                                                                                 |
|:------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asp   | Choose the current AWS credentials profile from those defined in .aws/config, with auto-completion support. Also makes the currently set profile to be shown in the RPROMPT. |
| agp   | Print the currently set AWS credentials profile.                                                                                                                            |

---

## bower

**Maintainer:** [miklos-martin](https://github.com/miklos-martin)

Bower is a package manager for the web. This plugin provides some aliases and completions for this great tool.

### Aliases

| Alias | Description                             |
|:------|:----------------------------------------|
| _bi_  | installs a package (`bower install`)    |
| _bl_  | lists installed packages (`bower list`) |
| _bs_  | searches for packages (`bower search`)  |

### Completion

It completes the basic commands for bower. It uses the `bower help` command to achieve this, not a burned-in list of commands. It also provides completion for bower install, uses the output of bower search. It takes a few seconds for the first time (in the session), but then the output of `bower search` is cached, so things then speed up a lot.

##### _Example: to install jquery for example_
```shell
bi jq<TAB>
```

---

## brew

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

[[Homebrew|http://mxcl.github.com/homebrew/]] is an OS X package manager

This plugin:

* creates a `brews` alias to list installed brews (= `brew list -1`)
* adds completion for the `brew` command.

_Note: With the advent of their 1.0 release, Homebrew has decided to bundle
  the zsh completion as part of the brew installation, so we no longer
  ship it with the brew plugin; now it only has brew aliases._

---

## bundler

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Enables aliases to [Bundler](http://gembundler.com/).

| Alias | Description                                                 |
|:------|:------------------------------------------------------------|
| be    | Bundle exec, execute a command in the context of the bundle |
| bi    | Bundle install                                              |
| bu    | Bundle update                                               |

Also creates shell aliases so you don't have to type "bundle exec" before most common ruby commands when you are in a directory with a Gemfile. Here is a [list of commands](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/bundler/bundler.plugin.zsh#L9) it does this for: `annotate cap capify cucumber ey foreman guard heroku middleman nanoc rackup rainbows rails rake rspec ruby shotgun spec spork thin thor unicorn unicorn_rails`

---

## cabal

**Maintainer:** [telser](https://github.com/telser)

- cabal -- auto-completion for [Cabal](http://haskell.org/cabal) a build tool for [Haskell](http://haskell.org).

---

## cake

**Maintainer:** [serby](https://github.com/serby)

Commands for [Cake](http://jashkenas.github.com/coffee-script/#cake), the coffee-script build tool.

- cake -- auto complete for cake tasks

---

## capistrano

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Commands for [Capistrano](https://github.com/capistrano/capistrano/wiki), a deployment tool built in Ruby.

- cap -- a few commands for Capistrano, a deployment tool built in Ruby

---

## cask

**Maintainer:** [mcornella](https://github.com/mcornella)

Loads completion from non-standard locations for [`cask`, a project management tool
for Emacs](https://github.com/cask/cask).

For more information see [the README](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/cask).

---

## catimg

**Maintainer:** [posva](https://github.com/posva/)

**Original repo:** [catimg.git](https://github.com/posva/catimg)

Print pictures to the `stdout` using `convert` [ImageMagick](http://www.imagemagick.org/)

Example usage `catimg image.png` options:

- `-h` -- print help
- `-w` -- select output width
- `-c` -- change printed character (default `"  "` without the quotes)

---

## celery

**Maintainer:** [dongweiming](https://github.com/dongweiming)

Commands for [celery](https://github.com/celery/celery), a distributed task queue.

### Completion

##### _View worker have those parameter options_
```
celery worker<TAB>
```

---

## chruby

**Maintainer** [webframp](https://github.com/webframp)

Loads [chruby](https://github.com/postmodern/chruby), a simple ruby version manager, if installed, and provides `chruby_prompt_info` variable for theme use.

Commands:

- `rubies: list installed rubies or change current ruby`

You can manually specify the path to load chruby from using zstyle:

- `zstyle :omz:plugins:chruby path`
- `zstyle :omz:plugins:chruby auto`

Simple build definition completion is also provided for [ruby-build](https://github.com/sstephenson/ruby-build) to make installed rubies from source faster.

---

## chucknorris

**Maintainers:** [apjanke](https://github.com/apjanke) [maff](https://github.com/maff)

Adds Chuck Norris fortune file from http://www.k-lug.org/~kessler/projects.html. Depends on fortune (and cowsay if using `chuck_cow`) being installed (available via homebrew, apt, ...). Perfectly suitable as MOTD.

| Command     | Description                     |
|:------------|:--------------------------------|
| _chuck_     | print random Chuck Norris quote |
| _chuck_cow_ | print quote in cowthink         |

##### _Example: output of `chuck_cow` command_
```
Last login: Fri Jan 30 23:12:26 on ttys001
 ______________________________________
( When Chuck Norris plays Monopoly, it )
( affects the actual world economy.    )
 --------------------------------------
        o   ^__^
         o  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

---

## command-not-found

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Only for Ubuntu and openSUSE: If a command is not recognized in the $PATH, this will use Ubuntu's command-not-found package to find it or suggest spelling mistakes:

```shell
~$ gedit
The program 'gedit' is currently not installed. You can install it by typing:
sudo apt-get install gedit
bash: gedit: command not found
```

The plugin uses the command-not-found package zsh support.

---

## Composer

**Maintainer:** [danielcsgomes](https://github.com/danielcsgomes)

[Composer](http://getcomposer.org/) autocomplete plugin with useful aliases:

| Alias  | Command                                 |
|:-------|:----------------------------------------|
| _c_    | composer                                |
| _csu_  | composer self-update                    |
| _cu_   | composer update                         |
| _ci_   | composer install                        |
| _ccp_  | composer create-project                 |
| _cget_ | (installs composer on the current path) |

---

## cloudapp

**Maintainer:** [matthewmccullough](http://github.com/matthewmccullough)

Uploads files and piped contents to the [Cloudapp](http://getcloudapp.com/) service. Outputs and copies the resultant URL to the clipboard. Uses the cloudapp ruby gem from @holman.

---

## coffee

**Maintainer:** [jdavis](https://github.com/jdavis)

Completion plugin for [CoffeeScript](http://coffeescript.org/).

For available options, look at the [usage](http://coffeescript.org/#usage) or run the command `coffee --help`.

---

## common-aliases

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Collection of useful zsh aliases, not enabled by default since they may change some user defined aliases.

| Alias   | Command                      |
|:--------|:-----------------------------|
| _l_     | ls -lFh                      |
| _la_    | ls -lAFh                     |
| _lr_    | ls -tRFh                     |
| _lt_    | ls -ltFh                     |
| _ll_    | ls -l                        |
| _ldot_  | ls -ld .*                    |
| _lS_    | ls -1FSsh                    |
| _lart_  | ls -1Fcart                   |
| _lrt_   | ls -1Fcrt                    |
| _zshrc_ | $EDITOR ~/.zshrc             |
| _h_     | history                      |
| _p_     | (processes for current user) |

##### _Alias to place at the end of command:_
| Alias | Command                   |
|:------|:--------------------------|
| _H_   | \| head                   |
| _T_   | \| tail                   |
| _G_   | \| grep                   |
| _L_   | \| less                   |
| _M_   | \| most                   |
| _LL_  | 2>&1 \| less              |
| _CA_  | 2>&1 \| cat -A            |
| _NE_  | 2> /dev/null              |
| _NUL_ | > /dev/null 2>&1          |
| _P_   | 2>&1\| pygmentize -l pytb |

- Interactive mode for rm, cp, mv
- Completion for the python interpreter

---

## compleat

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion for human beings. **Further documentation needed**

See this [blog post about compleat](http://limpet.net/mbrubeck/2009/10/30/compleat.html)

---

## cpanm

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion plugin for [cpanminus](https://github.com/miyagawa/cpanminus/)

---

## debian

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

A set of aliases to work with the Debian Advanced Packaging Tool, apt.

This plugin use aptitude if installed, or apt-get if not.
You can just set `apt_pref='apt-get'` to override it.

| Alias                      | Description                                                       |
|:---------------------------|:------------------------------------------------------------------|
| _as_ [search term]         | Search for packages                                               |
| _ad_                       | Update packages                                                   |
| _adg_                      | Updgrade packages                                                 |
| _ai_ [packages to install] | Install package(s)                                                |
| _ar_ [package to remove]   | Remove package                                                    |
| _app_                      | Apt policy                                                        |
| _acs_ [search term]        | Search packages in cache                                          |
| _ac_                       | Clean apt cache                                                   |
| _age_ [parameters]         | apt-get [parameters]                                              |
| _api_ [parameters]         | aptitude [parameters]                                             |
| _aps_ [search term]        | Search with aptitude                                              |
| _afs_ [search term]        | Search files in packages                                          |
| _asrc_ [parameters]        | apt-get source [parameters]                                       |
| _aac_   			         | Autoclean                                                         |
| _abd_   			         | Build dependencies                                                |
| _adu_   			         | Update & (safe)upgrade                                            |
| _afu_   			         | Update & full-upgrade                                             |
| _ag_   			         | Upgrade (safe)                                                    |
| _ail_ [list of packages]   | Install all packages in list                                      |
| _ap_   			         | Purge                                                             |
| _ads_   			         | Dselect upgrade                                                   |
| _dia_   			         | Install all ./*.deb                                               |
| _di_ [glob]  			     | Install all glob                                                  |
| _kclean_   		         | Remove unused kernel images                                       |
| _allpkgs_   		         | Print all installed packages                                      |
| _mydeb_   		         | Create .deb package                                               |
| _apt-list-packages_        | List packages by size                                             |
| _kerndeb_ 		         | Kernel-package building shortcut                                  |
| _apt-copy_ 		         | Creates script to install all current packages on other machine   |
| _apt-history_ 	         | Prints apt history                                                |

---

## dircycle

This is a small zle trick that lets you cycle your directory stack left or right using Ctrl+Shift+Left/Right. This is useful when moving back and forth between directories in development environments, and can be thought of as kind of a nondestructive pushd/popd.

---

## dirhistory

**Maintainer:** [jeffwilliams][jeffwilliams]

This plugin allows you to navigate the history of previous current-working-directories using ALT-LEFT and ALT-RIGHT. ALT-LEFT moves back to directories that the user has changed to in the past, and ALT-RIGHT undoes ALT-LEFT.

For example, if the shell was started, and the following commands were entered:

```shell
cd ~
cd /usr
cd share
cd doc
```

Then entering ALT-LEFT at the prompt would change directory from /usr/share/doc to /usr/share, then if pressed again to /usr/, then ~. If ALT-RIGHT were pressed the directory would be changed to /usr/ again.

Currently the max history size is 100. The navigation should work for xterm, PuTTY xterm mode, and GNU screen.

---

## dirpersist

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- dirpersist

---

## django

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Adds completion for [django and `manage.py`](https://www.djangoproject.com/).
[See for more info](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/django).

---

## dnf

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

| Alias | Command                 | Description              |
|-------|-------------------------|--------------------------|
| dnfl  | `dnf list`              | List packages            |
| dnfli | `dnf list installed`    | List installed packages  |
| dnfgl | `dnf grouplist`         | List package groups      |
| dnfmc | `dnf makecache`         | Generate metadata cache  |
| dnfp  | `dnf info`              | Show package information |
| dnfs  | `dnf search`            | Search package           |
| **Use `sudo`**                                             |
| dnfu  | `sudo dnf upgrade`      | Upgrade package          |
| dnfi  | `sudo dnf install`      | Install package          |
| dnfgi | `sudo dnf groupinstall` | Install package group    |
| dnfr  | `sudo dnf remove`       | Remove package           |
| dnfgr | `sudo dnf groupremove`  | Remove package group     |
| dnfc  | `sudo dnf clean all`    | Clean cache              |

See the [README](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/dnf/) for more information.

---

## docker

**Maintainer:** [Azaan](http://github.com/AeonAxan)

- Auto complete arguments and options for all docker commands.
- Show containerIDs and Images for tab completion where applicable ([screenshots](https://github.com/AeonAxan/oh-my-zsh/blob/master/plugins/docker/README.md))

---

## encode64

**Maintainer:** [fuksito](http://github.com/fuksito)

This is a plugin that helps to encode/decode strings with base64 from the console quickly:

| Command    | Description   |
|:-----------|:--------------|
| _encode64_ | encode string |
| _decode64_ | decode string |

##### _Example:_
```shell
$ encode64 some_string
=> c29tZV9zdHJpbmc=

$ decode64 c29tZV9zdHJpbmc=
=> some_string
```

---

## fabric

**Maintainer:** [santiycr](https://github.com/santiycr)

- fabric - completion plugin for [fabric](http://docs.fabfile.org/)

---

## fbterm

- fbterm - automatically start fbterm when running in /dev/tty*

---

## Forklift

**Maintainer:** [bitboxer](https://github.com/bitboxer)

| Command         | Description                                                             |
|:----------------|:------------------------------------------------------------------------|
| _fl_ [<folder>] |  Opens specified directory or current working directory in ForkLift.app |

---

## fasd

**Maintainer:** [a-b](https://github.com/a-b)

- [fasd](https://github.com/clvv/fasd) - command-line productivity booster, offers quick access to files and directories, inspired by autojump, z and v

---

## gas

- gas - completion plugin for the [gas](https://github.com/walle/gas) gem

---

## geeknote 

**Maintainer:** [Ján Koščo](https://github.com/s7anley)

See the [README](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/geeknote) for more info.

---

## gem

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- gem - completion plugin for the gem command

---

## gpg-agent

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

| Command     | Description                                                                               |
|:------------|:------------------------------------------------------------------------------------------|
| _gpg-agent_ | starts gpg-agent (with ssh support) if not running and includes its environment variables |

---

## git

**Maintainers:** [@Stibbons](https://github.com/Stibbons), [@ncanceill](https://github.com/ncanceill)

Adds a lot of git aliases and functions for pulling for dealing with the current branch. See the dedicated [Wiki page](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git), or a list of some of the aliases introduced [here *(OUTDATED)*](http://jasonm23.github.com/oh-my-git-aliases.html).

---

## gitfast

**Maintainer:** [felipec](https://github.com/felipec)

Enables the zsh completion from git.git folks, which is much faster than the official one from zsh. A lot of zsh-specific features are not supported, like descriptions for every argument, but everything the bash completion has, this one does too (as it is using it behind the scenes). Not only is it faster, it should be more robust, and updated regularly to the latest git upstream version.

---

## git-extras

**Maintainer:** [agrimaldi](https://github.com/agrimaldi)

git-extras - Support for [git-extras](https://github.com/visionmedia/git-extras) completion

Pressing tab after the various commands should autofill authors, branches and tags depending on context.

| Command                     | Description                                                                   |
|:----------------------------|:------------------------------------------------------------------------------|
| _git changelog_ [-l/--list] | populate changelog file with commits since the previous tag                   |
| _git contrib_               | display author contributions                                                  |
| _git count_ [--all]         | count commits                                                                 |
| _git delete-branch_         | delete local and remote branch                                                |
| _git delete-submodule_      | delete submodule                                                              |
| _git delete-tag_            | delete local and remote tag                                                   |
| _git extras_ [-v/--version] | git-extras                                                                    |
| _git graft_                 | merge commits from source branch to destination branch                        |
| _git squash_                | merge commits from source branch into the current one as a single commit      |
| _git feature_ [finish]      | create a feature branch                                                       |
| _git refactor_ [finish]     | create a refactor branch                                                      |
| _git bug_ [finish]          | create a bug branch                                                           |
| _git summary_               | repository summary                                                            |
| _git effort_ [--above]      | display effort statistics                                                     |
| _git repl_                  | read-eval-print-loop                                                          |
| _git commits-since_         | list commits since a given date                                               |
| _git release_               | release commit with the given tag                                             |
| _git alias_                 | define, search and show aliases                                               |
| _git ignore_                | add patterns to .gitignore                                                    |
| _git info_                  | show info about the repository                                                |
| _git create-branch_         | create local and remote branch                                                |
| _git fresh-branch_          | create empty local branch                                                     |
| _git undo_                  | remove the latest commit                                                      |
| _git setup_                 | setup a git repository                                                        |
| _git touch_                 | one step creation of new files                                                |
| _git obliterate_            | Completely remove a file from the repository, including past commits and tags |
| _git local-commits_         | list unpushed commits on the local branch                                     |

---

## git-flow

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- git-flow - Support for [git-flow](https://github.com/nvie/gitflow) completion

---

## git-flow-avh

**Maintainer:**

- git-flow-avh - Support for [git-flow-avh](https://github.com/petervanderdoes/gitflow) completion

---

## git-hubflow

**Maintainer:** [wweaver](https://github.com/wweaver)

- git-hubflow - Support for [git HubFlow](http://dev.datasift.com/blog/hubflow-github-and-gitflow-model-together) completion

---

## git_remote_branch

**Maintainer:** [webmat](https://github.com/webmat)

- git_remote_branch - Support for [grb](https://github.com/webmat/git_remote_branch) completion

| Commands                                     |
|:--------------------------------------------:|
| _grb create branch_name_ [origin_server]     |
| _grb publish branch_name_ [origin_server]    |
| _grb delete branch_name_ [origin_server]     |
| _grb track branch_name_ [origin_server]      |
| _grb rename new_branch_name_ [origin_server] |
| _grb explain create_                         |

---

## github

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- github - adds autocomplete to the github gem, which is installable via `gem install github`

---

## gradle

**Maintainer:** [matthewmccullough](http://github.com/matthewmccullough)

Adds autocompletion of task names and option switches to command line use of gradle by actually executing gradle tasks in the background and collecting the result.

Caches the result of the task names in a `.gradletasknamecache` file that is regenerated if the timestamp of the `build.gradle` file changes.

---

## grails

**Maintainer:** [zachriggle](http://github.com/zachriggle)

Adds tab-completion of Grails script names to the command line use of grails. Looks for scripts in the following paths:

- `$GRAILS_HOME/scripts`
- `~/.grails/scripts`
- `./scripts`
- `./plugins/*/scripts`

---

## httpie

**Maintainer:** [lululau](https://github.com/lululau)

Adds completion for [HTTPie](http://httpie.org), which is a command line HTTP client, a user-friendly cURL replacement.

---

## history

**Maintainer:** [r-darwish](https://github.com/r-darwish)

Provides a couple of convenient aliases for using the `history` command to examine your command line history.

| Alias               | Description                                                                                                                  |
|:--------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| _h_                 | List your command history. Equivalent to using `history`                                                                     |
| _hsi_               | When called without an argument you will get help on `grep` arguments                                                        |
| _hsi_ [search text] | Performs a **case insensitive** `grep` search on your command history, looking for commands that match the argument provided |

---

## jira

**Maintainer:** [tresni](https://github.com/tresni)

- Open Jira issues using the command *open_jira_issue*

##### _Examples:_
###### _Open new issue form in browser_
```shell
jira
```
###### _Open issue in browser_
```shell
jira ABC-123
```

If you use Rapid Board make sure to add the following to your .zshrc:
```shell
JIRA_RAPID_BOARD="true"
```

---

## jsontools

**Maintainer:** [bobwilliams](https://github.com/bobwilliams)

handy command line tools for dealing with json data.

| Command          | Description                                           |
|:-----------------|:------------------------------------------------------|
| _pp_json_        | pretty prints json                                    |
| _is_json_        | returns true if valid json; false otherwise           |
| _urlencode_json_ | returns a url encoded string for the given json       |
| _urldecode_json_ | returns decoded json for the given url encoded string |

---

## knife

**Maintainer:** [franklouwers](https://github.com/franklouwers)

- knife - adds autocompletion to [knife](https://docs.chef.io/knife.html)

---

## laravel4

**Maintainer:** [m0nah](https://github.com/m0nah)

[Laravel 4](http://laravel.com) autocomplete plugin!

| Alias       | Description              |
|:------------|:-------------------------|
| _la4_       | php artisan              |
| _la4dump_   |php artisan dump-autoload |
| _la4cache_  | php artisan cache:clear  |
| _la4routes_ | php artisan routes       |

---

## last-working-dir

**Maintainer:** [op](https://github.com/op)

Keeps track of the last used directory and automatically jumps to it for new shells. Similar to how many terminal emulators does it.

| Command | Description                                                          |
|:--------|:---------------------------------------------------------------------|
| _lwd_   | Jump to last working directory (automatically called for new shells) |

---

## lein

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- lein - auto-completion for [leiningen](https://github.com/technomancy/leiningen), build tool for [clojure](http://clojure.org/)

---

## lighthouse

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- lighthouse - open lighthouse tickets using the command *open_lighthouse_ticket* (see [[http://screencast.com/t/ZDgwNDUwNT]])

---

## lol

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- lol - brings lulz to your zsh (based on lolbash)

---

## macports

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- macports - adds "port" command completion and aliases for running macports commands

---

## mercurial

**Maintainers:** [ptrv](https://github.com/ptrv), [oshybystyi](https://github.com/oshybystyi)

| Alias  | Description                                         |
|:-------|:----------------------------------------------------|
| _hgc_  | hg commit                                           |
| _hgb_  | hg branch                                           |
| _hgba_ | hg branches                                         |
| _hgco_ | hg checkout                                         |
| _hgd_  | hg diff                                             |
| _hged_ | hg diffmerge                                        |
| _hgl_  | hg pull -u                                          |
| _hgp_  | hg push                                             |
| _hgs_  | hg status                                           |
| _hgca_ | hg qimport -r tip ; hg qrefresh -e ; hg qfinish tip |

Plus it adds mercurial repo info into zsh prompt.

See detailed instructions in [plugin README](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/mercurial)

---

## meteor

**Maintainer:** [jorge-d](https://github.com/jorge-d)

This plugin adds completion for the meteor command

##### _Examples:_
```shell
$ meteor [tab]
$ cd some_random_meteor_project
$ meteor add [tab] # Will list all the available packages
$ meteor remove [tab] # Will all the installed packages
```

---

## mvn

**Maintainer:** [fred-o](https://github.com/fred-o)

- mvn - adds command line completion for apache maven

---

## mysql-macports

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- mysql - aliases for starting stopping and getting mysql status ( *mysqlstart*, *mysqlstop*, *mysqlstatus*)

---

## nanoc

**Maintainer:** [josh-](https://github.com/josh-)

Enhances the [Nanoc](http://nanoc.stoneship.org/) static site generator with aliases and ZSH autocompletion. Discussed in further detail in [this blog post](http://joshparnham.com/2012/10/nanoc-plus-zsh-equals-awesomeness/).

| Alias          | Description                                                                                          |
|:---------------|:-----------------------------------------------------------------------------------------------------|
| _n_            | is an alias to `nanoc`, other commands may be appended to this or on its own it will compile a site. |
| _na_           | starts the autocompiler.                                                                             |
| _nco_          | compiles a site.                                                                                     |
| _nci_ <item>   | creates an item <item>.                                                                              |
| _ncl_ <layout> | creates a layout <layout>.                                                                           |
| _ncs_ <site>   | creates a site <site>.                                                                               |
| _nd_           | deploys a site.                                                                                      |
| _nv_           | starts the `adsf` server for the current site.                                                       |
| _nw_           | starts the watcher.                                                                                  |

---

## ng

Adds completion for `angular-cli` (also called `ng`).
See [the README](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/ng) for more information.

**Maintainer:** [@catull](https://github.com/catull)

---

## node

| Command               | Description                                                                                                 |
|:----------------------|:------------------------------------------------------------------------------------------------------------|
| _node-docs_ [SECTION] | open the [node api](https://nodejs.org/docs/v6.2.2/api/all.html), for your current version, in your browser. |

---

## npm

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- npm - adds autocompletion to [npm](https://npmjs.org)

---

## nyan

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- nyan - nyan cat goodness in your shell

---

## osx

| Command       | Description                                    |
|:--------------|:-----------------------------------------------|
| `tab`         | Open the current directory in a new tab        |
| `ofd`         | Open the current directory in a Finder window  |
| `pfd`         | Return the path of the frontmost Finder window |
| `pfs`         | Return the current Finder selection            |
| `cdf`         | `cd` to the current Finder directory           |
| `pushdf`      | `pushd` to the current Finder directory        |
| `quick-look`  | Quick-Look a specified file                    |
| `man-preview` | Open a specified man page in Preview app       |
| `showfiles`     | Show hidden files                                |
| `hidefiles`     | Hide the hidden files                            |
| `itunes`        | Control iTunes. User `itunes -h` for usage details |
| `spotify`       | Control Spotify and search by artist, album, track and etc.|

See the [README](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/osx) for more information.

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

---

## pass

**Maintainer:** [sanbor](https://github.com/sanbor)

Completion plugin for [pass](http://zx2c4.com/projects/password-store/). [Source](http://git.zx2c4.com/password-store/tree/contrib/pass.zsh-completion)

---

## per-directory-history

**Maintainer:** [jimhester](https://github.com/jimhester)

per-directory-history - tracks previous command history both per current directory and globally, with the ability to switch between them on the fly, bound to ctrl-g.

---

## perl

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- perl - useful shortcuts for perlbrew, perldoc, and perl one-liners

---

## perms

**Maintainer:** [Rory Hardy](https://github.com/gneatgeek)

Plugin to handle some unix filesystem permissions quickly

---

## pep8

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Completion for the pep8 python coding style (PEP8) check tool

---

## phing

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- phing - auto complete for phing targets.

---

## pip

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- pip - completion plugin for the pip command

---

## pod

**Maintainer:** [mekanics](https://github.com/mekanics)

- Completion plugin for [CocoaPods](http://cocoapods.org/)
- You can find the official documentation [here](http://docs.cocoapods.org/commands.html)

---

## pow

| Command | Description                                                                   |
|:--------|:------------------------------------------------------------------------------|
| _kapow_ | helper function to touch `tmp/restart.txt`, restarting an application in pow. |

---

## powify

A simple [powify](https://github.com/sethvargo/powify) autocomplete plugin. It includes all commands, subcomands, and rack app name autocompletion where needed.

---

## pyenv

**Maintainer:** [ssm](https://github.com/ssm)

- Completion for the [pyenv](https://github.com/yyuu/pyenv) command, which maintains local python installations.
- Exports a "pyenv_prompt_info()" function for your custom prompt.

---

## pylint

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Completion for the python file coding style check tool

---

## python

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Completion for the python interpreter

---

## rails

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

#### rails aliases:
| Alias | Command                  |
|:------|:-------------------------|
| _rc_  | rails console            |
| _rd_  | rails destroy            |
| _rdb_ | rails dbconsole          |
| _rg_  | rails generate           |
| _rgm_ | rails generate migration |
| _rp_  | rails plugin             |
| _ru_  | rails runner             |
| _rs_  | rails server             |
| _rsd_ | rails server --debugger  |

#### rake aliases:
| Alias   | Command                       |
|:--------|:------------------------------|
| _rdm_   | rake db:migrate               |
| _rdms_  | rake db:migrate:status        |
| _rdr_   | rake db:rollback              |
| _rdc_   | rake db:create                |
| _rds_   | rake db:seed                  |
| _rdd_   | rake db:drop                  |
| _rdtc_  | rake db:test:clone            |
| _rdtp_  | rake db:test:prepare          |
| _rdmtc_ | rake db:migrate db:test:clone |
| _rlc_   | rake log:clear                |
| _rn_    | rake notes                    |
| _rr_    | rake routes                   |

---

## rand-quote

**Maintainer:** [posva](https://github.com/posva)

Creates a function `quote` to display a colored random quote picked from this [site](http://www.quotationspage.com/random.php3)

---

## redis-cli

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion plugin for [redis-cli](http://redis.io/topics/quickstart)

---

## repo

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

- Completion plugin for [git-repo](https://code.google.com/p/git-repo/)

| Alias   | Command                   |
|:--------|:--------------------------|
| _rs_    | repo sync                 |
| _rra_   | repo rebase --auto-stash  |
| _rsrra_ | repo sync and repo rebase |

---

## ruby

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

| Alias | Command                              |
|:------|:-------------------------------------|
| rfind | find . -name "*.rb" \| xargs grep -n |
| sgem  | sudo gem                             |

---

## rvm

| Command         | Description                                                                                                                                     |
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| _rb18_ [GEMSET] | shortcut for `rvm use ruby-1.8.7-p334@GEMSET` (with gemset completion)                                                                          |
| _rb19_ [GEMSET] | shortcut for `rvm use ruby-1.9.2-p180@GEMSET` (with gemset completion)                                                                          |
| _rubies_        | list installed rubies                                                                                                                           |
| _gemsets_       | list gemsets for currently active ruby                                                                                                          |
| _gems_          | list gems available in currently active gemset **Note: This has opinions about colors. It should be re-factored to be customizable in themes.** |

After `rvm-update` (alias for `rvm get head; rvm reload`), run `rvm-link-completion` to make a symlink to the official zsh completion file that comes with rvm into your oh-my-zsh rvm plugin directory.

---

## sbt

**Maintainer:** [mcaserta](https://github.com/mcaserta)

- sbt - completion plugin for [SBT](http://www.scala-sbt.org/)

| Alias   | Command             |
|:--------|:--------------------|
| _sbc_   | sbt compile         |
| _sbco_  | sbt console         |
| _sbcq_  | sbt console-quick   |
| _sbcl_  | sbt clean           |
| _sbcp_  | sbt console-project |
| _sbd_   | sbt doc             |
| _sbdc_  | sbt dist:clean      |
| _sbdi_  | sbt dist            |
| _sbgi_  | sbt gen-idea        |
| _sbp_   | sbt publish         |
| _sbpl_  | sbt publish-local   |
| _sbr_   | sbt run             |
| _sbrm_  | sbt run-main        |
| _sbu_   | sbt update          |
| _sbx_   | sbt test            |

---

## scala

**Maintainer:** [mcaserta](https://github.com/mcaserta)

- scala - completion plugin for [scala](http://www.scala-lang.org/) and scalac

---

## screen

**Maintainer:** [fred-o](https://github.com/fred-o)

- screen - automatic setting of window titles and status for [GNU Screen](http://www.gnu.org/software/screen/)

---

## sprunge

**Maintainer:** [ilikenwf](https://github.com/ilikenwf)

- [sprunge](http://sprunge.us) - a basic cli interface to pastebin, which accepts it's input through web requests. Designed for Linux users, sprunge is an easy way to pastebin text without having to actually use a web browser. The oh-my-zsh plugin is based on http://www.shellperson.net/sprunge-pastebin-script/, author unknown.

You can use sprunge in the following ways:

##### _Examples:_
###### _Pipes:_
```shell
echo "hello there...testing sprunge"|sprunge
```
###### _Files:_
```shell
sprunge test.txt
```
###### _Strings:_
```shell
sprunge "hello"
```

Note that if a filename is misspelled or doesn't have the necessary path description, it will NOT generate an error, but will instead treat it as a text string and upload it.

---

## ssh-agent

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- ssh-agent - cygwin ssh-agent plugin for starting agent (see - http://www.cygwin.com/ml/cygwin/2001-06/msg00537.html )

---

## sublime

**Maintainer:** [dylnhdsn](https://github.com/dylnhdsn)

| Command | Description                                |
|:--------|:-------------------------------------------|
| _st_    | open a specified file in Sublime Text      |
| _stt_   | open the current directory in Sublime Text |

---

## sudo

**Maintainer:** [dongweiming](https://github.com/dongweiming)

- `ESC` twice: Puts `sudo` in front of the current command, or the last one if the command line is empty.

---

## supervisor

**Maintainer:** [everbird](http://github.com/everbird)

- supervisor - Adds tab-completion for supervisord/supervisorctl in [Supervisor](http://supervisord.org/). These scripts are from [zshcompfunc4supervisor](https://bitbucket.org/hhatto/zshcompfunc4supervisor).

---

## suse

**Maintainer:** [r-darwish](https://github.com/r-darwish)

| Alias | Command                  |
|:------|:-------------------------|
| _zi_  | sudo zypper install      |
| _zrf_ | sudo zypper refresh      |
| _zs_  | zypper search            |
| _zup_ | sudo zypper dist-upgrade |
| _zrm_ | sudo zypper remove       |
| _zp_  | sudo zypper patch        |
| _zps_ | sudo zypper ps           |

---

## svn

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- svn - adds several functions for dealing with the status of the current directory's svn repo.

---

## svn-fast-info

- svn-fast-info - is a faster drop-in replacement of the **svn** plugin, it brings the same level of functionality using the same API. The speed improvements are especially visible on big SVN repository.

---

## symfony2

**Maintainer:** [andrewtch](https://github.com/andrewtch)

[Symfony2](http://symfony.com) autocomplete plugin; binds to app/console<tab>, and not ./console command!

| Alias     | Command                         |
|:----------|:--------------------------------|
| _sf_      | php app/console                 |
| _sfcl_    | php app/console cache:clear     |
| _sfroute_ | php app/console router:debug    |
| _sfgb_    | php app/console generate:bundle |

---

## systemd

**Maintainer:** [aelesbao](https://github.com/aelesbao)

- [systemd](http://freedesktop.org/wiki/Software/systemd) aliases plugin; Add `sc-[command]` aliases to all `systemctl` commands, using `sudo` when needed.

---

## taskwarrior

**Maintainer:** [lepht](https://github.com/lepht)

- taskwarrior - adds smart tab completion for [TaskWarrior](http://taskwarrior.org). For example, `task[tabtab]` will give you a list of current tasks, `task 66[tabtab]` gives a list of available modifications for that task, etc.

---

## terminalapp

**Maintainer:** [OutPunk](https://github.com/OutPunk)

- terminalapp - automatically sets the Terminal.app resume directory, so when restoring windows with OS X Lion's "Resume" feature it will restore the directory too. **Note**: This plugin is deprecated and the functionality has been folded into core `lib/termsupport.zsh` which is loaded for all users. If you have a current version of Oh My Zsh, remove this from your `$plugins` list.

---

## terminitor

**Maintainer:** [philippbosch](https://github.com/philippbosch)

[terminitor](https://github.com/achiu/terminitor) is a tool that "automates your development workflow setup".

- terminitor – auto complete for terminitor commands and scripts

---

## textmate

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

| Alias            | Command                                                                                         |
|:-----------------|:------------------------------------------------------------------------------------------------|
| _et_             | mate .                                                                                          |
| _ett_            | mate Gemfile app config features lib db public spec test Rakefile Capfile Todo                  |
| _etp_            | mate app config lib db public spec test vendor/plugins vendor/gems Rakefile Capfile Todo        |
| _etts_           | mate app config lib db public script spec test vendor/plugins vendor/gems Rakefile Capfile Todo |
| _mr_             | mate CHANGELOG app config db lib public script spec test                                        |
| _tm_ [directory] | changes to specified directory and executes `mate .`                                            |

---

## tig

Adds aliases for `tig`. See [the README](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/tig) for more information.

---

## thor

Completions for `thor`

---

## tmux

**Maintainer:** [jmatth](http://github.com/jmatth)

Adds several options for effecting the startup behavior of [tmux](https://tmux.github.io). Each of the options are set by changing the environment variables below in the **TOP** of your `tmux.plugin.zsh` file:

1. `ZSH_TMUX_AUTOSTART`: Automatically start a tmux session upon logging in. Set to `false` by default.
2. `ZSH_TMUX_AUTOSTART_ONCE`: Only attempt to autostart tmux once. If this is disabled when the previous option is enabled, then tmux will be autostarted every time you source your zsh config files. Set to `true` by default.
3. `ZSH_TMUX_AUTOCONNECT`: When running `tmux` automatically connect to the currently running tmux session if it exits, otherwise start a new session. Set to `true` by default.
4. `ZSH_TMUX_AUTOQUIT`: Close the terminal session when tmux exits. Set to the value of `ZSH_TMUX_AUTOSTART` by default.
5. `ZSH_TMUX_FIXTERM`: When running tmux, the variable `$TERM` is supposed to be set to `screen` or one of its derivatives. This option will set the `default-terminal` option of tmux to `screen-256color` if 256 color terminal support is detected, and `screen` otherwise. The term values it uses can be overridden by changing the `ZSH_TMUX_FIXTERM_WITH_256COLOR` and `ZSH_TMUX_FIXTERM_WITHOUT_256COLOR` variables respectively. Set to `true` by default.

If the user specifies any arguments for `tmux` then the command is just executed as it was typed it without any 
modification.

### aliases

| Alias | Command    |
|:------|:-----------|
|ta | tmux attach -t|
|tad | tmux attach -d -t|
|ts | tmux new-session -s|
|tl | tmux list-sessions|
|tksv | tmux kill-server|
|tkss | tmux kill-session -t|


---

## tmuxinator

Completions for [tmuxinator](https://github.com/aziz/tmuxinator). To enable completions for `mux`, a shortcut for tmuxinator, add following alias in your zshrc to overwrite the executable:

| Alias | Command    |
|:------|:-----------|
| mux   | tmuxinator |

---

## tugboat

**Maintainer:** [DimitriSteyaert](https://github.com/DimitriSteyaert)

- tugboat - autocompletion for Tugboat commands, the CLI tool to manage your Digital Ocean configuration and droplets.

---

## urltools

Adds command line utilities for URL manipulation.

| Command     | Description                                                                       |
|:------------|:----------------------------------------------------------------------------------|
| _urlencode_ | encodes a string so it compiles with the URL character rules laid out in RFC 1738 |
| _urldecode_ | decode a string encoded according to the URL character rules in RFC 1738          |

---

## vagrant

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- vagrant - autocompletion for Vagrant commands, task names, box names and built-in handy documentation. All in one place.

---

## vi-mode

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

** Read the plugin [README](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/vi-mode) file **

- Increase zsh `vi-like` functionality

---

## virtualenvwrapper

**Maintainer:** [mispy](https://github.com/mispy)

- virtualenvwrapper - Loads Python's [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) shell tools, and automatically activates virtualenv on cd into git repository with matching name.

---

## web-search

**Maintainer:** [xuhdev](https://github.com/xuhdev)

Adds several commands to do web search.

| Commands   |
|:----------:|
| bing       |
| google     |
| yahoo      |
| duckduckgo |

##### _Examples:_
###### _Search for oh-my-zsh on Google:_
```shell
google oh-my-zsh
```
###### _Search for "What is GitHub" on Bing:_
```shell
bing what is github
```
###### _Search for "foo bar" on DuckDuckGo:_
```shell
ddg foo bar
```
---

## yarn

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

[Yarn](https://yarnpkg.com/en/) autocompletion plugin.

---

## yii

**Maintainer:** [IgorTimoshenko](https://github.com/IgorTimoshenko)

[Yii](http://yiiframework.com) autocompletion plugin.

| Alias | Command        |
|:------|:---------------|
| yiic  | protected/yiic |

---

## yii2

**Maintainer:** [ekaragodin](https://github.com/ekaragodin)

[Yii2](http://yiiframework.com) autocompletion plugin.

---

## yum

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Enables aliases for [Yum](http://yum.baseurl.org), the popular front-end to the RPM Package Manager.

| Alias | Command                         | Description                   |
|:------|:-------------------------------:|:------------------------------|
| _ys_  | yum search                      | Search package                |
| _yp_  | yum info                        | Show package info             |
| _yl_  | yum list                        | List packages                 | 
| _ygl_ | yum grouplist                   | List package groups           |
| _yli_ | yum list installed              | Print all installed packages  |
| _ymc_ | yum makecache                   | Rebuilds the yum package list |
| _yu_  | sudo yum update                 | pgrade packages               |
| _yi_  | sudo yum install                | Install package               |
| _ygi_ | sudo yum groupinstall           | Install package group         |
| _yr_  | sudo yum remove                 | Remove package                |
| _ygr_ | sudo yum groupremove            | Remove pagage group           |
| _yrl_ | sudo yum remove --remove-leaves | Remove package and leaves     |
| _yc_  | sudo yum clean all              | Clean cache                   |

---

## zeus

**Homepage:** [Zeus project](https://github.com/burke/zeus)

### Aliases

**Maintainer:** [Bamboo](https://github.com/b4mboo)

| Alias        | Command                                                            |
|:-------------|:-------------------------------------------------------------------|
| _zi_         | zeus init                                                          |
| _zinit_      | zeus init                                                          |
| _zs_         | zeus start                                                         |
| _ztart_      | zeus start                                                         |
| _zc_         | zeus console                                                       |
| _zonsole_    | zeus console                                                       |
| _zsr_        | zeus server                                                        |
| _zerver_     | zeus server                                                        |
| _zr_         | zeus rake                                                          |
| _zake_       | zeus rake                                                          |
| _zg_         | zeus generate                                                      |
| _zenerate_   | zeus generate                                                      |
| _zrn_        | zeus runner                                                        |
| _zunner_     | zeus runner                                                        |
| _zcu_        | zeus cucumber                                                      |
| _zucumber_   | zeus cucumber                                                      |
| _zt_         | zeus test                                                          |
| _zest_       | zeus test                                                          |
| _zu_         | zeus test test/unit/*                                              |
| _zunits_     | zeus test test/unit/*                                              |
| _zf_         | zeus test test/functional/*                                        |
| _zunctional_ | zeus test test/functional/*                                        |
| _za_         | zeus test test/unit/*; zeus test test/functional/; zeus cucumber   |
| _zall_       | zeus test test/unit/*; zeus test test/functional/; zeus cucumber   |
| _zsw_        | rm .zeus.sock                                                      |
| _zweep_      | rm .zeus.sock                                                      |

### Completion

**Maintainer:** [johnjohndoe](https://github.com/johnjohndoe)

Completion plugin for [zeus](https://github.com/burke/zeus). The describing texts are inspired by the texts given in the [documentation of Rails command line tools](http://guides.rubyonrails.org/command_line.html).*[Source](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/zeus/_zeus)

---

## wd

**Maintainer:** [mfaerevaag](https://github.com/mfaerevaag)

`wd` (warp directory) lets you jump to custom directories in zsh, without using cd. Why? Because cd seems inefficient when the folder is frequently visited or has a long path. [Source](https://github.com/mfaerevaag/wd)

Print usage with no opts or the `help` argument.

##### _Examples:_
###### _Add warp point to current working directory:_
```
wd add test
```

If a warp point with the same name exists, use `add!` to overwrite it.

##### _Examples:_
###### _From an other directory, warp to test with:_
```
wd test
```
###### _You can warp back to previous directory, and so on, with the puncticulation syntax:_
```
wd ..
wd ...
```

This is a wrapper for the zsh `dirs` function.

###### _Remove warp point test point:_
```
wd rm test
```
###### _List warp points to current directory (stored in `~/.warprc`):_
```
wd show
```
###### _List all warp points (stored in `~/.warprc`):_
```
wd list
```