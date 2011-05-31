Enable the plugins you want by editing your _~/.zshrc_ file. Example:

    plugins=(rails3 git ruby)

_Completion plugins_ will let zsh know which arguments the package has so it can autocomplete. For instance, if you have the Homebrew plugin installed and type:

    brew in

.. and then hit tab, the _brew_-plugin will enable autocompletion to _brew install_. Completion plugins are not documented further on this page as they only provide better introspection for zsh into the original command. _man_ is your friend.

You should always read the source for the plugin before using it to avoid surprises. Plugins are located in ~/.oh-my-zsh/plugins.

The following plugins are bundled:

## apache2-macports
**Maintainer:** [robbyrussell][robbyrussell]

Enables aliases to control a local Apache2 installed via [Macports](http://www.macports.org/).

Start Apache:

    apache2start

Stop Apache:

    apache2stop

Restart Apache:

    apache2restart

## Autojump

Will enable autojump if installed with homebrew.

This does not add any commands on its own.

## brew
**Maintainer:** [robbyrussell][robbyrussell]

* `brews`: list installed brews

Adds the brew install directories to your path **in front** of `/usr/bin`.

After `brew update`, run `brew-link-completion` to make a symlink to the official zsh completion file that comes with brew into your oh-my-zsh brew plugin directory.

Completion plugin for the [[Homebrew|http://mxcl.github.com/homebrew/]] OS X package manager.

## bundler
**Maintainer:** [robbyrussell][robbyrussell]

Enables aliases to [Bundler](http://gembundler.com/).

Bundle exec, execute a command in the context of the bundle

    be [command]

Bundle install

    bi

Bundle update

    bu

## cap
**Maintainer:** [robbyrussell][robbyrussell]

Commands for [Capistrano](https://github.com/capistrano/capistrano/wiki), a deployment tool built in Ruby.

* cap -- a few commands for Capistrano, a deployment tool built in Ruby

## command-not-found
**Maintainer:** [robbyrussell][robbyrussell]

Only for Ubuntu: If a command is not recognized in the $PATH, this will use Ubuntu's command-not-found package to find it or suggest spelling mistakes:

    ~$ gedit
    The program 'gedit' is currently not installed. You can install it by typing:
    sudo apt-get install gedit
    bash: gedit: command not found

The plugin uses the command-not-found package zsh support.

## compleat
**Maintainer:** [robbyrussell][robbyrussell]

Completion for human beings. **Further documentation needed**

## cpanm
**Maintainer:** [robbyrussell][robbyrussell]

Completion plugin for cpanminus (see [[https://github.com/rshhh/cpanminus/blob/master/etc/_cpanm]])_

## deb
**Maintainer:** [robbyrussell][robbyrussell]

A set of aliases to work with the Debian Advanced Packaging Tool, apt.

Search for packages

    as [search term]

Update packages

    ad

Upgrade packages

    au

Install packages

    ai [packages to install]

Remove package

    ar [package to remove]

Apt policy

    ap

Show package info

    av [package name]

Search packages

    acs [search term]

Clean apt cache

    ac

## debian
**Maintainer:** [robbyrussell][robbyrussell]

## dirpersist
**Maintainer:** [robbyrussell][robbyrussell]

* dirpersist

## gem
**Maintainer:** [robbyrussell][robbyrussell]

* gem - completion plugin for the gem command

## gpg-agent
**Maintainer:** [robbyrussell][robbyrussell]

* gpg-agent - starts gpg-agent (with ssh support) if not running and includes its environment variables

## git
**Maintainer:** [robbyrussell][robbyrussell]

* git - adds a lot of git aliases ( g*x* e.g. gd - git diff) and functions for pulling for dealing with the current branch

## git-flow
**Maintainer:** [robbyrussell][robbyrussell]

* git-flow - Support for [git-flow](https://github.com/nvie/gitflow) completion

## github
**Maintainer:** [robbyrussell][robbyrussell]

* github - adds autocomplete to the github gem installable via gem install github-gem

## lein
**Maintainer:** [robbyrussell][robbyrussell]

* lein - auto-completion for [leiningen](https://github.com/technomancy/leiningen), build tool for [clojure](http://clojure.org/)

## lighthouse
**Maintainer:** [robbyrussell][robbyrussell]

* lighthouse - open lighthouse tickets using the command *open_lighthouse_ticket* ( see [[http://screencast.com/t/ZDgwNDUwNT]]

## lol
**Maintainer:** [robbyrussell][robbyrussell]

* lol - brings lulz to your zsh (based on lolbash)

## macports
**Maintainer:** [robbyrussell][robbyrussell]

* macports - adds "port" command completion and aliases for running macports commands

## mysql-macports
**Maintainer:** [robbyrussell][robbyrussell]

* mysql - aliases for starting stopping and getting mysql status ( *mysqlstart*, *mysqlstop*, *mysqlstatus*)

## node
* `node-api [SECTION]`: open the [node api](http://nodejs.org/docs/v0.4.8/api/all.html), for your current version, in your browser. **Note: This uses `open` which comes with OS X. This needs to be re-factored to work on other platforms.**

## npm
**Maintainer:** [robbyrussell][robbyrussell]

## osx
**Maintainer:** [robbyrussell][robbyrussell]

* `showfiles`/`hidefiles`: show/hide hidden files in Finder
* `rm-dsstore`: recursively remove `.DS_Store` files from the current directory
* osx - open the current directory in a new tab via the *tab* command

## perl
**Maintainer:** [robbyrussell][robbyrussell]

* perl - useful shortcuts for perlbrew, perldoc, and perl one-liners

## phing
**Maintainer:** [robbyrussell][robbyrussell]

* phing - auto complete for phing targets. 

## pip
**Maintainer:** [robbyrussell][robbyrussell]

* pip - completion plugin for the pip command

## pow
* `kapow`: helper function to touch `tmp/restart.txt`, restarting an application in pow.

## rails
**Maintainer:** [robbyrussell][robbyrussell]

* rails - rails 2.3 commands (mostly) for running scripts

## rails3
**Maintainer:** [robbyrussell][robbyrussell]

## redis-cli
**Maintainer:** [robbyrussell][robbyrussell]

## ruby
**Maintainer:** [robbyrussell][robbyrussell]

* ruby - alias for sudo gem ( *sgem* ) and a find ruby files in directory alias ( *rfind* )

## rvm
* `rb18 [GEMSET]`: shortcut for `rvm use ruby-1.8.7-p334@GEMSET` (with gemset completion)
* `rb19 [GEMSET]`: shortcut for `rvm use ruby-1.9.2-p180@GEMSET` (with gemset completion)
* `rubies`: list installed rubies
* `gemsets`: list gemsets for currently active ruby
* `gems`: list gems available in currently active gemset **Note: This has opinions about colors. It should be re-factored to be customizable in themes.**

After `rvm-update` (alias for `rvm get head; rvm reload`), run `rvm-link-completion` to make a symlink to the official zsh completion file that comes with rvm into your oh-my-zsh rvm plugin directory.

## ssh-agent
**Maintainer:** [robbyrussell][robbyrussell]

* ssh-agent - cygwin ssh-agent plugin for starting agent (see - http://www.cygwin.com/ml/cygwin/2001-06/msg00537.html )

## svn
**Maintainer:** [robbyrussell][robbyrussell]

## textmate
**Maintainer:** [robbyrussell][robbyrussell]

* textmate -  aliases for opening rails apps without the cruft, also has *tm* function which cd's to the folder and opens mate

## thor

Completions for `thor`

## vagrant
**Maintainer:** [robbyrussell][robbyrussell]

* vagrant - autocompletion for Vagrant commands, task names, box names and built-in handy documentation. All in one place.

## vi-mode
**Maintainer:** [robbyrussell][robbyrussell]

* vi-mode

## yum
**Maintainer:** [robbyrussell][robbyrussell]

[robbyrussell]: https://github.com/robbyrussell
