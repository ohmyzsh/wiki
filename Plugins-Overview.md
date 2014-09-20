* [Productivity](Plugins-Overview#productivity) 
* [FS jumping](Plugins-Overview#fs-jumping) 
* [Build tools](Plugins-Overview#build-tools) 
* [Node JS](Plugins-Overview#node-js) 
* [PHP](Plugins-Overview#php) 
* [Ruby](Plugins-Overview#ruby) 
* [Python](Plugins-Overview#python) 
* [Distro-related](Plugins-Overview#distro-related) 
* [MacOS](Plugins-Overview#macos) 
* [Misc](Plugins-Overview#misc) 

### About
Last review date: 20-Nov-13

### Productivity
Name              | Description                                                      |
------------------|------------------------------------------------------------------|
autoenv           | automaticly execs script on changing dir (.env file)             |
colemak           | colemak layout support + vi-mode fixes for colemak http://en.wikipedia.org/wiki/Keyboard_layout#Colemak                                 |
colored-man       | adds colors to manpages                                          |
colorize          | cat with syntax highlight support                                |
command-not-found | suggests package name with relevant command                      |
compleat          | reformats completion http://github.com/mbrubeck/compleat         |
copydir           | copies current dir full path to clipboard                        |
copyfile          | copies selected file content to clipboard                        |
cp                | cp with progress bar (rsync)                                     |
dircycle          | hotkeys fot cycling directories                                  |
dirpersist        | saves and restores your directory stack across shell invocations |
encode64          | e64 & d64 aliases                                                |
extract           | 'x' alias - swiss knife for archive extracting                   |
fbterm            | enhanced VESA terminal https://code.google.com/p/fbterm/         |
gpg-agent         | gpg-agent start/stop funcs                                       |
history           | aliases: h for history, hsi for grepping history                 |
history-substring-search** |  implementation of fish history substring search     |
kate              |   Kate text editor alias http://kate-editor.org/
last-working-dir  |     same as dirpresist
mosh |     mobile shell with roaming (wifi, mobile networks) and local echo http://mosh.mit.edu/
pass |    pass utility autocompletion
per-directory-history |     self-descriptive
profiles |     different zsh profiles per hostname
rsync |    aliases
safe-paste |    extended copy/paste in terminal
screen |    GNU screen enhances (titles etc)
sprunge |  CLI pastbin service sprunge.us uploader (http://www.shellperson.net/sprunge-pastebin-script/)
ssh-agent |     ssh-agent start script
sublime |     aliases for SublimeText Editor 
supervisor |    autocompletion for http://supervisord.org
taskwarrior |    autocompletion for http://taskwarrior.org
terminitor | **[RENAMED to consular]** Consular automates your development workflow setup https://github.com/achiu/consular
tmux tmuxinator |    enchanced Tmux support
torrent | magnet2torrent converter function
urltools | urlencode/urldecode etc
vi-mode |     self descriptive
vundle|     Vim plugin manager  http://github.com/gmarik/vundle
wakeonlan |    funcs for wakeonlan tool
web-search |    google from CLI



** (To make it work on Ubuntu do `echo DEBIAN_PREVENT_KEYBOARD_CHANGES=yes>>~/.zshenv`).


### FS Jumping
Name              | Description                                                      |
------------------|------------------------------------------------------------------|
autojump          | shell extension to jump to frequently used directories           |
fasd              | quick access to files and dirs https://github.com/clvv/fasd      |
jump              | allows to mark dirs and jump to marks                           |
pj |     aliases for quick access to projects dir
wd |    yet another autojump tool github.com/mfaerevaag/wd
z |     yet another autojump

### Build tools
Name     | Description                                                                    |
---------|--------------------------------------------------------------------------------|
ant      | Java build tool http://ant.apache.org/                                         |
bower    | Front-end package manager https://github.com/bower/bower                       |
cabal    | Haskell package manager http://www.haskell.org/cabal/                          |
cake     | CoffeeScript build tool                                                        |
coffee   | CoffeeScript completion                                                        |
cpanm    | cpanminus get, unpack, build, install Perl modules https://github.com/miyagawa/cpanminus/ |
docker   | application shipment tool https://github.com/dotcloud/docker                   |
gas      | small utility used to manage Git authors. https://github.com/walle/gas         | 
git      | extras: git-extras gitfast git-flow git-flow-avh git-hubflow git-remote-branch |
github   | cli access, url shortener                                                      |
gitignore| gi alias to fetch default .gitignore files from http://gitignore.io/           |
gnu-utils| GNU coreutils wrappers to override shell builtins                              |
go       | Go build tool http://golang.org/cmd/go/                                        |
golang   | **[DUPLICATE]** indetical to 'go'. Should be removed?                          |
gradle   | build automation tool http://www.gradle.org/                                   |
grails   | funcs for grails scritp managment http://grails.org/
heroku   | cli access https://www.heroku.com/
jira      | JIRA cli access
knife knife_ssh |   knife autocompletion http://docs.opscode.com/knife.html
lein      | leiningen autocompletion http://leiningen.org
lighthouse| CLI access ot issue tracker Lighthouse, http://lighthouseapp.com/
mercurial | hg autocompletion
mix       | Elixir build tool autocompletion http://elixir-lang.org/docs/stable/Mix.html
mvn       | maven completion
nanoc     | static website generator http://nanoc.ws/
postgres |   aliases for Postgres managing
perl | aliases for Perl
rebar |    Eralng build tool autocompletion
redis-cli |    Redis autocompletion
repo |    git repo managment tool autocompletion https://code.google.com/p/git-repo/
sbt |    autocomplete for ScalaBuildTool http://www.scala-sbt.org/
scala |    autocomplete
sfffe |    aliases for ack (JS & CSS grepping) http://beyondgrep.com/
svn |    subversion autocompletion
svn-fast-info |    faster subversion autocompletion (especially interesting on big project)
vagrant | quick development env deployment http://www.vagrantup.com/

### Node JS
Name      | Description                    |
----------|--------------------------------|
jake-node | Node JS build tool Jake https://github.com/mde/jake
node      | NodeJS docs easy access via CLI
npm       | package managerfor NodeJS
nvm       | NodeJs version manager

### PHP
Name       | Description                          |
-----------|--------------------------------------|
composer | PHP dependency manager http://getcomposer.org
laravel | PHP deployment tool artisan completion http://four.laravel.com/docs/artisan
phing | Ant-like build system for PHP http://phing.info
symfony symfony2 | PHP webframework http://symfony.com
yii | PHP webframework http://yiiframework.com

### Ruby
Name       | Description                          |
-----------|--------------------------------------|
bundler    | package manager http://bundler.io/   |
capistrano | remote deployment tool               |
gem        | http://rubygems.org/                 |
jruby      | Jruby aliases
pow |  rack apps restarter http://pow.cx/
powder |     powder gem autocompletion https://github.com/Rodreegez/powder 
powify |    another pow manager https://github.com/sethvargo/powify
rails | rails aliases for rails 2, rails 3, and rails 4 all in one clean plugin
rake | Ruby build tool 
rbenv | ruby version switcher
rbfu | **[OBSOLATE]**  anther Ruby version manager https://github.com/hmans/rbfu
ruby |    aliases
rvm |    another RubyVersionManager
thor | Ruby doc tool https://github.com/erikhuda/thor
zeus |    funcs for Zeus (Rails env preloader) https://github.com/burke/zeus

### Python
Name    | Description                                            |
--------|--------------------------------------------------------|
celery  | Python distributed task queue                          |
django  | https://www.djangoproject.com/                         |
fabric  | remote deployment tool http://docs.fabfile.org/en/1.8/ |
pip |   Python package manager  http://www.pip-installer.org/en/latest/
python  |    python aliases (pyfind, pyclean, pygrep)
virtualenv virtualenvwrapper |    https://pypi.python.org/pypi/virtualenv isolated Python envs


### Distro-related
Name      | Description                    |
----------|--------------------------------|
archlinux | aliases for yaourt and pacman  |
debian    | aliases for apt* utils         |
suse |    aliases for Suse Linux (zypper aliases)
systemd | aliases
yum |    aliases


### MacOS
Name               | Description                                                     |
-------------------|-----------------------------------------------------------------|
apache2-macports   | apache managment functions                                      |
brew               | package manger http://brew.sh/                                  |
bwana              | allows to open manpages in browser http://www.bruji.com/bwana/  |
cloudapp           | completion for cloudapp http://getcloudapp.com/                 |
forklift           | MacOS file browser                                              |
macports  | macport autocompletion
mysql-macports |    same as apache-macport for MySQL
osx | MacOS completions
pod |    http://cocoapods.org library dependency manager for Xcode
terminalapp |    Apple Terminal enhancer
textmate |    aliases

### Misc
Name       | Description                     |
-----------|---------------------------------|
battery    | allows see battery status in PS |
emoji-clock| fancy shell clocks              |
lol | dowant
nyan | Nyancat in terminal (nyanhost is down :( ) 
rand-quote |  quote function for random quoutes from http://www.quotationspage.com/random.php3
themes |    ZSH theme switcher