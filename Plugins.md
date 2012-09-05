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

## archlinux
**Maintainer:** [Benjamin Boudreau](https://github.com/dreur)

### Enabled [aliases](https://wiki.archlinux.org/index.php/Pacman_Tips) for `pacman` (replace `pac` by `ya` for `yaourt`)
Install specific package(s) from the repositories

    pacin='sudo pacman -S'

Install specific package not from the repositories but from a file 

    pacins='sudo pacman -U'          

Remove the specified package(s), retaining its configuration(s) and required dependencies

    pacre='sudo pacman -R'           

Remove the specified package(s), its configuration(s) and unneeded dependencies

    pacrem='sudo pacman -Rns'        

Display information about a given package in the repositories

    pacrep='pacman -Si'              

Search for package(s) in the repositories

    pacreps='pacman -Ss'             

Display information about a given package in the local database

    pacloc='pacman -Qi'              

Search for package(s) in the local database

    paclocs='pacman -Qs'

Update and refresh the local package and ABS databases against repositories

    pacupd='sudo pacman -Sy && sudo abs'     

Install given package(s) as dependencies of another package

    pacinsd='sudo pacman -S --asdeps'        

Force refresh of all package lists after updating /etc/pacman.d/mirrorlist

    pacmir='sudo pacman -Syy'

### Extra functions for package management in Archlinux

List all installed packages with a short description - [Source](https://bbs.archlinux.org/viewtopic.php?id=93683)

    paclist

List all orphaned packages

    paclsorphans

Delete all orphaned packages

    pacrmorphans
    
List all disowned files in your system

    pacdisowned | less +F

## Autojump

Will enable autojump if installed with homebrew or macports.

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

Also creates shell aliases so you don't have to type "bundle exec" before most common ruby commands when you are in a directory with a Gemfile.  Here is a [list of commands](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/bundler/bundler.plugin.zsh#L9) it does this for: `annotate cap capify cucumber ey foreman guard heroku middleman nanoc rackup rainbows rails rake rspec ruby shotgun spec spork thin thor unicorn unicorn_rails`

## cake
**Maintainer:** [PabloSerbo][PabloSerbo]

Commands for [Cake](http://jashkenas.github.com/coffee-script/#cake), the coffee-script build tool.

* cake -- auto complete for cake tasks

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

## cloudapp
**Maintainer:** [matthewmccullough](http://github.com/matthewmccullough)

Uploads files and piped contents to the [Cloudapp](http://getcloudapp.com/) service. Outputs and copies the resultant URL to the clipboard. Uses the cloudapp ruby gem from @holman.

## compleat
**Maintainer:** [robbyrussell][robbyrussell]

Completion for human beings. **Further documentation needed**

See this [blog post about compleat](http://limpet.net/mbrubeck/2009/10/30/compleat.html)

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

## dircycle
This is a small zle trick that lets you cycle your directory stack left or right using Ctrl+Shift+Left/Right. This is useful when moving back and forth between directories in development environments, and can be thought of as kind of a nondestructive pushd/popd.

## dirpersist
**Maintainer:** [robbyrussell][robbyrussell]

* dirpersist


## encode64
**Maintainer:** [fuksito](http://github.com/fuksito)

This is a plugin that helps to encode/decode strings with base64 from the console quickly:

    $ encode64 some_string
    => c29tZV9zdHJpbmc=

    $ decode64 c29tZV9zdHJpbmc=
    => some_string

## fabric
**Maintainer:** [santiycr][santiycr]

* fab - completion plugin for [fabric](http://docs.fabfile.org/en/1.2.2/index.html)

## gas

* gas - completion plugin for the [gas](https://github.com/walle/gas) gem

## gem
**Maintainer:** [robbyrussell][robbyrussell]

* gem - completion plugin for the gem command

## gpg-agent
**Maintainer:** [robbyrussell][robbyrussell]

* gpg-agent - starts gpg-agent (with ssh support) if not running and includes its environment variables

## git
**Maintainer:** [robbyrussell][robbyrussell]

* git - adds a lot of git aliases ( g*x* e.g. gd - git diff) and functions for pulling for dealing with the current branch

You can find a list of some of the aliases introduced [here](http://jasonm23.github.com/oh-my-git-aliases.html).

## git-flow
**Maintainer:** [robbyrussell][robbyrussell]

* git-flow - Support for [git-flow](https://github.com/nvie/gitflow) completion

## github
**Maintainer:** [robbyrussell][robbyrussell]

* github - adds autocomplete to the github gem installable via gem install github-gem

## gradle
**Maintainer:** [matthewmccullough](http://github.com/matthewmccullough)

Adds autocompletion of task names and option switches to command line use of gradle by actually executing gradle tasks in the background and collecting the result.

Caches the result of the task names in a `.gradletasknamecache` file that is regenerated if the timestamp of the `build.gradle` file changes.

## grails
**Maintainer:** [zachriggle](http://github.com/zachriggle)

Adds tab-completion of Grails script names to the command line use of grails.  Looks for scripts in the following paths:

- `$GRAILS_HOME/scripts` 
- `~/.grails/scripts `
- `./scripts`
- `./plugins/*/scripts`

## knife
**Maintainer:** [franklouwers](https://github.com/franklouwers)

* knife - adds autocompletion to [knife](http://wiki.opscode.com/display/chef/Knife)

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

## mercurial
**Maintainer:** [ptrv](https://github.com/ptrv)

* `hgc - hg commit`
* `hgb - hg branch`
* `hgba - hg branches`
* `hgco - hg checkout`
* `hgd - hg diff`
* `hged - hg diffmerge`
* `hgl - hg pull -u`
* `hgp - hg push`
* `hgs - hg status`
* `hgca - hg qimport -r tip ; hg qrefresh -e ; hg qfinish tip`, this is the 'git commit --amend' equivalent

## mvn
**Maintainer:** [fred-o][fred-o]

* mvn - adds command line completion for apache maven

## mysql-macports
**Maintainer:** [robbyrussell][robbyrussell]

* mysql - aliases for starting stopping and getting mysql status ( *mysqlstart*, *mysqlstop*, *mysqlstatus*)

## node
* `node-api [SECTION]`: open the [node api](http://nodejs.org/docs/v0.4.8/api/all.html), for your current version, in your browser. **Note: This uses `open` which comes with OS X. This needs to be re-factored to work on other platforms.**

## npm
**Maintainer:** [robbyrussell][robbyrussell]

## nyan
**Maintainer:** [robbyrussell][robbyrussell]

* nyan - nyan cat goodness in your shell

## osx
**Maintainer:** [robbyrussell][robbyrussell]

* `tab` - open the current directory in a new tab
* `pfd` - return the path of the frontmost Finder window
* `pfs` - return the current Finder selection
* `cdf` - cd to the current Finder directory
* `pushdf` - pushd to the current Finder directory
* `quick-look` - Quick Look a specified file
* `man-preview` - open a specified man page in Preview
* `trash` - move a specified file to the Trash

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

* `rc - rails console`
* `rd - rails destroy`
* `rdb - rails dbconsole`
* `rdbm - rake db:migrate db:test:clone`
* `rg - rails generate`
* `rp - rails plugin`
* `rs - rails server`
* `rsd - rails server --debugger`
* `devlog - tail -f log/development.log`
* `rdm - rake db:migrate`
* `rdr - rake db:rollback`

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

## screen
**Maintainer:** [fred-o][fred-o]

* screen - automatic setting of window titles and status for [GNU Screen](http://www.gnu.org/software/screen/)

## sprunge
**Maintainer:** [ilikenwf](https://github.com/ilikenwf)

* [sprunge](http://sprunge.us) - a basic cli interface to pastebin, which accepts it's input through web requests. Designed for Linux users, sprunge is an easy way to pastebin text without having to actually use a web browser. The oh-my-zsh plugin is based on http://www.shellperson.net/sprunge-pastebin-script/, author unknown.

You can use sprunge in the following ways:

* **Pipes**: `echo "hello there...testing sprunge"|sprunge`
* **Files**: `sprunge test.txt`
* **Strings**: `sprunge "hello"`

Note that if a filename is misspelled or doesn't have the necessary path description, it will NOT generate an error, but will instead treat it as a text string and upload it.

## ssh-agent
**Maintainer:** [robbyrussell][robbyrussell]

* ssh-agent - cygwin ssh-agent plugin for starting agent (see - http://www.cygwin.com/ml/cygwin/2001-06/msg00537.html )

## sublime
**Maintainer:** [dylnhdsn](https://github.com/dylnhdsn)

* `st` - open a specified file in Sublime Text
* `stt` - open the current directory in Sublime Text

## supervisor
**Maintainer:** [everbird](http://github.com/everbird)

* supervisor - Adds tab-completion for supervisord/supervisorctl in [Supervisor](http://supervisord.org/). These scripts are from [zshcompfunc4supervisor](https://bitbucket.org/hhatto/zshcompfunc4supervisor).

## suse
**Maintainer:** [r-darwish](https://github.com/r-darwish)

* `zi - sudo zypper install`
* `zrf - sudo zypper refresh`
* `zs - zipper search`
* `zup - sudo zypper dist-upgrade`
* `zrm - sudo zypper remove`
* `zp - sudo zypper patch`
* `zps - sudo zypper ps`

## svn
**Maintainer:** [robbyrussell][robbyrussell]

## symfony2
**Maintainer:** [andrewtch](https://github.com/andrewtch)

[Symfony2](http://symfony.com) autocomplete plugin; binds to app/console<tab>, and not ./console command!

## taskwarrior
**Maintainer:** [lepht](https://github.com/lepht)

* taskwarrior - adds smart tab completion for [TaskWarrior](http://taskwarrior.org). For example, `task[tabtab]` will give you a list of current tasks, `task 66[tabtab]` gives a list of available modifications for that task, etc.

## terminalapp
**Maintainer:** [OutPunk](https://github.com/OutPunk)

* terminalapp - automatically sets the Terminal.app resume directory, so when restoring windows with OS X Lion's "Resume" feature it will restore the directory too.

## terminitor
**Maintainer:** [philippbosch](https://github.com/philippbosch)

[terminitor](https://github.com/achiu/terminitor) is a tool that "automates your development workflow setup". 

* terminitor – auto complete for terminitor commands and scripts

## textmate
**Maintainer:** [robbyrussell][robbyrussell]

* `et` aliases `mate .`
* `ett` aliases `mate Gemfile app config features lib db public spec test Rakefile Capfile Todo`
* `etp` aliases `mate app config lib db public spec test vendor/plugins vendor/gems Rakefile Capfile Todo`
* `etts` aliases `mate app config lib db public script spec test vendor/plugins vendor/gems Rakefile Capfile Todo`
* `mr` aliases `mate CHANGELOG app config db lib public script spec test`
* `tm [directory]` changes to specified directory and executes `mate .` 


## thor

Completions for `thor`

## vagrant
**Maintainer:** [robbyrussell][robbyrussell]

* vagrant - autocompletion for Vagrant commands, task names, box names and built-in handy documentation. All in one place.

## vi-mode
**Maintainer:** [robbyrussell][robbyrussell]

* vi-mode

## virtualenvwrapper
**Maintainer:** [mispy](https://github.com/mispy)

* virtualenvwrapper - Loads Python's [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) shell tools, and automatically activates virtualenv on cd into git repository with matching name.

## yum
**Maintainer:** [robbyrussell][robbyrussell]

[robbyrussell]: https://github.com/robbyrussell