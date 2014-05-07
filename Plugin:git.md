# The `git` plugin

The `git` [plugin](Plugins#git) provides many [aliases](#Aliases) and a few useful [functions](Functions).

Enable it by adding `git` to the [`plugins` array](https://github.com/robbyrussell/oh-my-zsh/blob/master/templates/zshrc.zsh-template#L51) before sourcing OMZ.

## Aliases

<table>
<tr><th>Alias</th><th>Command</th></tr>
<tr><td><pre>g</pre></td><td><pre>git</pre></td></tr>
<tr><td><pre>gst</pre></td><td><pre>git status</pre></td></tr>
<tr><td><pre>gd</pre></td><td><pre>git diff</pre></td></tr>
<tr><td><pre>gdc</pre></td><td><pre>git diff --cached</pre></td></tr>
<tr><td><pre>gl</pre></td><td><pre>git pull</pre></td></tr>
<tr><td><pre>gup</pre></td><td><pre>git pull --rebase</pre></td></tr>
<tr><td><pre>gp</pre></td><td><pre>git push</pre></td></tr>
<tr><td><pre>gd</pre></td><td><pre>git diff</pre></td></tr>
<tr><td><pre>gdv</pre></td><td><pre>git diff -w "$@" | view -</pre></td></tr>
<tr><td><pre>gc</pre></td><td><pre>git commit -v</pre></td></tr>
<tr><td><pre>gc!</pre></td><td><pre>git commit -v --amend</pre></td></tr>
<tr><td><pre>gca</pre></td><td><pre>git commit -v -a</pre></td></tr>
<tr><td><pre>gca!</pre></td><td><pre>git commit -v -a --amend</pre></td></tr>
<tr><td><pre>gcmsg</pre></td><td><pre>git commit -m</pre></td></tr>
<tr><td><pre>gco</pre></td><td><pre>git checkout</pre></td></tr>
<tr><td><pre>gcm</pre></td><td><pre>git checkout master</pre></td></tr>
<tr><td><pre>gr</pre></td><td><pre>git remote</pre></td></tr>
<tr><td><pre>grv</pre></td><td><pre>git remote -v</pre></td></tr>
<tr><td><pre>grmv</pre></td><td><pre>git remote rename</pre></td></tr>
<tr><td><pre>grrm</pre></td><td><pre>git remote remove</pre></td></tr>
<tr><td><pre>grset</pre></td><td><pre>git remote set-url</pre></td></tr>
<tr><td><pre>grup</pre></td><td><pre>git remote update</pre></td></tr>
<tr><td><pre>grbi</pre></td><td><pre>git rebase -i</pre></td></tr>
<tr><td><pre>grbc</pre></td><td><pre>git rebase --continue</pre></td></tr>
<tr><td><pre>grba</pre></td><td><pre>git rebase --abort</pre></td></tr>
<tr><td><pre>gb</pre></td><td><pre>git branch</pre></td></tr>
<tr><td><pre>gba</pre></td><td><pre>git branch -a</pre></td></tr>
<tr><td><pre>gcount</pre></td><td><pre>git shortlog -sn</pre></td></tr>
<tr><td><pre>gcl</pre></td><td><pre>git config --list</pre></td></tr>
<tr><td><pre>gcp</pre></td><td><pre>git cherry-pick</pre></td></tr>
<tr><td><pre>glg</pre></td><td><pre>git log --stat --max-count=10</pre></td></tr>
<tr><td><pre>glgg</pre></td><td><pre>git log --graph --max-count=10</pre></td></tr>
<tr><td><pre>glgga</pre></td><td><pre>git log --graph --decorate --all</pre></td></tr>
<tr><td><pre>glo</pre></td><td><pre>git log --oneline --decorate --color</pre></td></tr>
<tr><td><pre>glog</pre></td><td><pre>git log --oneline --decorate --color --graph</pre></td></tr>
<tr><td><pre>gss</pre></td><td><pre>git status -s</pre></td></tr>
<tr><td><pre>ga</pre></td><td><pre>git add</pre></td></tr>
<tr><td><pre>gm</pre></td><td><pre>git merge</pre></td></tr>
<tr><td><pre>grh</pre></td><td><pre>git reset HEAD</pre></td></tr>
<tr><td><pre>grhh</pre></td><td><pre>git reset HEAD --hard</pre></td></tr>
<tr><td><pre>gclean</pre></td><td><pre>git reset --hard && git clean -dfx</pre></td></tr>
<tr><td><pre>gwc</pre></td><td><pre>git whatchanged -p --abbrev-commit --pretty=medium</pre></td></tr>
<tr><td><pre>gpoat</pre></td><td><pre>git push origin --all && git push origin --tags</pre></td></tr>
<tr><td><pre>gmt</pre></td><td><pre>git mergetool --no-prompt</pre></td></tr>
<tr><td><pre>gg</pre></td><td><pre>git gui citool</pre></td></tr>
<tr><td><pre>gga</pre></td><td><pre>git gui citool --amend</pre></td></tr>
<tr><td><pre>gk</pre></td><td><pre>gitk --all --branches</pre></td></tr>
<tr><td><pre>gsts</pre></td><td><pre>git stash show --text</pre></td></tr>
<tr><td><pre>gsta</pre></td><td><pre>git stash</pre></td></tr>
<tr><td><pre>gstp</pre></td><td><pre>git stash pop</pre></td></tr>
<tr><td><pre>gstd</pre></td><td><pre>git stash drop</pre></td></tr>
<tr><td><pre>grt</pre></td><td><pre>cd $(git rev-parse --show-toplevel || echo ".")</pre></td></tr>
<tr><td><pre>git-svn-dcommit-push</pre></td><td><pre>git svn dcommit && git push github master:svntrunk</pre></td></tr>
<tr><td><pre>gsr</pre></td><td><pre>git svn rebase</pre></td></tr>
<tr><td><pre>gsd</pre></td><td><pre>git svn dcommit</pre></td></tr>
</table>

## Functions

### Current *

* `current_branch`
> Returns the name of the current branch
_Example:_ `git pull origin $(current_branch)`

* `current_repository`
> Returns the names of the current remotes

<table>
<tr><th>Alias</th><th>Command</th></tr>
<tr><td><pre>g</pre></td><td><pre>git</pre></td></tr>
<tr><td><pre>ggpull</pre></td><td><pre>git pull origin $(current_branch)</pre></td></tr>
<tr><td><pre>ggpur</pre></td><td><pre>git pull --rebase origin $(current_branch)</pre></td></tr>
<tr><td><pre>ggpush</pre></td><td><pre>git push origin $(current_branch)</pre></td></tr>
<tr><td><pre>ggpnp</pre></td><td><pre>git pull origin $(current_branch) && git push origin $(current_branch)</pre></td></tr>
</table>

### Pretty log messages

* `glp`
> Prints log with specified [format](http://git-scm.com/docs/git-log)
_Example:_ `glp "%h - %an, %ar : %s"`

* `glp`
> Prints log with specified [format](http://git-scm.com/docs/git-log)
_Example:_ `glp "%h - %an, %ar : %s"`

### WiP

These features allow to pause a branch development and switch to another one (_"Work in Progress"_, or wip). When you want to go back to work, just unwip it.

* `work_in_progress`
> Echoes a warning if the current branch is a wip

* `gwip`
> Commit wip branch

* `gunwip`
> Uncommit wip branch

