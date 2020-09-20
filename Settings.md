# Settings

## Main settings

These are the main variables which control Oh My Zsh. Some are required and some are optional, this is specified next to the setting name. **NOTE:** these variables need to be declared **before** Oh My Zsh is sourced in your `.zshrc` file.

### `ZSH`

(_Required_) This variable points to the path of the Oh My Zsh folder. _By default_, Oh My Zsh is installed in `$HOME/.oh-my-zsh`, but if you ran the installer with a different path this will be set accordingly in your `.zshrc` file.

```zsh
export ZSH="$HOME/.oh-my-zsh"
```

If this variable is not set the behavior of Oh My Zsh is undefined, meaning there may be things that break without a warning, so it's always best to set it.

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
