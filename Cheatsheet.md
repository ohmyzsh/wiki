To try it out if you have just cloned it (to your home directory):

- `source ~/.oh-my-zsh/templates/zshrc.zsh-template`

Commands
========

- `tab` - Create a new tab in the current directory (OS X - req enabling access for assistive devices under sys prefs)
- `take` - Create a new directory and change to it, will create intermediate directories as required.
- `x`/`extract` - Extract an archive (supported types: tar.{bz2,gz,xz,lzma}, bz2, rar, gz, tar, tbz2, tgz, zip, Z, 7z).
- `zsh_stats` - Get a list of the top ten commands and how many times they have been run
- `uninstall_oh_my_zsh` - Uninstall Oh-my-zsh
- `upgrade_oh_my_zsh` - Upgrade Oh-my-zsh

See `~/.oh-my-zsh/lib/directories.zsh`
--------------------------------------

- `alias` lists all aliases
- `..` aliases `cd ..`
- `cd..` aliases `cd ..`
- `cd...` aliases `cd ../..`
- `cd....` aliases `cd ../../..`
- `cd.....` aliases `cd ../../../..`
- `cd/` aliases `cd /`
- `cd +n` to switch to directory number `n`
- `1` aliases `cd -`
- `2` aliases `cd +2`
- `3` aliases `cd +3`
- `4` aliases `cd +4`
- `5` aliases `cd +5`
- `6` aliases `cd +6`
- `7` aliases `cd +7`
- `8` aliases `cd +8`
- `9` aliases `cd +9`
- `md` aliases `mkdir -p`
- `rd` aliases `rmdir`
- `d` aliases `dirs -v`, lists last used directories

Tab-completion
==============

- `ls -(tab)` - For options and helpful text of what they do
- `cap (tab)`
- `rake (tab)`
- `ssh (tab)`
- `sudo umount (tab)`
- `kill (tab)`
- `unrar (tab)`

Git
===

Dynamic access to current branch name with the current_branch function
----------------------------------------------------------------------

- `git pull origin $(current_branch)`
- `grb publish $(current_branch) origin`

Helpful aliases for common git tasks
------------------------------------

- `g` - `git`
- `gst` - `git status`
- `gl` - `git pull`
- `gup` - `git pull --rebase`
- `gp` - `git push`
- `gd` - `git diff`
- `gdc` - `git diff --cached`
- `gdv` - <code>git diff ~~w "$`" | view -</code>
- `gc - `git commit -v`
- `gc!` - `git commit -v --amend`
- `gca` - `git commit -v -a`
- `gca!` - `git commit -v -a --amend`
- `gcmsg` - `git commit -m`
- `gco` - `git checkout`
- `gcm` - `git checkout master`
- `gr` - `git remote`
- `grv` - `git remote -v`
- `grmv` - `git remote rename`
- `grrm` - `git remote remove`
- `gsetr` - `git remote set-url`
- `grup` - `git remote update`
- `grbi` - `git rebase -i`
- `grbc` - `git rebase --continue`
- `grba` - `git rebase --abort`
- `gb` - `git branch`
- `gba` - `git branch -a`
- `gcount` - `git shortlog -sn`
- `gcl` - `git config --list`
- `gcp` - `git cherry-pick`
- `glg` - `git log --stat --max-count=10`
- `glgg` - `git log --graph --max-count=10`
- `glgga` - `git log --graph --decorate --all`
- `glo` - `git log --oneline --decorate --color`
- `glog` - `git log --oneline --decorate --color --graph`
- `gss` - `git status -s`
- `ga` - `git add`
- `gm` - `git merge`
- `grh` - `git reset HEAD`
- `grhh` - `git reset HEAD --hard`
- `gclean` - `git reset --hard && git clean -dfx`
- `gwc` - `git whatchanged -p --abbrev-commit --pretty=medium`
- `gsts` - `git stash show --text`
- `gsta` - `git stash`
- `gstp` - `git stash pop`
- `gstd` - `git stash drop`
- `ggpull` - `git pull origin $(current_branch)`
- `ggpur` - `git pull --rebase origin $(current_branch)`
- `ggpush` - `git push origin $(current_branch)`
- `ggpnp` - `git pull origin $(current_branch) && git push origin $(current_branch)`
- `glp` - `_git_log_prettily`

Editors
-------

- `stt` - `open current directory in Sublime Text 2/3`

Symfony2
--------

- `sf` - `php app/console`
- `sfcl` - `php app/console cache:clear`
- `sfroute` - `php app/console router:debug`
- `sfgb` - `php app/console generate:bundle`
