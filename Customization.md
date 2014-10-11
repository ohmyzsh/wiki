oh-my-zsh is fully configurable to your needs with the help of the `$ZSH_CUSTOM` variable, whether you want to change its internals, plugins or the rich theme set - and all that **without forking**!

Initially `$ZSH_CUSTOM` points to oh-my-zsh's `custom` directory. Whatever you place inside of it will take precedence over the built-in configuration.

[[_TOC_]]

#### Overriding and adding plugins

Let's say you created your own plugin `foobar` and want to add it to your configuration.

```zsh
# Your .zshrc
plugins=(git bundler foobar)
```

Then, create a `foobar` directory inside the `plugins` folder and an initialization script to launch your plugin. This script has to follow a naming convention, as all plugin files must have an ending of `.plugin.zsh`. Your file tree should look like this:


```
zsh_custom
└── plugins
    └── foobar
        └── foobar.plugin.zsh
```

Also follow these steps if you want to override plugins that ship with your oh-my-zsh installation. In case it's the rvm plugin you want to override, create the directory `custom/plugins/rvm` and place a file called `rvm.plugin.zsh` inside of it.

A word of warning: None of the original rvm plugin files will get sourced if you define a custom rvm plugin. If you want to customize just a single public function of a plugin, use the approach as outlined in the section below that tells you about how to override internals.

#### Overriding and adding themes

Adding and customizing your own themes pretty much works the same as with plugins.

Themes are located in a `themes` folder and must end with `.zsh-theme`.

```
zsh_custom
└── themes
    └── my_awesome_theme.zsh-theme
```

and within your .zshrc,

```zsh
ZSH_THEME="my_awesome_theme"
```

Remember that customizations always take precedence over built-ins. If you happen to enjoy a particular theme that comes packaged with oh-my-zsh, but would like to change just a little detail inside of it - let's say you love the `agnoster` theme, it will be the easiest to copy the `agnoster.zsh-theme` file to your `custom/themes` directory and customize it.

If you don't change its filename, your `.zshrc` file can stay the same: `ZSH_THEME="agnoster"` will be perfect and still take your changes into account. You might also want to consider this before filing a new issue or pull request that just changes a trivial detail inside of a built-in theme.

Hint: Using a random theme with `$ZSH_THEME="random"` will not look into your custom themes directory. Only built-in themes will be used.

#### Overriding internals

oh-my-zsh's internals are defined in its `lib` directory. To change them just create a file inside the `custom` directory (its name doesn't matter, as long as it has a `.zsh` ending) and start customizing whatever you want. Unsatisfied with the way `git_prompt_info()` works? Ride your own implementation!

```zsh
# custom/my_patches.zsh
function git_prompt_info() {
  # prove that you can do better
}
```

Such customization files will always be the last thing that oh-my-zsh sources before handing over control to your terminal. Also use this approach if you want to override specific details of built-in plugins.


#### Using another customization directory

If you don't want to use the built-in `custom` directory itself, just change the path of `$ZSH_CUSTOM` inside your `.zshrc` to a directory of your own liking. Everything will be fine as long as you adhere to the conventional file hierarchy.

```zsh
# your .zshrc
ZSH_CUSTOM=$HOME/my_customizations
```

File tree inside of your home directory:

```
$HOME
└── my_customizations
    ├── my_lib_patches.zsh
    ├── plugins
    │   └── my_plugin
    │       └── my_plugin.plugin.zsh
    └── themes
        └── my_awesome_theme.zsh-theme
```

### Version control of customizations

By default git is set to ignore the custom directory, so that oh-my-zsh's update process does not interfere with your customizations. If you want to use a version control system like git for your personal changes, just initialize an own repository inside the `custom` directory (`git init`), or point `$ZSH_CUSTOM` to another directory you have under version control.
