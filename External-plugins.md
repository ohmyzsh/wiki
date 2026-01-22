<!-- prettier-ignore-start -->
> _This wiki is automatically published from [ohmyzsh/wiki](https://github.com/ohmyzsh/wiki). To edit this page,_
> _go to [ohmyzsh/wiki](https://github.com/ohmyzsh/wiki), make your changes and submit a Pull Request._
<!-- prettier-ignore-end -->

## Non-Bundled Plugins

Unlike [themes](https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes), there are no restrictions for integrating your plugin into the zsh bundle. However, the purpose of creating this page is to address a common concern: uncertainty about whether your plugin might inadvertently cause harm, potentially disrupting the system or its functionalities.

**Installation**: Clear instructions are crucial and should adhere to these [guidelines](https://github.com/ohmyzsh/ohmyzsh/wiki/Customization#overriding-and-adding-plugins).

---

### CLI

- [fz](https://github.com/changyuheng/fz)

  Give tab-completions to `z`.

  [![fz demo](https://github.com/changyuheng/fz/raw/master/fz-demo.gif)](https://github.com/changyuheng/fz/blob/master/fz-demo.gif)

- [tenv](https://github.com/tofuutils/zsh-tenv)

  tofuutils tenv plugin providing autocompletions

- [zsh-copilot](https://github.com/Gamma-Software/zsh-copilot)

  Integrate ChatGPT to your terminal so that you can predict your next command based on command history. Ask to generate complexe commands. Or Fix a previous failed command.

- [Databricks CLI Plugin](https://github.com/SlavaYakovenko/zsh-databricks)
  Enhanced Databricks CLI integration for Zsh with convenient aliases and profile management.
  This plugin provides a set of convenient aliases and functions to streamline your Databricks workflow. All commands use the dbrs prefix to avoid conflicts with existing tools.

- [Docker ps output colorized](https://github.com/bouteillerAlan/dockolor)

  `dockolor` is a lightweight plugin that enhances your docker ps experience with color-coded output based on container status. It also replaces common aliases like dps and dpsa if defined.

### FUN

- [Doge Say](https://github.com/txstc55/dogesay/blob/master/dogesay.plugin.zsh)

  Get a doge to repeat every command you put in! See it in action:

  ![Alt Text](https://raw.githubusercontent.com/txstc55/dogesay/master/dogesay.gif)

### GIT

- [Auto Status](https://gist.github.com/oshybystyi/475ee7768efc03727f21)

  If you found yourself constantly typing `git status` after bunch of commands like
  `git commit` and you want to avoid that, then this plugin is for you. This plugin is a nice addition to **git_prompt_status**.

- [Branch](https://github.com/cpwillis/omz-git-branch)

  This plugin visually formats the current git branch name or commit hash, considering customizable variables like hiding status, maximum branch length, prefix, and suffix trimming, with an option to display git status. For example;

  ```
  abc-custom-feature-xyz-12345678       -->  custom-fe...12345678
  user123/repo-9876/fix-bug-in-feature  -->  9876/fix...-feature
  ```

- [git-clean-branches](https://github.com/adelbeke/git-clean-branches)

  Interactive git branch deletion tool with a beautiful UI powered by [gum](https://github.com/charmbracelet/gum). Shows branch info with last commit date and message. Automatically protects current branch and main/master branches.

- [git-switch-branch](https://github.com/adelbeke/git-switch-branch)

  Interactive git branch switching tool with gum-powered UI. Displays branch info with last commit date and message. Warns about uncommitted changes with optional auto-stash.

- [Custom Git](https://github.com/davidde/git)

  A small, tidy, lightweight notes app that creates a daily text file and timestamps every line of added text

- [Mingit](https://github.com/evansendra/mingit/tree/master/mingit-ohmyzsh)

  An alternative to the default ohmyzsh git plugin.

  ```
  g a .                      // git add .
  g b other-branch           // git branch other-branch
  g b which                  // git branch --show-current (note this assumes git version >= 2.22)
  g c -m "made some changes" // git commit -m "made some changes"
  g co master                // git checkout master
  g d                        // git diff
  g f                        // git fetch
  g i                        // git init
  g m hotfix                 // git merge hotfix
  g pll                      // git pull
  g psh                      // git push
  g r                        // git reset
  g rsto                     // git restore
  g s                        // git status

  // autocompletions
  $ g co <TAB><TAB>
  HEAD         master       second-branch   ORIG_HEAD
  ```

### GPG

- [History Sync](https://github.com/wulfgarpro/history-sync)

  GPG encrypted, Internet synchronized Zsh history using Git.

### NOTES

- [aterminal](https://github.com/guiferpa/aterminal)

  This plugin show platforms version.

  ![Demo](https://raw.githubusercontent.com/guiferpa/aterminal/master/images/demo.gif)

- [Bookmark](https://github.com/calmzhu/ohmyzsh-plugin-bookmark)

  Yet another ohmyzsh plugin to quick jump between cmdline directories with an intuitive design. _Add path to bookmarks, return an ordered number and use the numbers to switch between dirs finally._

- [zshnotes](https://github.com/jameshgrn/zshnotes)

  A small, tidy, lightweight notes app that creates a daily text file and timestamps every line of added text

### NODE

- [node-bin](https://github.com/remcohaszing/zsh-node-bin)

  Add `node_modules/.bin` directories to your `$PATH`.

### PYTHON

- [viper-env](https://github.com/DanielAtKrypton/viper-env)

  Automatically activates and deactivates python virtualenv upon cd in and out.

  ![Demo](https://github.com/DanielAtKrypton/viper-env/raw/master/make_animation/assets/final.svg)

### SSH

- [tmux-ssh-syncing](https://github.com/alberti42/tmux-ssh-syncing)

	Synchronize your [tmux](https://github.com/tmux/tmux/wiki) window names with active ssh sessions. This plugin dynamically updates the tmux window name to reflect the remote hosts of active ssh sessions in the same window. It also restores the original window name when all ssh sessions are closed.

	<img src="https://github.com/alberti42/tmux-ssh-syncing/blob/main/doc/screencast.gif" alt="Screencast" />

- [xxh](https://github.com/xxh/xxh)

  Bring Oh My Zsh wherever you go through the SSH. This allows you to bring Zsh with Oh My Zsh framework to the remote host without any installations, root access or affection on the host.

---

### UNORGANISED

- [TEMPLATE](https://github.com/cpwillis)

  I'm a template... when adding a new plugin, please follow my structure or copypasta me. Organise your addition into the existing sub-headings **alphabetically** (or make a new one). If you're unsure, just add it below and someone will organise it for you. :)
