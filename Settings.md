# Settings

<!-- TOC depthFrom:2 -->

- [Main settings](#main-settings)
  - [`ZSH`](#zsh)
  - [`ZSH_THEME`](#zsh_theme)
  - [`plugins`](#plugins)
  - [`ZSH_CUSTOM`](#zsh_custom)
  - [`ZSH_CACHE_DIR`](#zsh_cache_dir)
- [Completion settings](#completion-settings)
  - [`ZSH_COMPDUMP`](#zsh_compdump)
  - [`ZSH_DISABLE_COMPFIX`](#zsh_disable_compfix)
- [Library settings](#library-settings)
- [Random theme](#random-theme)
  - [`ZSH_THEME_RANDOM_CANDIDATES`](#zsh_theme_random_candidates)
  - [`ZSH_THEME_RANDOM_IGNORED`](#zsh_theme_random_ignored)
  - [`ZSH_THEME_RANDOM_QUIET`](#zsh_theme_random_quiet)

<!-- /TOC -->

## Main settings

These are the main variables which control Oh My Zsh. Some are required and some are optional, this is specified next to the setting name. **NOTE: these variables need to be declared _before_ Oh My Zsh is sourced in your `.zshrc` file.**

### `ZSH`

(_Required_) This variable points to the path of the Oh My Zsh folder. _By default_, Oh My Zsh is installed in `$HOME/.oh-my-zsh`, but if you ran the installer with a different path this will be set accordingly in your `.zshrc` file.

```zsh
export ZSH="$HOME/.oh-my-zsh"
```

It's important that this variable is set, but if it isn't, Oh My Zsh will try to determine its value when loading Oh My Zsh to the directory where the init script (`oh-my-zsh.sh`) is located.

### `ZSH_THEME`

(_Optional_) This variable holds the name of the Oh My Zsh you want to use. See [[Themes]] for valid theme names, or [[External themes]] for themes that aren't included in Oh My Zsh. For example:

```zsh
ZSH_THEME=agnoster
```

If this is not set, Oh My Zsh will not load any themes and you'll get the default zsh prompt.

**NOTE:** if there's a built-in theme and a custom theme of the same name, the custom theme has preference, meaning it will be loaded instead of the built-in one.

### `plugins`

(_Optional_) (<u>array</u>) This variable is an array containing the plugins that should be loaded when loading Oh My Zsh. See [[Plugins]] for valid plugins and the link to their README. Note that, in zsh, array elements are separated by spaces (do not use commas). For example:

```zsh
plugins=(git dircycle autojump)
```

The order of the plugins in the array controls the order in which they'll be loaded. In the example above, the `git` plugin will be loaded first, then the `dircycle` plugin and then the `autojump` plugin.

**NOTE:** as it happens with themes, if there's a custom plugin of the same name as a built-in one, the custom plugin will be loaded instead.

### `ZSH_CUSTOM`

(_Optional_) Path to the custom folder. _By default_, this variable points to `$ZSH/custom`. This variable is useful to, for instance, put the custom folder on another location so as to manage it with a version control system. For example:

```zsh
ZSH_CUSTOM=~/code/ohmyzsh-custom
```

### `ZSH_CACHE_DIR`

(_Optional_) Path to the cache folder. This folder is used to store and cache all sorts of data used by plugins and completion scripts. _By default_, this variable points to `$ZSH/cache`, but you can put it wherever else you see fit. For example:

```zsh
ZSH_CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/ohmyzsh"
```

## Completion settings

### `ZSH_COMPDUMP`

(_Optional_) Path to the completion cache file. _By default_, the name of the cache file is computed using the `$SHORT_HOST` (hostname) and `$ZSH_VERSION` variables, and put in either `$ZDOTDIR` or `$HOME`. You can change it to avoid cluttering your home directory. For example:

```zsh
# If $ZSH_CACHE_DIR is already defined
ZSH_COMPDUMP="$ZSH_CACHE_DIR/.zcompdump"
```

As explained in the [[FAQ]], you can reset the completion cache file by `rm`-ing it and restarting the zsh session:

```zsh
rm "$ZSH_COMPDUMP"
exec zsh
```

### `ZSH_DISABLE_COMPFIX`

(_Optional_) Zsh automatically detects directories in `$fpath` that might have insecure permissions. These are directories that are checked when loading completion functions or other functions, so if a directory has insecure permissions, it could mean that you end up running code that a malicious actor put there.

**You only need to use this setting when** the directories detected by Zsh have secure permissions but you still get the warning message. By setting this variable to `true`, you won't get the warning anymore. For example:

If you get this or a similar warning in macOS:

```console
[oh-my-zsh] Insecure completion-dependent directories detected:
drwxr-xr-x  3 john  admin   96 Jul 25 23:13 /usr/local/share/zsh
drwxr-xr-x  4 john  admin  128 Jul 26 03:38 /usr/local/share/zsh/site-functions
```

you can safely ignore it as long as you control the `john` user, which has write permissions in both those directories. To do that, set the `ZSH_DISABLE_COMPFIX` variable, **before** Oh My Zsh is sourced in your `.zshrc` file:

```zsh
ZSH_DISABLE_COMPFIX=true
```

## Random theme

These settings only work if the random theme is selected (`ZSH_THEME=random`).

### `ZSH_THEME_RANDOM_CANDIDATES`

(<u>Array</u>) If this variable is set, the random theme will choose only one of the themes specified in this array. **Otherwise**, the random theme chooses one from all the themes found in `$ZSH/themes` and `$ZSH_CUSTOM`. For example:

```zsh
ZSH_THEME_RANDOM_CANDIDATES=(robbyrussell af-magic ys)
```

In this example, only 1 of these 3 themes will be selected at random. This is useful when you've used the random theme enough that you know specifically the themes that you like.

**NOTE:** if this variable is set, the `ZSH_THEME_RANDOM_IGNORED` setting has no effect.

### `ZSH_THEME_RANDOM_IGNORED`

(<u>Array</u>) If this variable is set the random theme won't choose any of the themes specified in this array. This is useful if you know specifically the themes that you don't like or don't work correctly in your environment. For example:

```zsh
ZSH_THEME_RANDOM_IGNORED=(agnoster pygmalion rkj)
```

In this example, the random theme will remove these 3 themes from the pool of candidates to choose from.

**NOTE:** if the `ZSH_THEME_RANDOM_CANDIDATES` variable is set (see above), this setting has no effect.

### `ZSH_THEME_RANDOM_QUIET`

If this variable is set to a value (`true` or `1`), the random theme will not show a startup message indicating which theme was chosen. For example:

```zsh
ZSH_THEME_RANDOM_QUIET=true
```

If this is set and you want to know which theme was chosen, you can `echo $RANDOM_THEME` to show the theme name.
