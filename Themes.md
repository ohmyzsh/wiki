All the current themes can be found in the `themes/` directory in the oh-my-zsh distribution. [See list here.](http://github.com/robbyrussell/oh-my-zsh/tree/master/themes/)

In order to enable a theme, set `ZSH_THEME` to the name of the theme in your `~/.zshrc`, before sourcing Oh My Zsh; for example: `ZSH_THEME=robbyrussell`  
If you do not want any theme enabled, just set `ZSH_THEME` to blank: `ZSH_THEME=""`

Here is a collection of screenshots and descriptions of themes that have been contributed to Oh My Zsh. There are some missing from this page. If you want to add or edit descriptions, see the [format description](#theme-description-format) at the bottom of this page.

## The Themes

### robbyrussell
*the (default) that Robby uses* 

[![robbyrussell](https://cloud.githubusercontent.com/assets/2618447/6316876/710cbb8c-ba03-11e4-90b3-0315d72f270c.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316876/710cbb8c-ba03-11e4-90b3-0315d72f270c.jpg)

------------------------------------

The rest of the themes, in alphabetical order:

### af-magic
[![af-magic](https://cloud.githubusercontent.com/assets/2618447/6316860/70f310d8-ba03-11e4-973c-eb5eb6b5b289.png)](https://cloud.githubusercontent.com/assets/2618447/6316860/70f310d8-ba03-11e4-973c-eb5eb6b5b289.png)

### afowler
[![afowler](https://cloud.githubusercontent.com/assets/2618447/6316859/70f1cb06-ba03-11e4-865f-209473ddd5c8.png)](https://cloud.githubusercontent.com/assets/2618447/6316859/70f1cb06-ba03-11e4-865f-209473ddd5c8.png)

### agnoster
([more info](https://gist.github.com/3712874))

[![agnoster](https://cloud.githubusercontent.com/assets/2618447/6316862/70f58fb6-ba03-11e4-82c9-c083bf9a6574.png)](https://cloud.githubusercontent.com/assets/2618447/6316862/70f58fb6-ba03-11e4-82c9-c083bf9a6574.png)
https://cloud.githubusercontent.com/assets/1441704/11986491/65c9c702-a9d0-11e5-8393-ce262988ab09.png
(Shown with [Solarized Dark colorscheme](http://ethanschoonover.com/solarized) and Powerline-patched Menlo 14pt in [iTerm 2](http://www.iterm2.com/))

Additional setup:

- Install one of the [patched fonts from Vim-Powerline](https://github.com/powerline/fonts) or [patch your own](https://github.com/powerline/fontpatcher) for the special characters.
- *Optionally* set `DEFAULT_USER` in `~/.zshrc` to your regular username to hide the “user@hostname” info when you’re logged in as yourself on your local machine.

### alanpeabody
[![alanpeabody](https://cloud.githubusercontent.com/assets/2618447/6316714/5190b8ba-ba00-11e4-8fa9-9f22160be9e4.png)](https://cloud.githubusercontent.com/assets/2618447/6316714/5190b8ba-ba00-11e4-8fa9-9f22160be9e4.png)


### amuse
[![amuse](https://cloud.githubusercontent.com/assets/2618447/6316861/70f3c4ce-ba03-11e4-88a5-0b423dd5a2ce.png)](https://cloud.githubusercontent.com/assets/2618447/6316861/70f3c4ce-ba03-11e4-88a5-0b423dd5a2ce.png)

Shown in the screenshot with tmux and the [powerline plugin](https://github.com/powerline/powerline) (you might need to install one of the [patched powerline fonts](https://github.com/powerline/fonts) for it to look the same).

### arrow
[![arrow](https://cloud.githubusercontent.com/assets/2618447/6316717/51a09e7e-ba00-11e4-8120-45ca128b9bf6.png)](https://cloud.githubusercontent.com/assets/2618447/6316717/51a09e7e-ba00-11e4-8120-45ca128b9bf6.png)

### aussiegeek
[![aussiegeek](https://cloud.githubusercontent.com/assets/2618447/6316719/51a34962-ba00-11e4-9577-882124c30b4e.png)](https://cloud.githubusercontent.com/assets/2618447/6316719/51a34962-ba00-11e4-9577-882124c30b4e.png)

### avit
[![avit](https://cloud.githubusercontent.com/assets/2618447/6316718/51a2fd9a-ba00-11e4-845a-24bed6ae9210.png)](https://cloud.githubusercontent.com/assets/2618447/6316718/51a2fd9a-ba00-11e4-845a-24bed6ae9210.png)

### awesomepanda
[![awesomepanda](https://cloud.githubusercontent.com/assets/760855/18191406/2cb2e21e-70f4-11e6-83f0-42096ff33cfd.png)](https://cloud.githubusercontent.com/assets/760855/18191406/2cb2e21e-70f4-11e6-83f0-42096ff33cfd.png)


### bira
[![bira](https://cloud.githubusercontent.com/assets/2618447/6316716/51a0708e-ba00-11e4-8664-11a804f2fe3f.png)](https://cloud.githubusercontent.com/assets/2618447/6316716/51a0708e-ba00-11e4-8664-11a804f2fe3f.png)

### blinks
[![blinks](https://cloud.githubusercontent.com/assets/2618447/6316715/519c8e56-ba00-11e4-9792-a4b3d1d3775a.png)](https://cloud.githubusercontent.com/assets/2618447/6316715/519c8e56-ba00-11e4-9792-a4b3d1d3775a.png)

Additional setup: Set up [Solarized](http://ethanschoonover.com/solarized).

### bureau
[![bureau](https://cloud.githubusercontent.com/assets/2618447/6316720/51a54ba4-ba00-11e4-82d2-f2af8cc18869.png)](https://cloud.githubusercontent.com/assets/2618447/6316720/51a54ba4-ba00-11e4-82d2-f2af8cc18869.png)

To use: In the right prompt you see git status and (if you use nvm) the Node.js version. (I’m using the [Solarized](http://ethanschoonover.com/solarized) color scheme in this screenshot.)

### candy
[![candy](https://cloud.githubusercontent.com/assets/2618447/6316863/70f5b87e-ba03-11e4-8ee5-65345537e0bf.png)](https://cloud.githubusercontent.com/assets/2618447/6316863/70f5b87e-ba03-11e4-8ee5-65345537e0bf.png)

### clean
[![clean](https://cloud.githubusercontent.com/assets/2618447/6316721/51af13a0-ba00-11e4-87ea-cf83f32010f0.png)](https://cloud.githubusercontent.com/assets/2618447/6316721/51af13a0-ba00-11e4-87ea-cf83f32010f0.png)

### cloud
[![cloud](https://cloud.githubusercontent.com/assets/2618447/6316723/51b24944-ba00-11e4-8dcb-cb09a198523e.png)](https://cloud.githubusercontent.com/assets/2618447/6316723/51b24944-ba00-11e4-8dcb-cb09a198523e.png)

### crunch
[![crunch](https://cloud.githubusercontent.com/assets/2618447/6316722/51b1f4b2-ba00-11e4-9ebf-1359aa272fbd.png)](https://cloud.githubusercontent.com/assets/2618447/6316722/51b1f4b2-ba00-11e4-9ebf-1359aa272fbd.png)

### cypher
[![cypher](https://cloud.githubusercontent.com/assets/2618447/6316864/70f5c09e-ba03-11e4-90c3-c539e09c6cc9.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316864/70f5c09e-ba03-11e4-90c3-c539e09c6cc9.jpg)

### dallas
[![dallas](https://cloud.githubusercontent.com/assets/2618447/6316725/51b39b28-ba00-11e4-942e-600c704a8180.png)](https://cloud.githubusercontent.com/assets/2618447/6316725/51b39b28-ba00-11e4-942e-600c704a8180.png)

### darkblood
[![darkblood](https://cloud.githubusercontent.com/assets/2618447/6316865/70fa9006-ba03-11e4-81c4-593d9ae34a9c.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316865/70fa9006-ba03-11e4-81c4-593d9ae34a9c.jpg)

### daveverwer
[![daveverwer](https://cloud.githubusercontent.com/assets/2618447/6317506/faa0ca2a-ba24-11e4-9c34-ffa83f0cca23.png)](https://cloud.githubusercontent.com/assets/2618447/6317506/faa0ca2a-ba24-11e4-9c34-ffa83f0cca23.png)

### dieter
[![dieter](https://cloud.githubusercontent.com/assets/2618447/6316724/51b2886e-ba00-11e4-805f-c622567608e3.png)](https://cloud.githubusercontent.com/assets/2618447/6316724/51b2886e-ba00-11e4-805f-c622567608e3.png)

Additional setup: Get this small [[fix|https://github.com/Dieterbe/oh-my-zsh/commit/7ca0afd6861fe0c9e6903a08f0e469746df627e0]] if you don’t have it yet. (Fix was [[pulled|https://github.com/robbyrussell/oh-my-zsh/commit/8294cf44d1d348fd1590ee28b5be8483fb012153]] into robbyrussell/oh-my-zsh on 2011-01-08.)

### dogenpunk
[![dogenpunk](https://cloud.githubusercontent.com/assets/2618447/6316727/51b8067c-ba00-11e4-8e59-722a79ec60c2.png)](https://cloud.githubusercontent.com/assets/2618447/6316727/51b8067c-ba00-11e4-8e59-722a79ec60c2.png)

### dpoggi
[![dpoggi](https://cloud.githubusercontent.com/assets/2618447/6316730/51bca236-ba00-11e4-810d-ab3e9365c56b.png)](https://cloud.githubusercontent.com/assets/2618447/6316730/51bca236-ba00-11e4-810d-ab3e9365c56b.png)

### eastwood
[![eastwood](https://cloud.githubusercontent.com/assets/2618447/6316728/51ba0026-ba00-11e4-9d83-435c3c4513cf.png)](https://cloud.githubusercontent.com/assets/2618447/6316728/51ba0026-ba00-11e4-9d83-435c3c4513cf.png)

### evan
*a skinny, topless prompt*

[![evan](https://cloud.githubusercontent.com/assets/2618447/6316867/70fc6e44-ba03-11e4-8537-9a77378e6c48.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316867/70fc6e44-ba03-11e4-8537-9a77378e6c48.jpg)

### fishy
The fish shell prompt with git support

[![fishy](https://cloud.githubusercontent.com/assets/1441704/6315377/3ee891ce-ba00-11e4-92cc-885bc3c96c6e.png)](https://cloud.githubusercontent.com/assets/1441704/6315377/3ee891ce-ba00-11e4-92cc-885bc3c96c6e.png)

### flazz
Has git and vi-command mode support (when enabled)

[![flazz](https://cloud.githubusercontent.com/assets/2618447/6316729/51bc9fac-ba00-11e4-9e4b-cb0612d5f440.png)](https://cloud.githubusercontent.com/assets/2618447/6316729/51bc9fac-ba00-11e4-9e4b-cb0612d5f440.png)

### frisk
[![frisk](https://cloud.githubusercontent.com/assets/2618447/6316732/51bdd21e-ba00-11e4-97ac-0fdda49fe3c2.png)](https://cloud.githubusercontent.com/assets/2618447/6316732/51bdd21e-ba00-11e4-97ac-0fdda49fe3c2.png)

### funky
it’s funky…
[![funky](https://cloud.githubusercontent.com/assets/1441704/6315381/55ccfdb2-ba00-11e4-9fd1-86623b5bba17.png)](https://cloud.githubusercontent.com/assets/1441704/6315381/55ccfdb2-ba00-11e4-9fd1-86623b5bba17.png)

### gallifrey
[![gallifrey](https://cloud.githubusercontent.com/assets/2618447/6316866/70fc3f8c-ba03-11e4-888a-baef9f609c56.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316866/70fc3f8c-ba03-11e4-888a-baef9f609c56.jpg)

### gallois
[![gallois](https://cloud.githubusercontent.com/assets/2618447/6316731/51bd3b88-ba00-11e4-9c58-e09a3965e0f0.png)](https://cloud.githubusercontent.com/assets/2618447/6316731/51bd3b88-ba00-11e4-9c58-e09a3965e0f0.png)

### garyblessington
[![garyblessington](https://cloud.githubusercontent.com/assets/2618447/6316868/7100520c-ba03-11e4-9357-07472942ad5e.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316868/7100520c-ba03-11e4-9357-07472942ad5e.jpg)

### gentoo
[![gentoo](https://cloud.githubusercontent.com/assets/2618447/6316733/51c0f390-ba00-11e4-876d-70a95b5d629b.png)](https://cloud.githubusercontent.com/assets/2618447/6316733/51c0f390-ba00-11e4-876d-70a95b5d629b.png)

### geoffgarside
[![geoffgarside](https://cloud.githubusercontent.com/assets/1441704/6315385/701d32e0-ba00-11e4-8c31-ab30a0fd6324.png)](https://cloud.githubusercontent.com/assets/1441704/6315385/701d32e0-ba00-11e4-8c31-ab30a0fd6324.png)

### gianu
[![gianu](https://cloud.githubusercontent.com/assets/2618447/6316736/51c6a6c8-ba00-11e4-8b5f-b45795d98907.png)](https://cloud.githubusercontent.com/assets/2618447/6316736/51c6a6c8-ba00-11e4-8b5f-b45795d98907.png)

### gnzh
[![gnzh](https://cloud.githubusercontent.com/assets/2618447/6316735/51c62b1c-ba00-11e4-8107-fb532db89c7d.png)](https://cloud.githubusercontent.com/assets/2618447/6316735/51c62b1c-ba00-11e4-8107-fb532db89c7d.png)

### Honukai
[![Honukai](https://cloud.githubusercontent.com/assets/34213/11912137/aa0d81be-a62f-11e5-90ab-bf9bfc7a56f0.png)](https://cloud.githubusercontent.com/assets/34213/11912137/aa0d81be-a62f-11e5-90ab-bf9bfc7a56f0.png)

Additional eye-candy in the **[source repo](https://github.com/oskarkrawczyk/honukai-iterm-zsh)**.

### imajes
[![imajes](https://cloud.githubusercontent.com/assets/2618447/6316870/710289f0-ba03-11e4-9482-25742645379d.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316870/710289f0-ba03-11e4-9482-25742645379d.jpg)

### jnrowe
[![jnrowe](https://cloud.githubusercontent.com/assets/2618447/6316737/51c7104a-ba00-11e4-9875-ca6652e45fb5.png)](https://cloud.githubusercontent.com/assets/2618447/6316737/51c7104a-ba00-11e4-9875-ca6652e45fb5.png)

### jreese
[![jreese](https://cloud.githubusercontent.com/assets/2618447/6316734/51c54d82-ba00-11e4-882e-695dd5570528.png)](https://cloud.githubusercontent.com/assets/2618447/6316734/51c54d82-ba00-11e4-882e-695dd5570528.png)

### jtriley
[![jtriley](https://cloud.githubusercontent.com/assets/2618447/6316738/51c836c8-ba00-11e4-87a9-667ccbcbbd30.png)](https://cloud.githubusercontent.com/assets/2618447/6316738/51c836c8-ba00-11e4-87a9-667ccbcbbd30.png)

### juanghurtado
[![juanghurtado](https://cloud.githubusercontent.com/assets/2618447/6316739/51cc2814-ba00-11e4-9d4a-1dca9961d906.png)](https://cloud.githubusercontent.com/assets/2618447/6316739/51cc2814-ba00-11e4-9d4a-1dca9961d906.png)

### junkfood

> Totally ripped off Dallas theme

[![junkfood](https://cloud.githubusercontent.com/assets/1441704/9643381/e9cc48b6-51c1-11e5-99ee-e8cfbbf60d99.png)](https://cloud.githubusercontent.com/assets/1441704/9643381/e9cc48b6-51c1-11e5-99ee-e8cfbbf60d99.png)

[+info](http://www.tylercipriani.com/2012/12/18/zsh-prompt-customization.html)

### kafeitu
[![kafeitu](https://cloud.githubusercontent.com/assets/2618447/6316741/51cec254-ba00-11e4-8433-a3c2524086c1.png)](https://cloud.githubusercontent.com/assets/2618447/6316741/51cec254-ba00-11e4-8433-a3c2524086c1.png)

### kardan
[![kardan](https://cloud.githubusercontent.com/assets/2618447/6316740/51ce9356-ba00-11e4-80c1-79e0b489cd32.png)](https://cloud.githubusercontent.com/assets/2618447/6316740/51ce9356-ba00-11e4-80c1-79e0b489cd32.png)

### kennethreitz
[![kennethreitz](https://cloud.githubusercontent.com/assets/2618447/6316742/51cfb3e4-ba00-11e4-8e8e-720bab641edd.png)](https://cloud.githubusercontent.com/assets/2618447/6316742/51cfb3e4-ba00-11e4-8e8e-720bab641edd.png)

### kolo
[![kolo](https://cloud.githubusercontent.com/assets/2618447/6316743/51d066ea-ba00-11e4-850c-6527b01d8ef5.png)](https://cloud.githubusercontent.com/assets/2618447/6316743/51d066ea-ba00-11e4-850c-6527b01d8ef5.png)

### kphoen
[![kphoen](https://cloud.githubusercontent.com/assets/2618447/6316871/7103ea8e-ba03-11e4-977d-255b34aabe53.png)](https://cloud.githubusercontent.com/assets/2618447/6316871/7103ea8e-ba03-11e4-977d-255b34aabe53.png)

### lambda
[![lambda](https://cloud.githubusercontent.com/assets/2618447/6316744/51d09ba6-ba00-11e4-9e41-e942ee626bae.png)](https://cloud.githubusercontent.com/assets/2618447/6316744/51d09ba6-ba00-11e4-9e41-e942ee626bae.png)

### linuxonly
[![linuxonly](https://cloud.githubusercontent.com/assets/2618447/6316745/51dab9ba-ba00-11e4-853b-7ea8ab5ced35.png)](https://cloud.githubusercontent.com/assets/2618447/6316745/51dab9ba-ba00-11e4-853b-7ea8ab5ced35.png)

(As the name states, this only works on linux.)

### lukerandall
[![lukerandall](https://cloud.githubusercontent.com/assets/2618447/6316747/51db7bca-ba00-11e4-8018-6838f2bec7da.png)](https://cloud.githubusercontent.com/assets/2618447/6316747/51db7bca-ba00-11e4-8018-6838f2bec7da.png)

### macovsky
[![macovsky](https://cloud.githubusercontent.com/assets/2618447/6316872/71047346-ba03-11e4-8a49-2d83c4437b81.png)](https://cloud.githubusercontent.com/assets/2618447/6316872/71047346-ba03-11e4-8a49-2d83c4437b81.png)

### maran
[![maran](https://cloud.githubusercontent.com/assets/1441704/6315389/7df9c496-ba00-11e4-8386-027d324255c4.png)](https://cloud.githubusercontent.com/assets/1441704/6315389/7df9c496-ba00-11e4-8386-027d324255c4.png)

### mh
[![mh](https://cloud.githubusercontent.com/assets/2618447/6316746/51db6d92-ba00-11e4-988c-6c89eb581c8c.png)](https://cloud.githubusercontent.com/assets/2618447/6316746/51db6d92-ba00-11e4-988c-6c89eb581c8c.png)

### michelebologna
[![michelebologna](https://cloud.githubusercontent.com/assets/530992/7785021/34c45cea-017d-11e5-964f-10f99d4a5d37.png)](https://cloud.githubusercontent.com/assets/530992/7785021/34c45cea-017d-11e5-964f-10f99d4a5d37.png)

### miloshadzic
[![miloshadzic](https://cloud.githubusercontent.com/assets/2618447/6316748/51dc1eae-ba00-11e4-843d-379183044762.png)](https://cloud.githubusercontent.com/assets/2618447/6316748/51dc1eae-ba00-11e4-843d-379183044762.png)

### minimal
[![minimal](https://cloud.githubusercontent.com/assets/2618447/6316749/51de4ad0-ba00-11e4-8b4e-42e7000bad53.png)](https://cloud.githubusercontent.com/assets/2618447/6316749/51de4ad0-ba00-11e4-8b4e-42e7000bad53.png)

### mortalscumbag
also tells you when logged in over ssh

[![mortalscumbag](https://cloud.githubusercontent.com/assets/2618447/6316750/51dee102-ba00-11e4-8ede-27627cd495f9.png)](https://cloud.githubusercontent.com/assets/2618447/6316750/51dee102-ba00-11e4-8ede-27627cd495f9.png)

### mrtazz
[![mrtazz](https://cloud.githubusercontent.com/assets/2618447/6316873/71057cc8-ba03-11e4-911a-53d085b1894e.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316873/71057cc8-ba03-11e4-911a-53d085b1894e.jpg)

### muse
[![muse](https://cloud.githubusercontent.com/assets/2618447/6316752/51e211a6-ba00-11e4-8f57-e82fcc4a453f.png)](https://cloud.githubusercontent.com/assets/2618447/6316752/51e211a6-ba00-11e4-8f57-e82fcc4a453f.png)

### nanotech
[![nanotech](https://cloud.githubusercontent.com/assets/2618447/6316751/51e187c2-ba00-11e4-8a7e-1a45e4df00bf.png)](https://cloud.githubusercontent.com/assets/2618447/6316751/51e187c2-ba00-11e4-8a7e-1a45e4df00bf.png)

### nebirhos
[![nebirhos](https://cloud.githubusercontent.com/assets/2618447/6316754/51e4a182-ba00-11e4-8cf1-65ff1511da34.png)](https://cloud.githubusercontent.com/assets/2618447/6316754/51e4a182-ba00-11e4-8cf1-65ff1511da34.png)

### nicoulaj
[![nicoulaj](https://cloud.githubusercontent.com/assets/2618447/6316755/51e4b0c8-ba00-11e4-85ef-3e7faeeb0e0b.png)](https://cloud.githubusercontent.com/assets/2618447/6316755/51e4b0c8-ba00-11e4-85ef-3e7faeeb0e0b.png)

### norm
[![norm](https://cloud.githubusercontent.com/assets/1441704/11986491/65c9c702-a9d0-11e5-8393-ce262988ab09.png)](https://cloud.githubusercontent.com/assets/1441704/11986491/65c9c702-a9d0-11e5-8393-ce262988ab09.png)

### philips
[![philips](https://cloud.githubusercontent.com/assets/2618447/6316874/710a1e22-ba03-11e4-91c4-30f195e3fa2f.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316874/710a1e22-ba03-11e4-91c4-30f195e3fa2f.jpg)

### pygmalion
[![pygmalion](https://cloud.githubusercontent.com/assets/2618447/6316756/51e859ee-ba00-11e4-8b58-2f086c491926.png)](https://cloud.githubusercontent.com/assets/2618447/6316756/51e859ee-ba00-11e4-8b58-2f086c491926.png)

(Shown with [Solarized Dark colorscheme](http://ethanschoonover.com/solarized).)

### risto
[![risto](https://cloud.githubusercontent.com/assets/1441704/6315405/18aa274c-ba01-11e4-8bb7-0ba9ca166974.png)](https://cloud.githubusercontent.com/assets/1441704/6315405/18aa274c-ba01-11e4-8bb7-0ba9ca166974.png)

### rixius
[![rixius](https://cloud.githubusercontent.com/assets/2618447/6316760/51efdeb2-ba00-11e4-8da6-a839f192a207.png)](https://cloud.githubusercontent.com/assets/2618447/6316760/51efdeb2-ba00-11e4-8da6-a839f192a207.png)

### rkj-repos
[![rkj-repos](https://cloud.githubusercontent.com/assets/2618447/6316757/51ee9e12-ba00-11e4-86d4-1d59a182f688.png)](https://cloud.githubusercontent.com/assets/2618447/6316757/51ee9e12-ba00-11e4-86d4-1d59a182f688.png)

[![rkj-repos-2](https://cloud.githubusercontent.com/assets/2618447/6316875/710b063e-ba03-11e4-9e22-ecb86da25f46.png)](https://cloud.githubusercontent.com/assets/2618447/6316875/710b063e-ba03-11e4-9e22-ecb86da25f46.png)

### sammy
[![sammy](https://cloud.githubusercontent.com/assets/2618447/6316759/51ef7a44-ba00-11e4-9c76-e9bb6e75f5ce.png)](https://cloud.githubusercontent.com/assets/2618447/6316759/51ef7a44-ba00-11e4-9c76-e9bb6e75f5ce.png)

### simple
[![simple](https://cloud.githubusercontent.com/assets/2618447/6316758/51ef3480-ba00-11e4-840c-a9ebec42f4b6.png)](https://cloud.githubusercontent.com/assets/2618447/6316758/51ef3480-ba00-11e4-840c-a9ebec42f4b6.png)

### smt
[![smt](https://cloud.githubusercontent.com/assets/2618447/6316761/51f0052c-ba00-11e4-990f-cdf7fc5610e6.png)](https://cloud.githubusercontent.com/assets/2618447/6316761/51f0052c-ba00-11e4-990f-cdf7fc5610e6.png)

### sorin
[![sorin](https://cloud.githubusercontent.com/assets/2618447/6316762/51f34624-ba00-11e4-948a-6ac65a49f8c5.png)](https://cloud.githubusercontent.com/assets/2618447/6316762/51f34624-ba00-11e4-948a-6ac65a49f8c5.png)

### sporty_256
![sporty_256](https://cloud.githubusercontent.com/assets/2618447/6316763/51f8f2e0-ba00-11e4-82fe-40c9a5a81569.png)

### steeef
[![steeef](https://cloud.githubusercontent.com/assets/2618447/6316764/51f98994-ba00-11e4-9083-ecec290a8dcb.png)](https://cloud.githubusercontent.com/assets/2618447/6316764/51f98994-ba00-11e4-9083-ecec290a8dcb.png)

### sunaku
exit status if nonzero, status & branch if git, `pwd` always
[![sunaku](https://cloud.githubusercontent.com/assets/1441704/6315408/4599c546-ba01-11e4-8ba0-591dc9433f7f.png)](https://cloud.githubusercontent.com/assets/1441704/6315408/4599c546-ba01-11e4-8ba0-591dc9433f7f.png)

### sunrise
Lightweight prompt with exit status and `git status` consistent mode line

[![sunrise](https://cloud.githubusercontent.com/assets/2618447/6316766/51fbf062-ba00-11e4-9b66-2b0da5a0dbbc.png)](https://cloud.githubusercontent.com/assets/2618447/6316766/51fbf062-ba00-11e4-9b66-2b0da5a0dbbc.png)

### superjarin
git status, git branch, and ruby, all in a no muss, no fuss prompt! Works with RVM, chruby, and rbenv (just activate the corresponding plugin).

[![superjarin](https://cloud.githubusercontent.com/assets/2618447/6316765/51fac93a-ba00-11e4-95bc-e2eea4e98c8b.png)](https://cloud.githubusercontent.com/assets/2618447/6316765/51fac93a-ba00-11e4-95bc-e2eea4e98c8b.png)

### suvash
username, host, directory, git branch and rvm gemset

[![suvash](https://cloud.githubusercontent.com/assets/2618447/6316877/710d06be-ba03-11e4-8942-d6d28c54ff74.png)](https://cloud.githubusercontent.com/assets/2618447/6316877/710d06be-ba03-11e4-8942-d6d28c54ff74.png)

### terminalparty
There is a party every day.

[![terminalparty](https://cloud.githubusercontent.com/assets/2618447/6316767/51fc28fc-ba00-11e4-9129-953048acce0a.png)](https://cloud.githubusercontent.com/assets/2618447/6316767/51fc28fc-ba00-11e4-9129-953048acce0a.png)

### theunraveler
Minimal, informative when it needs to be.
[![theunraveler](https://cloud.githubusercontent.com/assets/1441704/6315413/6d28ed9e-ba01-11e4-98ad-7ae9a713e95c.png)](https://cloud.githubusercontent.com/assets/1441704/6315413/6d28ed9e-ba01-11e4-98ad-7ae9a713e95c.png)

### tjkirch
Based on dst, plus a lightning bolt and return codes.

[![tjkirch](https://cloud.githubusercontent.com/assets/2618447/6316768/520565e8-ba00-11e4-98ad-4665f72882ac.png)](https://cloud.githubusercontent.com/assets/2618447/6316768/520565e8-ba00-11e4-98ad-4665f72882ac.png)

### tonotdo
[![tonotdo](https://cloud.githubusercontent.com/assets/2618447/6316878/710deab6-ba03-11e4-8897-52154d993ad8.jpg)](https://cloud.githubusercontent.com/assets/2618447/6316878/710deab6-ba03-11e4-8897-52154d993ad8.jpg)

### trapd00r
[![trapd00r](https://cloud.githubusercontent.com/assets/2618447/6316879/710ec8dc-ba03-11e4-923a-580d6682a3bf.png)](https://cloud.githubusercontent.com/assets/2618447/6316879/710ec8dc-ba03-11e4-923a-580d6682a3bf.png)

### wedisagree
[![wedisagree](https://cloud.githubusercontent.com/assets/2618447/6316769/5205cc54-ba00-11e4-9d2b-e7b632f74997.png)](https://cloud.githubusercontent.com/assets/2618447/6316769/5205cc54-ba00-11e4-9d2b-e7b632f74997.png)

Instructions to further customize the theme are available as comments in the theme file.

### wezm
[![wezm](https://cloud.githubusercontent.com/assets/1441704/6315419/915f6ca6-ba01-11e4-95b3-2c98114b5e5c.png)](https://cloud.githubusercontent.com/assets/1441704/6315419/915f6ca6-ba01-11e4-95b3-2c98114b5e5c.png)

### wuffers
[![wuffers](https://cloud.githubusercontent.com/assets/2618447/6316770/52071794-ba00-11e4-9122-c7194f5188f4.png)](https://cloud.githubusercontent.com/assets/2618447/6316770/52071794-ba00-11e4-9122-c7194f5188f4.png)

### xiong-chiamiov
[![xiong-chiamiov](https://cloud.githubusercontent.com/assets/1441704/6315428/ded1e6ee-ba01-11e4-8b9d-a67485476e9f.png)](https://cloud.githubusercontent.com/assets/1441704/6315428/ded1e6ee-ba01-11e4-8b9d-a67485476e9f.png)

### xiong-chiamiov-plus
[![xiong-chiamiov-plus](https://cloud.githubusercontent.com/assets/1441704/6315427/d02464d2-ba01-11e4-8546-9c8dc984be79.png)](https://cloud.githubusercontent.com/assets/1441704/6315427/d02464d2-ba01-11e4-8546-9c8dc984be79.png)

### ys
Clean, simple, compatible and meaningful.Tested on Linux, Unix and Windows under ANSI colors.
It is recommended to use with a dark background.

([more info](http://blog.ysmood.org/my-ys-terminal-theme/))

![ys-zsh-theme](https://cloud.githubusercontent.com/assets/1415488/13198621/f2c1320c-d848-11e5-8f22-7fac1baeec2f.jpg)


### zhann
[![zhann](https://cloud.githubusercontent.com/assets/2618447/6316771/520a5170-ba00-11e4-9561-78f0c76e996c.png)](https://cloud.githubusercontent.com/assets/2618447/6316771/520a5170-ba00-11e4-9561-78f0c76e996c.png)

## More themes
You can find more themes [here](https://github.com/robbyrussell/oh-my-zsh/wiki/External-themes).

##  (Don’t) Send us your theme! (for now)

We have enough themes for the time being. Please fork the project and add on in there, you can let people know how to grab it from there.

Or put it gist and list it in https://github.com/robbyrussell/oh-my-zsh/wiki/External-themes .

## Theme Description Format

The theme descriptions in this page should contain:
* The name of the theme
* A screenshot
  * (Preferably in PNG format, and hosted on a GitHub issue)
* Instructions for any configuration besides setting `ZSH_THEME` in `~/.zshrc`
  * For example, font installation, terminal color scheme configuration, or optional environment variables that affect the theme
* Any dependencies outside Oh My Zsh

We use manually-constructed screenshots because some of the themes require additional terminal configuration to look their best, and so the code in example shell sessions can showcase the theme's features. There is also a separate collection of automatically-generated screenshots linked [at the bottom of this page](#screenshots-of-each-theme).

###  Uploading screenshots to GitHub

We host all the screenshot images on GitHub itself, to avoid external dependencies on other hosting services or URLs that might break. We use issue attachments which will get them in to githubusercontent.com. (It's also possible to store image files in a GitHub wiki itself, but this requires you to have Contributor permissions for the repo whose Wiki you're editing. The issue-attachment method can be done by anybody.)

To upload an image to GitHub, just drag and drop it into the text area on an issue you're editing. You can use issue #3619 for this to avoid spamming people with notifications about new issues. The uploaded image will turn in to a link in Markdown format. Edit that to use the special `[![name](image-url)](image-url)` syntax to make the image link to itself, so people can open the image in a new tab to view it full size. (Images inside a wiki page may be displayed scaled down.)

For example:

```
    [![wezm](https://cloud.githubusercontent.com/assets/1441704/6315419/915f6ca6-ba01-11e4-95b3-2c98114b5e5c.png)](https://cloud.githubusercontent.com/assets/1441704/6315419/915f6ca6-ba01-11e4-95b3-2c98114b5e5c.png)
```

If you have several uploaded screenshot links you need to convert to that self-linked syntax, you can use this `sed` command on the markdown file to programmatically convert them.

    sed 's/^!\[[a-zA-Z0-9 -]*\](\([^)]*\)) *$/[&](\1)/'

##  Screenshots of Each Theme

[Screenshots of each theme](https://www.dropbox.com/sh/u532agyv1hyash1/LS9yNESRlQ?lst) (as of 2013-04-10), in OS X Terminal.app using Consolas 13pt and Pro color scheme, inside a folder containing both a git and a mercurial repo. Each screenshot displays the output of the `pwd` command. It has shortcomings (plugins for some themes might be missing), but it offers a convenient and uniform overview of each theme. Plugins used were battery, rvm, hg prompt, among others.