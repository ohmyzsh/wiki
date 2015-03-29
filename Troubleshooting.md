This page is meant to describe the most common problems with oh-my-zsh and what you can do to diagnose them:

### Keyboard shortcut problems

Example: 
```sh
bindkey '^L' clear-screen
```

Two main things could go wrong:

1. The key sequence (`^L` in the example) does not match the key sequence being sent to the terminal:  

   You can see the exact sequence a keyboard shortcut sents by pressing `CTRL`+`V` and then the keyboard shortcut.  
   For example: `CTRL`+`V`, `CTRL`+`L` will output `^L` (`^` represents the Control key).

2. The command executed (`clear-screen` in the example) has an error. In that case, post both the key binding and the definition of the command (if exists) like so:

   - **key binding:** `bindkey '^[[1;6D'`  
     will print `"^[[1;6D" insert-cycledleft`
   - **command definition:** `which insert-cycledleft`  
     will print `insert-cycledleft () { ... }`
  
     Notice that sometimes the command is a builtin [zle widget](http://zsh.sourceforge.net/Doc/Release/Zsh-Line-Editor.html) and so the `which` command won't work. If that's the case, just post the key binding and we'll figure it out.

### Completion problems

*...to be filled...*


### Everything else

*...to be filled...*
