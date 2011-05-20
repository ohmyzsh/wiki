
Enable the plugins you want by editing your _~/.zshrc_ file. Example:

    plugins=(rails3 git ruby)

_Completion plugins_ will let zsh know which arguments the package has so it can autocomplete. For instance, if you have the Homebrew plugin installed and type:

    brew in

.. and then hit tab, the _brew_-plugin will enable autocompletion to _brew install_. Completion plugins are not documented further on this page as they only provide better introspection for zsh into the original command. _man_ is your friend.

You should always read the source for the plugin before using it to avoid surprises. Plugins are located in ~/.oh-my-zsh/plugins.

The following plugins are bundled:

## apache2-macports

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Enables aliases to control a local Apache2 installed via [Macports](http://www.macports.org/).

Start Apache:

    apache2start

Stop Apache:

    apache2stop

Restart Apache:

    apache2restart

## brew

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion plugin for the [[Homebrew|http://mxcl.github.com/homebrew/]] OS X package manager.

## bundler

Enables aliases to [Bundler](http://gembundler.com/).

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Bundle exec, execute a command in the context of the bundle

    be [command]

Bundle install

    bi

Bundle update

    bu

## cap

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Commands for [Capistrano](https://github.com/capistrano/capistrano/wiki), a deployment tool built in Ruby.

* cap -- a few commands for Capistrano, a deployment tool built in Ruby

## command-not-found

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Only for Ubuntu: If a command is not recognized in the $PATH, this will use Ubuntu's command-not-found package to find it or suggest spelling mistakes:

    ~$ gedit
    The program 'gedit' is currently not installed. You can install it by typing:
    sudo apt-get install gedit
    bash: gedit: command not found

The plugin uses the command-not-found package zsh support.

## compleat

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion for human beings. **Further documentation needed**

## cpanm

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion plugin for cpanminus (see [[https://github.com/rshhh/cpanminus/blob/master/etc/_cpanm]])_

## deb

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

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

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)


## dirpersist

* dirpersist

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## gem

* gem - completion plugin for the gem command

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## git

* git - adds a lot of git aliases ( g*x* e.g. gd - git diff) and functions for pulling for dealing with the current branch

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## git-flow
* git-flow - Support for [git-flow](https://github.com/nvie/gitflow) completion

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## github

* github - adds autocomplete to the github gem installable via gem install github-gem

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## lein

* lein - auto-completion for [leiningen](https://github.com/technomancy/leiningen), build tool for [clojure](http://clojure.org/)

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## lighthouse

* lighthouse - open lighthouse tickets using the command *open_lighthouse_ticket* ( see [[http://screencast.com/t/ZDgwNDUwNT]]

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## lol
* lol - brings lulz to your zsh (based on lolbash)

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## macports

* macports - adds "port" command completion and aliases for running macports commands

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## mysql-macports

* mysql - aliases for starting stopping and getting mysql status ( *mysqlstart*, *mysqlstop*, *mysqlstatus*)

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## npm

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## osx

* osx - open the current directory in a new tab via the *tab* command

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## perl

* perl - useful shortcuts for perlbrew, perldoc, and perl one-liners

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## phing

* phing - auto complete for phing targets. 

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## pip

* pip - completion plugin for the pip command

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## rails
* rails - rails 2.3 commands (mostly) for running scripts

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## rails3

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## redis-cli

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## ruby
* ruby - alias for sudo gem ( *sgem* ) and a find ruby files in directory alias ( *rfind* )

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## ssh-agent
* ssh-agent - cygwin ssh-agent plugin for starting agent (see - http://www.cygwin.com/ml/cygwin/2001-06/msg00537.html )

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## svn

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## textmate
* textmate -  aliases for opening rails apps without the cruft, also has *tm* function which cd's to the folder and opens mate

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## vagrant

* vagrant - autocompletion for Vagrant commands, task names, box names and built-in handy documentation. All in one place.

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## vi-mode
* vi-mode

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

## yum

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)
