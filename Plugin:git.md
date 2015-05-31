## The git Plugin

The [git](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/git) plugin provides many [aliases](#Aliases) and a few useful [functions](#Functions).

Enable it by adding _git_ to the [_plugins array_](https://github.com/robbyrussell/oh-my-zsh/blob/master/templates/zshrc.zsh-template#L48) before sourcing OMZ (see [[Plugins]]).

## Aliases

| Alias                | Command                                                                |
|:---------------------|:-----------------------------------------------------------------------|
| g                    | git                                                                    |
| gst                  | git status                                                             |
| gd                   | git diff                                                               |
| gdc                  | git diff --cached                                                      |
| gdv                  | git diff -w "$@" | view -                                              |
| gl                   | git pull                                                               |
| gup                  | git pull --rebase                                                      |
| gp                   | git push                                                               |
| gc                   | git commit -v                                                          |
| gc!                  | git commit -v --amend                                                  |
| gca                  | git commit -v -a                                                       |
| gca!                 | git commit -v -a --amend                                               |
| gcmsg                | git commit -m                                                          |
| gco                  | git checkout                                                           |
| gcm                  | git checkout master                                                    |
| gr                   | git remote                                                             |
| grv                  | git remote -v                                                          |
| grmv                 | git remote rename                                                      |
| grrm                 | git remote remove                                                      |
| grset                | git remote set-url                                                     |
| grup                 | git remote update                                                      |
| grbi                 | git rebase -i                                                          |
| grbc                 | git rebase --continue                                                  |
| grba                 | git rebase --abort                                                     |
| gb                   | git branch                                                             |
| gba                  | git branch -a                                                          |
| gcount               | git shortlog -sn                                                       |
| gcl                  | git config --list                                                      |
| gcp                  | git cherry-pick                                                        |
| glg                  | git log --stat --max-count=10                                          |
| glgg                 | git log --graph --max-count=10                                         |
| glgga                | git log --graph --decorate --all                                       |
| glo                  | git log --oneline --decorate --color                                   |
| glog                 | git log --oneline --decorate --color --graph                           |
| gss                  | git status -s                                                          |
| ga                   | git add                                                                |
| gm                   | git merge                                                              |
| grh                  | git reset HEAD                                                         |
| grhh                 | git reset HEAD --hard                                                  |
| gclean               | git reset --hard && git clean -dfx                                     |
| gwc                  | git whatchanged -p --abbrev-commit --pretty=medium                     |
| gpoat                | git push origin --all && git push origin --tags                        |
| gmt                  | git mergetool --no-prompt                                              |
| gg                   | git gui citool                                                         |
| gga                  | git gui citool --amend                                                 |
| gk                   | gitk --all --branches                                                  |
| gsts                 | git stash show --text                                                  |
| gsta                 | git stash                                                              |
| gstp                 | git stash pop                                                          |
| gstd                 | git stash drop                                                         |
| grt                  | cd $(git rev-parse --show-toplevel || echo ".")                        |
| git-svn-dcommit-push | git svn dcommit && git push github master:svntrunk                     |
| gsr                  | git svn rebase                                                         |
| gsd                  | git svn dcommit                                                        |
| g                    | git                                                                    |
| ggpull               | git pull origin $(current_branch)                                      |
| ggpur                | git pull --rebase origin $(current_branch)                             |
| ggpush               | git push origin $(current_branch)                                      |
| ggpnp                | git pull origin $(current_branch) && git push origin $(current_branch) |
| glp                  | Prints log with specified [format](http://git-scm.com/docs/git-log)    |

## Functions

### Current

| Command            | Description                             |
|:-------------------|:----------------------------------------|
| current_branch     | Return the name of the current branch   |
| current_repository | Return the names of the current remotes |

### WiP

These features allow to pause a branch development and switch to another one (_"Work in Progress"_,  or wip). When you want to go back to work, just unwip it.

| Command          | Description                                     |
|:-----------------|:------------------------------------------------|
| work_in_progress | Echoes a warning if the current branch is a wip |
| gwip             | Commit wip branch                               |
| gunwip           | Uncommit wip branch                             |
