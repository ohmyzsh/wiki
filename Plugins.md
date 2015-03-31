Enable the plugins you want by editing your *~/.zshrc* file. Example:

```
plugins=(rails git ruby)
```

*Completion plugins* will let zsh know which arguments the package has so it can autocomplete. For instance, if you have the Homebrew plugin installed and type:

```
brew in
```

.. and then hit tab, the *brew* plugin will enable autocompletion to *brew install*. Completion plugins are not documented further on this page as they only provide better introspection for zsh into the original command. *man* is your friend.

You should always read the source for the plugin before using it to avoid surprises. Plugins are located in ~/.oh-my-zsh/plugins.

The following plugins are bundled:

apache2-macports
----------------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Enables aliases to control a local Apache2 installed via [Macports](http://www.macports.org/).

Start Apache:

```
apache2start
```

Stop Apache:

```
apache2stop
```

Restart Apache:

```
apache2restart
```

archlinux
---------

**Maintainer:** [Benjamin Boudreau](https://github.com/dreur)

### Enabled [aliases](https://wiki.archlinux.org/index.php/Pacman_Tips) for `pacman` (replace `pac` by `ya` for `yaourt`)

Install specific package(s) from the repositories

```
pacin='sudo pacman -S'
```

Install specific package not from the repositories but from a file

```
pacins='sudo pacman -U'
```

Remove the specified package(s), retaining its configuration(s) and required dependencies

```
pacre='sudo pacman -R'
```

Remove the specified package(s), its configuration(s) and unneeded dependencies

```
pacrem='sudo pacman -Rns'
```

Display information about a given package in the repositories

```
pacrep='pacman -Si'
```

Search for package(s) in the repositories

```
pacreps='pacman -Ss'
```

Display information about a given package in the local database

```
pacloc='pacman -Qi'
```

Search for package(s) in the local database

```
paclocs='pacman -Qs'
```

Update and refresh the local package and ABS databases against repositories

```
pacupd='sudo pacman -Sy && sudo abs'
```

Install given package(s) as dependencies of another package

```
pacinsd='sudo pacman -S --asdeps'
```

Force refresh of all package lists after updating /etc/pacman.d/mirrorlist

```
pacmir='sudo pacman -Syy'
```

### Extra functions for package management in Archlinux

List all installed packages with a short description - [Source](https://bbs.archlinux.org/viewtopic.php?id=93683)

```
paclist
```

List all orphaned packages

```
paclsorphans
```

Delete all orphaned packages

```
pacrmorphans
```

List all disowned files in your system

```
pacdisowned | less +F
```

autojump
--------

Enables [autojump](https://github.com/joelthelion/autojump/wiki/) if installed with homebrew, macports or debian/ubuntu package.

This does not add any commands on its own.

autopep8
--------

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Completion for the python file formatting (PEP8) tool

aws
---

**Maintainer:** [Cristian Măgherușan-Stanciu](https://github.com/cristim)

Activates the ZSH completion plugin shipped together with the [aws command-line tool](http://aws.amazon.com/cli/)

### Enabled aliases

Choose the current AWS credentials profile from those defined in .aws/config, with auto-completion support. Also makes the currently set plugin to be shown in the RPROMPT.

```
asp
```

Print the currently set AWS credentials profile.

```
agp
```

bower
-----

**Maintainer:** [miklos-martin](https://github.com/miklos-martin)

Bower is a package manager for the web. This plugin provides some aliases and completions for this great tool.

### Aliases

- `bi`: installs a package (`bower install`)
- `bl`: lists installed packages (`bower list`)
- `bs`: searches for packages (`bower search`)

### Completion

It completes the basic commands for bower. It uses the `bower help` command to achieve this, not a burned-in list of commands. It also provides completion for bower install, uses the output of bower search. It takes a few seconds for the first time (in the session), but then the output of `bower search` is cached, so things then speed up a lot.

### Example

```
# to install jquery for example
bi jq<TAB>
```

brew
----

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

[[Homebrew|http://mxcl.github.com/homebrew/]] is an OS X package manager

This plugin :* creates a `brews` alias to list installed brews (= `brew list -1`)* adds completion for the `brew` command

bundler
-------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Enables aliases to [Bundler](http://gembundler.com/).

Bundle exec, execute a command in the context of the bundle

```
be [command]
```

Bundle install

```
bi
```

Bundle update

```
bu
```

Also creates shell aliases so you don't have to type "bundle exec" before most common ruby commands when you are in a directory with a Gemfile. Here is a [list of commands](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/bundler/bundler.plugin.zsh#L9) it does this for: `annotate cap capify cucumber ey foreman guard heroku middleman nanoc rackup rainbows rails rake rspec ruby shotgun spec spork thin thor unicorn unicorn_rails`

cabal
-----

**Maintainer:** [telser](https://github.com/telser)

- cabal -- auto-completion for [Cabal](http://haskell.org/cabal) a build tool for [Haskell](http://haskell.org).

cake
----

**Maintainer:** [serby](https://github.com/serby)

Commands for [Cake](http://jashkenas.github.com/coffee-script/#cake), the coffee-script build tool.

- cake -- auto complete for cake tasks

cap
---

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Commands for [Capistrano](https://github.com/capistrano/capistrano/wiki), a deployment tool built in Ruby.

- cap -- a few commands for Capistrano, a deployment tool built in Ruby

catimg
------

**Maintainer:** [posva](https://github.com/posva/)

**Original repo:** [catimg.git](https://github.com/posva/catimg)

Print pictures to the `stdout` using `convert` [ImageMagick](http://www.imagemagick.org/)

Example usage `catimg image.png` options:

- `-h` -- print help
- `-w` -- select output width
- `-c` -- change printed character (default `"  "` without the quotes)

celery
------

**Maintainer:** [dongweiming](https://github.com/dongweiming)

Commands for [celery](https://github.com/celery/celery), a distributed task queue.

### Completion

```
# View worker have those parameter options
celery worker<TAB>
```

chruby
------

**Maintainer** [webframp](https://github.com/webframp)

Loads [chruby](https://github.com/postmodern/chruby), a simple ruby version manager, if installed, and provides `chruby_prompt_info` variable for theme use.

Commands:

- `rubies: list installed rubies or change current ruby`

You can manually specify the path to load chruby from using zstyle:

- `zstyle :omz:plugins:chruby path`
- `zstyle :omz:plugins:chruby auto`

Simple build definition completion is also provided for [ruby-build](https://github.com/sstephenson/ruby-build) to make installed rubies from source faster.

chucknorris
-----------

**Maintainer** [maff](https://github.com/maff)

Adds Chuck Norris fortune file from http://www.k-lug.org/~kessler/projects.html. Depends on fortune (and cowsay if using `chuck_cow`) being installed (available via homebrew, apt, ...). Perfectly suitable as MOTD.

Commands:

- `chuck: print random Chuck Norris quote`
- `chuck_cow: print quote in cowthink`

Having `chuck_cow` at the end of your .zshrc results in:

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

command-not-found
-----------------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Only for Ubuntu and openSUSE: If a command is not recognized in the $PATH, this will use Ubuntu's command-not-found package to find it or suggest spelling mistakes:

```
~$ gedit
The program 'gedit' is currently not installed. You can install it by typing:
sudo apt-get install gedit
bash: gedit: command not found
```

The plugin uses the command-not-found package zsh support.

Composer
--------

**Maintainer:** [danielcsgomes](https://github.com/danielcsgomes)

[Composer](http://getcomposer.org/) autocomplete plugin with useful aliases:

- `c   = 'composer'`
- `csu = 'composer self-update'`
- `cu  = 'composer update'`
- `ci  = 'composer install'`
- `ccp = 'composer create-project'`
- `cget = installs composer on the current path`

cloudapp
--------

**Maintainer:** [matthewmccullough](http://github.com/matthewmccullough)

Uploads files and piped contents to the [Cloudapp](http://getcloudapp.com/) service. Outputs and copies the resultant URL to the clipboard. Uses the cloudapp ruby gem from @holman.

coffee
------

**Maintainer:** [jdavis](https://github.com/jdavis)

Completion plugin for [CoffeeScript](http://coffeescript.org/).

For available options, look at the [usage](http://coffeescript.org/#usage) or run the command `coffee --help`.

common-aliases
--------------

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Collection of useful zsh aliases, not enabled by default since they may change some user defined aliases.

- ls aliases: l, la (all), lr (recustively sorted by date), lt (current dir sorted by date), ll (long list), lS (reverse sort by size)
- zshrc: edit directly ~/.zshrc with vim
- cd .., cd ../.., cd ../../../... directly mapped to '..', or '...', or '....'
- alias to place at the end of command line: G (grep), H (head), T (tail), M (most)
- h (history)
- j (jobs)
- p (processes for current user)
- interactive mode for rm, cp, mv

Completion for the python interpreter

compleat
--------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion for human beings. **Further documentation needed**

See this [blog post about compleat](http://limpet.net/mbrubeck/2009/10/30/compleat.html)

cpanm
-----

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion plugin for [cpanminus](https://github.com/miyagawa/cpanminus/)

debian
------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

A set of aliases to work with the Debian Advanced Packaging Tool, apt.

Search for packages

```
as [search term]
```

Update packages

```
ad
```

Upgrade packages

```
ag
```

Install packages

```
ai [packages to install]
```

Remove package

```
ar [package to remove]
```

Apt policy

```
app
```

Search packages

```
acs [search term]
```

Clean apt cache

```
ac
```

dircycle
--------

This is a small zle trick that lets you cycle your directory stack left or right using Ctrl+Shift+Left/Right. This is useful when moving back and forth between directories in development environments, and can be thought of as kind of a nondestructive pushd/popd.

dirhistory
----------

**Maintainer:** [jeffwilliams][jeffwilliams]

This plugin allows you to navigate the history of previous current-working-directories using ALT-LEFT and ALT-RIGHT. ALT-LEFT moves back to directories that the user has changed to in the past, and ALT-RIGHT undoes ALT-LEFT.

For example, if the shell was started, and the following commands were entered:

```
cd ~
cd /usr
cd share
cd doc
```

Then entering ALT-LEFT at the prompt would change directory from /usr/share/doc to /usr/share, then if pressed again to /usr/, then ~. If ALT-RIGHT were pressed the directory would be changed to /usr/ again.

Currently the max history size is 100. The navigation should work for xterm, PuTTY xterm mode, and GNU screen.

dirpersist
----------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- dirpersist

docker
------

**Maintainer:** [Azaan](http://github.com/AeonAxan)

- Auto complete arguments and options for all docker commands.
- Show containerIDs and Images for tab completion where applicable ([screenshots](https://github.com/AeonAxan/oh-my-zsh/blob/master/plugins/docker/README.md))

encode64
--------

**Maintainer:** [fuksito](http://github.com/fuksito)

This is a plugin that helps to encode/decode strings with base64 from the console quickly:

```
$ encode64 some_string
=> c29tZV9zdHJpbmc=

$ decode64 c29tZV9zdHJpbmc=
=> some_string
```

fabric
------

**Maintainer:** [santiycr](https://github.com/santiycr)

- fabric - completion plugin for [fabric](http://docs.fabfile.org/)

fbterm
------

- fbterm - automatically start fbterm when running in /dev/tty*

Forklift
--------

**Maintainer:** [bitboxer](https://github.com/bitboxer)

```
fl [<folder>] - Opens specified directory or current working directory in ForkLift.app
```

fasd
----

**Maintainer:** [a-b](https://github.com/a-b)

- [fasd](https://github.com/clvv/fasd) - command-line productivity booster, offers quick access to files and directories, inspired by autojump, z and v

gas
---

- gas - completion plugin for the [gas](https://github.com/walle/gas) gem

gem
---

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- gem - completion plugin for the gem command

gpg-agent
---------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- gpg-agent - starts gpg-agent (with ssh support) if not running and includes its environment variables

git
---

**Maintainers:** [@Stibbons](https://github.com/Stibbons), [@ncanceill](https://github.com/ncanceill)

Adds a lot of git aliases ( g*x* e.g. gd - git diff) and functions for pulling for dealing with the current branch. See the [dedicated Wiki page](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git), or a list of some of the aliases introduced [here *(OUTDATED)*](http://jasonm23.github.com/oh-my-git-aliases.html).

gitfast
-------

**Maintainer:** [felipec](https://github.com/felipec)

Enables the zsh completion from git.git folks, which is much faster than the official one from zsh. A lot of zsh-specific features are not supported, like descriptions for every argument, but everything the bash completion has, this one does too (as it is using it behind the scenes). Not only is it faster, it should be more robust, and updated regularly to the latest git upstream version.

git-extras
----------

**Maintainer:** [agrimaldi](https://github.com/agrimaldi)

git-extras - Support for [git-extras](https://github.com/visionmedia/git-extras) completion

Pressing tab after the various commands should autofill authors, branches and tags depending on context.

- `git changelog [-l/--list]` - populate changelog file with commits since the previous tag
- `git contrib` - display author contributions
- `git count [--all]` - count commits
- `git delete-branch` - delete local and remote branch
- `git delete-submodule` - delete submodule
- `git delete-tag` - delete local and remote tag
- `git extras [-v/--version]` - git-extras
- `git graft` - merge commits from source branch to destination branch
- `git squash` - merge commits from source branch into the current one as a single commit
- `git feature [finish]` - create a feature branch
- `git refactor [finish]` - create a refactor branch
- `git bug [finish]` - create a bug branch
- `git summary` - repository summary
- `git effort [--above]` - display effort statistics
- `git repl` - read-eval-print-loop
- `git commits-since` - list commits since a given date
- `git release` - release commit with the given tag
- `git alias` - define, search and show aliases
- `git ignore` - add patterns to .gitignore
- `git info` - show info about the repository
- `git create-branch` - create local and remote branch
- `git fresh-branch` - create empty local branch
- `git undo` - remove the latest commit
- `git setup` - setup a git repository
- `git touch` - one step creation of new files
- `git obliterate` - Completely remove a file from the repository, including past commits and tags
- `git local-commits` - list unpushed commits on the local branch

git-flow
--------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- git-flow - Support for [git-flow](https://github.com/nvie/gitflow) completion

git-flow-avh
------------

**Maintainer:**

- git-flow-avh - Support for [git-flow-avh](https://github.com/petervanderdoes/gitflow) completion

git-hubflow
-----------

**Maintainer:** [wweaver](https://github.com/wweaver)

- git-hubflow - Support for [git HubFlow](http://dev.datasift.com/blog/hubflow-github-and-gitflow-model-together) completion

git_remote_branch
-----------------

**Maintainer:** [webmat](https://github.com/webmat)

- git_remote_branch - Support for [grb](https://github.com/webmat/git_remote_branch) completion
- grb create branch_name [origin_server]
- grb publish branch_name [origin_server]
- grb delete branch_name [origin_server]
- grb track branch_name [origin_server]
- grb rename new_branch_name [origin_server]
- grb explain create

github
------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- github - adds autocomplete to the github gem, which is installable via `gem install github`

gradle
------

**Maintainer:** [matthewmccullough](http://github.com/matthewmccullough)

Adds autocompletion of task names and option switches to command line use of gradle by actually executing gradle tasks in the background and collecting the result.

Caches the result of the task names in a `.gradletasknamecache` file that is regenerated if the timestamp of the `build.gradle` file changes.

grails
------

**Maintainer:** [zachriggle](http://github.com/zachriggle)

Adds tab-completion of Grails script names to the command line use of grails. Looks for scripts in the following paths:

- `$GRAILS_HOME/scripts`
- `~/.grails/scripts`
- `./scripts`
- `./plugins/*/scripts`

jira
----

**Maintainer:** [tresni](https://github.com/tresni)

- Open Jira issues using the command *open_jira_issue*`shell
jira # Open new issue form in browser
jira ABC-123 # Open issue in browser
`

If you use Rapid Board make sure to add the following to your .zshrc:`shell
JIRA_RAPID_BOARD="true"
`

jsontools
---------

**Maintainer:** [bobwilliams](https://github.com/bobwilliams)

handy command line tools for dealing with json data.

- pp_json - pretty prints json
- is_json - returns true if valid json; false otherwise
- urlencode_json - returns a url encoded string for the given json
- urldecode_json - returns decoded json for the given url encoded string

knife
-----

**Maintainer:** [franklouwers](https://github.com/franklouwers)

- knife - adds autocompletion to [knife](http://wiki.opscode.com/display/chef/Knife)

laravel4
--------

**Maintainer:** [m0nah](https://github.com/m0nah)

[Laravel 4](http://laravel.com) autocomplete plugin!

**Aliases:**

- `la4 = 'php artisan'`
- `la4dump = 'php artisan dump-autoload'`
- `la4cache = 'php artisan cache:clear'`
- `la4routes = 'php artisan routes'`

last-working-dir
----------------

**Maintainer:** [op](https://github.com/op)

Keeps track of the last used directory and automatically jumps to it for new shells. Similar to how many terminal emulators does it.

- lwd - jump to last working directory (automatically called for new shells)

lein
----

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- lein - auto-completion for [leiningen](https://github.com/technomancy/leiningen), build tool for [clojure](http://clojure.org/)

lighthouse
----------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- lighthouse - open lighthouse tickets using the command *open_lighthouse_ticket* (see [[http://screencast.com/t/ZDgwNDUwNT]])

lol
---

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- lol - brings lulz to your zsh (based on lolbash)

macports
--------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- macports - adds "port" command completion and aliases for running macports commands

mercurial
---------

**Maintainer:** [ptrv](https://github.com/ptrv)

- `hgc - hg commit`
- `hgb - hg branch`
- `hgba - hg branches`
- `hgco - hg checkout`
- `hgd - hg diff`
- `hged - hg diffmerge`
- `hgl - hg pull -u`
- `hgp - hg push`
- `hgs - hg status`
- `hgca - hg qimport -r tip ; hg qrefresh -e ; hg qfinish tip`, this is the 'git commit --amend' equivalent

meteor
------

**Maintainer:** [jorge-d](https://github.com/jorge-d)

This plugin adds completion for the meteor command

Examples:`shell
$ meteor [tab]
$ cd some_random_meteor_project
$ meteor add [tab] # Will list all the available packages
$ meteor remove [tab] # Will all the installed packages
`

mvn
---

**Maintainer:** [fred-o](https://github.com/fred-o)

- mvn - adds command line completion for apache maven

mysql-macports
--------------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- mysql - aliases for starting stopping and getting mysql status ( *mysqlstart*, *mysqlstop*, *mysqlstatus*)

nanoc
-----

**Maintainer:** [josh-](https://github.com/josh-)

Enhances the [Nanoc](http://nanoc.stoneship.org/) static site generator with aliases and ZSH autocompletion. Discussed in further detail in [this blog post](http://joshparnham.com/2012/10/nanoc-plus-zsh-equals-awesomeness/).

### Aliases

- `n` is an alias to `nanoc`, other commands may be appended to this or on its own it will compile a site.
- `na` starts the autocompiler.
- `nco` compiles a site.
- `nci <item>` creates an item <item>.
- `ncl <layout>` creates a layout <layout>.
- `ncs <site>` creates a site <site>.
- `nd` deploys a site.
- `nv` starts the `adsf` server for the current site.
- `nw` starts the watcher.

node
----

- `node-docs [SECTION]`: open the [node api](http://nodejs.org/docs/v0.4.8/api/all.html), for your current version, in your browser.

npm
---

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- npm - adds autocompletion to [npm](https://npmjs.org)

nyan
----

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- nyan - nyan cat goodness in your shell

osx
---

**Maintainers:** [robbyrussell](https://github.com/robbyrussell) [sorin-ionescu](https://github.com/sorin-ionescu)

- `tab` - open the current directory in a new tab
- `pfd` - return the path of the frontmost Finder window
- `pfs` - return the current Finder selection
- `cdf` - cd to the current Finder directory
- `pushdf` - pushd to the current Finder directory
- `quick-look` - Quick Look a specified file
- `man-preview` - open a specified man page in Preview
- `trash` - move a specified file to the Trash

pass
----

**Maintainer:** [sanbor](https://github.com/sanbor)

Completion plugin for [pass](http://zx2c4.com/projects/password-store/). [Source](http://git.zx2c4.com/password-store/tree/contrib/pass.zsh-completion)

per-directory-history
---------------------

**Maintainer:** [jimhester](https://github.com/jimhester)

per-directory-history - tracks previous command history both per current directory and globally, with the ability to switch between them on the fly, bound to ctrl-g.

perl
----

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- perl - useful shortcuts for perlbrew, perldoc, and perl one-liners

pep8
----

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Completion for the pep8 python coding style (PEP8) check tool

phing
-----

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- phing - auto complete for phing targets.

pip
---

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- pip - completion plugin for the pip command

pod
---

**Maintainer:** [mekanics](https://github.com/mekanics)

- Completion plugin for [CocoaPods](http://cocoapods.org/)
- You can find the official documentation [here](http://docs.cocoapods.org/commands.html)

pow
---

- `kapow`: helper function to touch `tmp/restart.txt`, restarting an application in pow.

powify
------

A simple [powify](https://github.com/sethvargo/powify) autocomplete plugin. It includes all commands, subcomands, and rack app name autocompletion where needed.

pyenv
-----

**Maintainer:** [ssm](https://github.com/ssm)

- Completion for the [pyenv](https://github.com/yyuu/pyenv) command, which maintains local python installations.
- Exports a "pyenv_prompt_info()" function for your custom prompt.

pylint
------

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Completion for the python file coding style check tool

python
------

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

Completion for the python interpreter

rails
-----

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- rails - rails 2.3 commands (mostly) for running scripts

rails3
------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- `rc - rails console`
- `rd - rails destroy`
- `rdb - rails dbconsole`
- `rdbm - rake db:migrate db:test:clone`
- `rg - rails generate`
- `rgm - rails generate migration`
- `rdm - rake db:migrate`
- `rdr - rake db:rollback`
- `rp - rails plugin`
- `rs - rails server`
- `rsd - rails server --debugger`

rand-quote
----------

**Maintainer:** [posva](https://github.com/posva)

Creates a function `quote` to display a colored random quote picked from this [site](http://www.quotationspage.com/random.php3)

redis-cli
---------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Completion plugin for [redis-cli](http://redis.io/topics/quickstart)

repo
----

**Maintainer:** [Gaetan Semet](https://github.com/Stibbons)

- rs: repo sync
- rra: repo rebase --auto-stash
- rsrra: repo sync and repo rebase

Completion plugin for [git-repo](https://code.google.com/p/git-repo/)

ruby
----

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- ruby - alias for sudo gem ( *sgem* ) and a find ruby files in directory alias ( *rfind* )

rvm
---

- `rb18 [GEMSET]`: shortcut for `rvm use ruby-1.8.7-p334@GEMSET` (with gemset completion)
- `rb19 [GEMSET]`: shortcut for `rvm use ruby-1.9.2-p180@GEMSET` (with gemset completion)
- `rubies`: list installed rubies
- `gemsets`: list gemsets for currently active ruby
- `gems`: list gems available in currently active gemset **Note: This has opinions about colors. It should be re-factored to be customizable in themes.**

After `rvm-update` (alias for `rvm get head; rvm reload`), run `rvm-link-completion` to make a symlink to the official zsh completion file that comes with rvm into your oh-my-zsh rvm plugin directory.

sbt
---

**Maintainer:** [mcaserta](https://github.com/mcaserta)

- sbt - completion plugin for [SBT](http://www.scala-sbt.org/)

Useful aliases:

- `sbc - sbt compile`
- `sbco - sbt console`
- `sbcq - sbt console-quick`
- `sbcl - sbt clean`
- `sbcp - sbt console-project`
- `sbd - sbt doc`
- `sbdc - sbt dist:clean`
- `sbdi - sbt dist`
- `sbgi - sbt gen-idea`
- `sbp - sbt publish`
- `sbpl - sbt publish-local`
- `sbr - sbt run`
- `sbrm - sbt run-main`
- `sbu - sbt update`
- `sbx - sbt test`

scala
-----

**Maintainer:** [mcaserta](https://github.com/mcaserta)

- scala - completion plugin for [scala](http://www.scala-lang.org/) and scalac

screen
------

**Maintainer:** [fred-o](https://github.com/fred-o)

- screen - automatic setting of window titles and status for [GNU Screen](http://www.gnu.org/software/screen/)

sprunge
-------

**Maintainer:** [ilikenwf](https://github.com/ilikenwf)

- [sprunge](http://sprunge.us) - a basic cli interface to pastebin, which accepts it's input through web requests. Designed for Linux users, sprunge is an easy way to pastebin text without having to actually use a web browser. The oh-my-zsh plugin is based on http://www.shellperson.net/sprunge-pastebin-script/, author unknown.

You can use sprunge in the following ways:

- **Pipes**: `echo "hello there...testing sprunge"|sprunge`
- **Files**: `sprunge test.txt`
- **Strings**: `sprunge "hello"`

Note that if a filename is misspelled or doesn't have the necessary path description, it will NOT generate an error, but will instead treat it as a text string and upload it.

ssh-agent
---------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- ssh-agent - cygwin ssh-agent plugin for starting agent (see - http://www.cygwin.com/ml/cygwin/2001-06/msg00537.html )

sublime
-------

**Maintainer:** [dylnhdsn](https://github.com/dylnhdsn)

- `st` - open a specified file in Sublime Text
- `stt` - open the current directory in Sublime Text

sudo
----

**Maintainer:** [dongweiming](https://github.com/dongweiming)

- `ESC` twice: Puts `sudo` in front of the current command, or the last one if the command line is empty.

supervisor
----------

**Maintainer:** [everbird](http://github.com/everbird)

- supervisor - Adds tab-completion for supervisord/supervisorctl in [Supervisor](http://supervisord.org/). These scripts are from [zshcompfunc4supervisor](https://bitbucket.org/hhatto/zshcompfunc4supervisor).

suse
----

**Maintainer:** [r-darwish](https://github.com/r-darwish)

- `zi - sudo zypper install`
- `zrf - sudo zypper refresh`
- `zs - zipper search`
- `zup - sudo zypper dist-upgrade`
- `zrm - sudo zypper remove`
- `zp - sudo zypper patch`
- `zps - sudo zypper ps`

svn
---

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- svn - adds several functions for dealing with the status of the current directory's svn repo.

svn-fast-info
-------------

- svn-fast-info - is a faster drop-in replacement of the **svn** plugin, it brings the same level of functionality using the same API. The speed improvements are especially visible on big SVN repository.

symfony2
--------

**Maintainer:** [andrewtch](https://github.com/andrewtch)

[Symfony2](http://symfony.com) autocomplete plugin; binds to app/console<tab>, and not ./console command!

**New aliases:**

- `sf = 'php app/console'`
- `sfcl = 'php app/console cache:clear'`
- `sfroute = 'php app/console router:debug'`
- `sfgb = 'php app/console generate:bundle'`

systemd
-------

**Maintainer:** [aelesbao](https://github.com/aelesbao)

[systemd](http://freedesktop.org/wiki/Software/systemd) aliases plugin; Add `sc-[command]` aliases to all `systemctl` commands, using `sudo` when needed.

taskwarrior
-----------

**Maintainer:** [lepht](https://github.com/lepht)

- taskwarrior - adds smart tab completion for [TaskWarrior](http://taskwarrior.org). For example, `task[tabtab]` will give you a list of current tasks, `task 66[tabtab]` gives a list of available modifications for that task, etc.

terminalapp
-----------

**Maintainer:** [OutPunk](https://github.com/OutPunk)

- terminalapp - automatically sets the Terminal.app resume directory, so when restoring windows with OS X Lion's "Resume" feature it will restore the directory too.

terminitor
----------

**Maintainer:** [philippbosch](https://github.com/philippbosch)

[terminitor](https://github.com/achiu/terminitor) is a tool that "automates your development workflow setup".

- terminitor – auto complete for terminitor commands and scripts

textmate
--------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- `et` aliases `mate .`
- `ett` aliases `mate Gemfile app config features lib db public spec test Rakefile Capfile Todo`
- `etp` aliases `mate app config lib db public spec test vendor/plugins vendor/gems Rakefile Capfile Todo`
- `etts` aliases `mate app config lib db public script spec test vendor/plugins vendor/gems Rakefile Capfile Todo`
- `mr` aliases `mate CHANGELOG app config db lib public script spec test`
- `tm [directory]` changes to specified directory and executes `mate .`

thor
----

Completions for `thor`

tmux
----

**Maintainer:** [jmatth](http://github.com/jmatth)

Adds several options for effecting the startup behavior of [tmux](http://tmux.sourceforge.net/). Each of the options are set by changing the environment variables below:

1. `ZSH_TMUX_AUTOSTART`: Automatically start a tmux session upon logging in. Set to `false` by default.
2. `ZSH_TMUX_AUTOSTART_ONCE`: Only attempt to autostart tmux once. If this is disabled when the previous option is enabled, then tmux will be autostarted every time you source your zsh config files. Set to `true` by default.
3. `ZSH_TMUX_AUTOCONNECT`: When running `tmux` automatically connect to the currently running tmux session if it exits, otherwise start a new session. Set to `true` by default.
4. `ZSH_TMUX_AUTOQUIT`: Close the terminal session when tmux exits. Set to the value of `ZSH_TMUX_AUTOSTART` by default.
5. `ZSH_TMUX_FIXTERM`: When running tmux, the variable `$TERM` is supposed to be set to `screen` or one of its derivatives. This option will set the `default-terminal` option of tmux to `screen-256color` if 256 color terminal support is detected, and `screen` otherwise. The term values it uses can be overridden by changing the `ZSH_TMUX_FIXTERM_WITH_256COLOR` and `ZSH_TMUX_FIXTERM_WITHOUT_256COLOR` variables respectively. Set to `true` by default.

If the user specifies any arguments for `tmux` then the command is just executed as it was typed it without any modification.

tmuxinator
----------

Completions for [tmuxinator](https://github.com/aziz/tmuxinator). To enable completions for `mux`, a shortcut for tmuxinator, add following alias in your zshrc to overwrite the executable:

```
alias mux=tmuxinator
```

urltools
--------

Adds command line utilities for URL manipulation.

- `urlencode` encodes a string so it compiles with the URL character rules laid out in RFC 1738
- `urldecode` decode a string encoded according to the URL character rules in RFC 1738

vagrant
-------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

- vagrant - autocompletion for Vagrant commands, task names, box names and built-in handy documentation. All in one place.

vi-mode
-------

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

** Read the plugin README file **

- Increase zsh `vi-like` functionality

virtualenvwrapper
-----------------

**Maintainer:** [mispy](https://github.com/mispy)

- virtualenvwrapper - Loads Python's [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) shell tools, and automatically activates virtualenv on cd into git repository with matching name.

web-search
----------

**Maintainer:** [xuhdev](https://github.com/xuhdev)

Adds several commands to do web search. Available commands are:

- `bing`
- `google`
- `yahoo`
- `duckduckgo`

Examples:

- Search for oh-my-zsh on Google: `google oh-my-zsh`
- Search for "What is GitHub" on Bing: `bing what is github`
- Search for "foo bar" on DuckDuckGo: `ddg foo bar`

yii
---

**Maintainer:** [IgorTimoshenko](https://github.com/IgorTimoshenko)

[Yii](http://yiiframework.com) autocompletion plugin.

### Aliases

- `yiic = 'protected/yiic'`

yii2
---

**Maintainer:** [ekaragodin](https://github.com/ekaragodin)

[Yii2](http://yiiframework.com) autocompletion plugin.

yum
---

**Maintainer:** [robbyrussell](https://github.com/robbyrussell)

Enables aliases for [Yum](http://yum.baseurl.org), the popular front-end to the RPM Package Manager.

Search package

```
ys - "yum search"
```

Show package info

```
yp - "yum info"
```

List packages

```
yl - "yum list"
```

List package groups

```
ygl - "yum grouplist"
```

Print all installed packages

```
yli - "yum list installed"
```

Rebuilds the yum package list

```
ymc - "yum makecache"
```

Upgrade packages

```
yu - "sudo yum update"
```

Install package

```
yi - "sudo yum install"
```

Install package group

```
ygi - "sudo yum groupinstall"
```

Remove package

```
yr - "sudo yum remove"
```

Remove pagage group

```
ygr - "sudo yum groupremove"
```

Remove package and leaves

```
yrl - "sudo yum remove --remove-leaves"
```

Clean cache

```
yc - "sudo yum clean all"
```

zeus
----

**Homepage:** [Zeus project](https://github.com/burke/zeus)

### Aliases

**Maintainer:** [Bamboo](https://github.com/b4mboo)

- `zi` aliases `zeus init`
- `zinit` aliases `zeus init`
- `zs` aliases `zeus start`
- `ztart` aliases `zeus start`
- `zc` aliases `zeus console`
- `zonsole` aliases `zeus console`
- `zsr` aliases `zeus server`
- `zerver` aliases `zeus server`
- `zr` aliases `zeus rake`
- `zake` aliases `zeus rake`
- `zg` aliases `zeus generate`
- `zenerate` aliases `zeus generate`
- `zrn` aliases `zeus runner`
- `zunner` aliases `zeus runner`
- `zcu` aliases `zeus cucumber`
- `zucumber` aliases `zeus cucumber`
- `zt` aliases `zeus test`
- `zest` aliases `zeus test`
- `zu` aliases `zeus test test/unit/*`
- `zunits` aliases `zeus test test/unit/*`
- `zf` aliases `zeus test test/functional/*`
- `zunctional` aliases `zeus test test/functional/*`
- `za` aliases `zeus test test/unit/*; zeus test test/functional/; zeus cucumber`
- `zall` aliases `zeus test test/unit/*; zeus test test/functional/; zeus cucumber`
- `zsw` aliases `rm .zeus.sock`
- `zweep` aliases `rm .zeus.sock`

### Completion

**Maintainer:** [johnjohndoe](https://github.com/johnjohndoe)

Completion plugin for [zeus](https://github.com/burke/zeus). The describing texts are inspired by the texts given in the [documenation of Rails command line tools](http://guides.rubyonrails.org/command_line.html).* [Source](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/zeus/_zeus)

wd
--

**Maintainer:** [mfaerevaag](https://github.com/mfaerevaag)

`wd` (warp directory) lets you jump to custom directories in zsh, without using cd. Why? Because cd seems inefficient when the folder is frequently visited or has a long path. [Source](https://github.com/mfaerevaag/wd)

### Usage

- Add warp point to current working directory:

```
wd add test
```

If a warp point with the same name exists, use `add!` to overwrite it.
- From an other directory, warp to test with:

```
wd test
```
- You can warp back to previous directory, and so on, with the puncticulation syntax:

```
wd ..
wd ...
```

This is a wrapper for the zsh `dirs` function.
- Remove warp point test point:

```
wd rm test
```
- List warp points to current directory (stored in `~/.warprc`):

```
wd show
```
- List all warp points (stored in `~/.warprc`):

```
wd ls
```
- Print usage with no opts or the `help` argument.
