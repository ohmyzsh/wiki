All the current themes can be found in the `themes/` directory in the oh-my-zsh distribution. [See list here.](http://github.com/robbyrussell/oh-my-zsh/tree/master/themes/)

In order to enable a theme, set `ZSH_THEME` to the name of the theme in your `~/.zshrc`, before sourcing Oh My Zsh; for example: `ZSH_THEME=robbyrussell`  
If you do not want any theme enabled, just set `ZSH_THEME` to blank: `ZSH_THEME=""`

Here is a collection of screenshots and descriptions of themes that have been contributed to Oh My Zsh. There are some missing from this page. If you want to add or edit descriptions, see the [format description](#theme-description-format) at the bottom of this page.

## The Themes

### robbyrussell
*the (default) that Robby uses* 

![](http://img.skitch.com/20091228-qcke3kuenp61cwcnwqcd724pr7.jpg)

------------------------------------

The rest of the themes, in alphabetical order:

### af-magic
![](http://i.imgur.com/il7uuoW.png)

### afowler
![](http://i.imgur.com/LEAtp.png)

### agnoster
([more info](https://gist.github.com/3712874))

![](http://i.imgur.com/xsUVuac.png)

(Shown with [Solarized Dark colorscheme](http://ethanschoonover.com/solarized) and [patched Menlo 14pt](https://gist.github.com/1595572) in [iTerm 2](http://www.iterm2.com/))

Additional setup:

- Install one of the [patched fonts from Vim-Powerline](https://github.com/Lokaltog/powerline-fonts) or [patch your own](https://powerline.readthedocs.org/en/latest/fontpatching.html#font-patching) for the special characters.
- *Optionally* set `DEFAULT_USER` in `~/.zshrc` to your regular username to hide the “user@hostname” info when you’re logged in as yourself on your local machine.

### alanpeabody
![alanpeabody](https://cloud.githubusercontent.com/assets/2618447/6316714/5190b8ba-ba00-11e4-8fa9-9f22160be9e4.png)


### amuse
![](https://github-camo.global.ssl.fastly.net/dbe28e6d07f700a96149a36fe48ff9c065aae14f/687474703a2f2f64687275766173616761722e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031332f30332f416d7573652e706e67)

To use: You might need to install one of the [patched powerline fonts](https://github.com/Lokaltog/powerline-fonts) for it to look the same.

### arrow
![arrow](https://cloud.githubusercontent.com/assets/2618447/6316717/51a09e7e-ba00-11e4-8120-45ca128b9bf6.png)

### aussiegeek
![aussiegeek](https://cloud.githubusercontent.com/assets/2618447/6316719/51a34962-ba00-11e4-9577-882124c30b4e.png)

### avit
![avit](https://cloud.githubusercontent.com/assets/2618447/6316718/51a2fd9a-ba00-11e4-845a-24bed6ae9210.png)

### bira
![bira](https://cloud.githubusercontent.com/assets/2618447/6316716/51a0708e-ba00-11e4-8664-11a804f2fe3f.png)

### blinks
![blinks](https://cloud.githubusercontent.com/assets/2618447/6316715/519c8e56-ba00-11e4-9792-a4b3d1d3775a.png)

Additional setup: Set up [Solarized](http://ethanschoonover.com/solarized).

### bureau
![bureau](https://cloud.githubusercontent.com/assets/2618447/6316720/51a54ba4-ba00-11e4-82d2-f2af8cc18869.png)

To use: In the right prompt you see git status and (if you use nvm) the Node.js version. (I’m using the [Solarized](http://ethanschoonover.com/solarized) color scheme in this screenshot.)

### candy
![](http://i.imgur.com/gDbxsff.png)

### clean
![clean](https://cloud.githubusercontent.com/assets/2618447/6316721/51af13a0-ba00-11e4-87ea-cf83f32010f0.png)

### cloud
![cloud](https://cloud.githubusercontent.com/assets/2618447/6316723/51b24944-ba00-11e4-8dcb-cb09a198523e.png)

### crunch
![crunch](https://cloud.githubusercontent.com/assets/2618447/6316722/51b1f4b2-ba00-11e4-9ebf-1359aa272fbd.png)

### cypher
![](http://img.skitch.com/20091228-r19yxykxhdxkkqqp6687w5pgf4.jpg)

### dallas
![dallas](https://cloud.githubusercontent.com/assets/2618447/6316725/51b39b28-ba00-11e4-942e-600c704a8180.png)

### darkblood
![](http://img.skitch.com/20091228-811f9n5j1gxb2bjk5bh5f32ds3.jpg)

### daveverwer
![daveverwer](https://cloud.githubusercontent.com/assets/2618447/6316726/51b3fc8a-ba00-11e4-8378-a18d1be9cee3.png)

### dieter
![dieter](https://cloud.githubusercontent.com/assets/2618447/6316724/51b2886e-ba00-11e4-805f-c622567608e3.png)

Additional setup: Get this small [[fix|https://github.com/Dieterbe/oh-my-zsh/commit/7ca0afd6861fe0c9e6903a08f0e469746df627e0]] if you don’t have it yet. (Fix was [[pulled|https://github.com/robbyrussell/oh-my-zsh/commit/8294cf44d1d348fd1590ee28b5be8483fb012153]] into robbyrussell/oh-my-zsh on 2011-01-08.)

### dogenpunk
![dogenpunk](https://cloud.githubusercontent.com/assets/2618447/6316727/51b8067c-ba00-11e4-8e59-722a79ec60c2.png)

### dpoggi
![dpoggi](https://cloud.githubusercontent.com/assets/2618447/6316730/51bca236-ba00-11e4-810d-ab3e9365c56b.png)

### eastwood
![eastwood](https://cloud.githubusercontent.com/assets/2618447/6316728/51ba0026-ba00-11e4-9d83-435c3c4513cf.png)

### evan
*a skinny, topless prompt*

![](http://img.skitch.com/20091228-nems77ig6wkayf7w3daysd7jif.jpg)

### fishy
The fish shell prompt with git support

![fishy](https://cloud.githubusercontent.com/assets/1441704/6315377/3ee891ce-ba00-11e4-92cc-885bc3c96c6e.png)

### flazz
Has git and vi-command mode support (when enabled)
![flazz](https://cloud.githubusercontent.com/assets/2618447/6316729/51bc9fac-ba00-11e4-9e4b-cb0612d5f440.png)

### frisk
![frisk](https://cloud.githubusercontent.com/assets/2618447/6316732/51bdd21e-ba00-11e4-97ac-0fdda49fe3c2.png)

### funky
it’s funky…
![funky](https://cloud.githubusercontent.com/assets/1441704/6315381/55ccfdb2-ba00-11e4-9fd1-86623b5bba17.png)

### gallifrey
![](http://img.skitch.com/20091113-qqtd3j8xinysujg5ugrsbr7x1y.jpg)

### gallois
![gallois](https://cloud.githubusercontent.com/assets/2618447/6316731/51bd3b88-ba00-11e4-9c58-e09a3965e0f0.png)

### garyblessington
![](http://img.skitch.com/20091228-b5psxcshiq9f3iqgremchrwxxr.jpg)

### gentoo
![gentoo](https://cloud.githubusercontent.com/assets/2618447/6316733/51c0f390-ba00-11e4-876d-70a95b5d629b.png)

### geoffgarside
![geoffgarside](https://cloud.githubusercontent.com/assets/1441704/6315385/701d32e0-ba00-11e4-8c31-ab30a0fd6324.png)

### gianu
![gianu](https://cloud.githubusercontent.com/assets/2618447/6316736/51c6a6c8-ba00-11e4-8b5f-b45795d98907.png)

### gnzh
![gnzh](https://cloud.githubusercontent.com/assets/2618447/6316735/51c62b1c-ba00-11e4-8107-fb532db89c7d.png)

### imajes
![](http://img.skitch.com/20091228-kq8qwqpsqdyh7jyeyuxmyptkma.jpg)

### jnrowe
![jnrowe](https://cloud.githubusercontent.com/assets/2618447/6316737/51c7104a-ba00-11e4-9875-ca6652e45fb5.png)

### jreese
![jreese](https://cloud.githubusercontent.com/assets/2618447/6316734/51c54d82-ba00-11e4-882e-695dd5570528.png)

### jtriley
![jtriley](https://cloud.githubusercontent.com/assets/2618447/6316738/51c836c8-ba00-11e4-87a9-667ccbcbbd30.png)

### juanghurtado
![juanghurtado](https://cloud.githubusercontent.com/assets/2618447/6316739/51cc2814-ba00-11e4-9d4a-1dca9961d906.png)

### junkfood
([more info](http://www.tylercipriani.com/2012/12/18/zsh-prompt-customization.html))

![](http://i.imgur.com/3bgU1UW.png)

### kafeitu
![kafeitu](https://cloud.githubusercontent.com/assets/2618447/6316741/51cec254-ba00-11e4-8433-a3c2524086c1.png)

### kardan
![kardan](https://cloud.githubusercontent.com/assets/2618447/6316740/51ce9356-ba00-11e4-80c1-79e0b489cd32.png)

### kennethreitz
![kennethreitz](https://cloud.githubusercontent.com/assets/2618447/6316742/51cfb3e4-ba00-11e4-8e8e-720bab641edd.png)

### kolo
![kolo](https://cloud.githubusercontent.com/assets/2618447/6316743/51d066ea-ba00-11e4-850c-6527b01d8ef5.png)

### kphoen
![](http://i.imgur.com/hIE3v.png.)

### lambda
![lambda](https://cloud.githubusercontent.com/assets/2618447/6316744/51d09ba6-ba00-11e4-9e41-e942ee626bae.png)

### linuxonly
![linuxonly](https://cloud.githubusercontent.com/assets/2618447/6316745/51dab9ba-ba00-11e4-853b-7ea8ab5ced35.png)

(As the name states, this only works on linux.)

### lukerandall
![lukerandall](https://cloud.githubusercontent.com/assets/2618447/6316747/51db7bca-ba00-11e4-8018-6838f2bec7da.png)

### macovsky
![](http://i.imgur.com/fsedfuT.png)

### maran
![maran](https://cloud.githubusercontent.com/assets/1441704/6315389/7df9c496-ba00-11e4-8386-027d324255c4.png)

### mh
![mh](https://cloud.githubusercontent.com/assets/2618447/6316746/51db6d92-ba00-11e4-988c-6c89eb581c8c.png)

### miloshadzic
![miloshadzic](https://cloud.githubusercontent.com/assets/2618447/6316748/51dc1eae-ba00-11e4-843d-379183044762.png)

### minimal
![minimal](https://cloud.githubusercontent.com/assets/2618447/6316749/51de4ad0-ba00-11e4-8b4e-42e7000bad53.png)

### mortalscumbag
also tells you when logged in over ssh

![mortalscumbag](https://cloud.githubusercontent.com/assets/2618447/6316750/51dee102-ba00-11e4-8ede-27627cd495f9.png)

### mrtazz
![](http://farm5.static.flickr.com/4101/4910363151_f8170b691d.jpg)

### muse
![muse](https://cloud.githubusercontent.com/assets/2618447/6316752/51e211a6-ba00-11e4-8f57-e82fcc4a453f.png)

### nanotech
![nanotech](https://cloud.githubusercontent.com/assets/2618447/6316751/51e187c2-ba00-11e4-8a7e-1a45e4df00bf.png)

### nebirhos
![nebirhos](https://cloud.githubusercontent.com/assets/2618447/6316754/51e4a182-ba00-11e4-8cf1-65ff1511da34.png)

### nicoulaj
![nicoulaj](https://cloud.githubusercontent.com/assets/2618447/6316755/51e4b0c8-ba00-11e4-85ef-3e7faeeb0e0b.png)

### norm
![norm](https://cloud.githubusercontent.com/assets/2618447/6316753/51e440c0-ba00-11e4-87ed-400fe2b0dd39.png)

### philips
![](http://farm5.static.flickr.com/4124/5065882407_11d06f4e45.jpg)

### pygmalion
![pygmalion](https://cloud.githubusercontent.com/assets/2618447/6316756/51e859ee-ba00-11e4-8b58-2f086c491926.png)

(Shown with [Solarized Dark colorscheme](http://ethanschoonover.com/solarized).)

### risto
![risto](https://cloud.githubusercontent.com/assets/1441704/6315405/18aa274c-ba01-11e4-8bb7-0ba9ca166974.png)

### rixius
![rixius](https://cloud.githubusercontent.com/assets/2618447/6316760/51efdeb2-ba00-11e4-8da6-a839f192a207.png)

### rkj-repos
![rkj-repos](https://cloud.githubusercontent.com/assets/2618447/6316757/51ee9e12-ba00-11e4-86d4-1d59a182f688.png)

![](http://i.imgur.com/vWJuk.png)

### sammy
![sammy](https://cloud.githubusercontent.com/assets/2618447/6316759/51ef7a44-ba00-11e4-9c76-e9bb6e75f5ce.png)

### simple
![simple](https://cloud.githubusercontent.com/assets/2618447/6316758/51ef3480-ba00-11e4-840c-a9ebec42f4b6.png)

### smt
![smt](https://cloud.githubusercontent.com/assets/2618447/6316761/51f0052c-ba00-11e4-990f-cdf7fc5610e6.png)

### sorin
![sorin](https://cloud.githubusercontent.com/assets/2618447/6316762/51f34624-ba00-11e4-948a-6ac65a49f8c5.png)

### sporty_256
![sporty_256](https://cloud.githubusercontent.com/assets/2618447/6316763/51f8f2e0-ba00-11e4-82fe-40c9a5a81569.png)

### steeef
![steeef](https://cloud.githubusercontent.com/assets/2618447/6316764/51f98994-ba00-11e4-9083-ecec290a8dcb.png)

### sunaku
exit status if nonzero, status & branch if git, `pwd` always
![sunaku](https://cloud.githubusercontent.com/assets/1441704/6315408/4599c546-ba01-11e4-8ba0-591dc9433f7f.png)

### sunrise
Lightweight prompt with exit status and `git status` consistent mode line

![sunrise](https://cloud.githubusercontent.com/assets/2618447/6316766/51fbf062-ba00-11e4-9b66-2b0da5a0dbbc.png)

### superjarin
git status, git branch, and RVM, all in a no muss, no fuss prompt! Screenshot uses 14 pt Inconsolata (antialiased).

![superjarin](https://cloud.githubusercontent.com/assets/2618447/6316765/51fac93a-ba00-11e4-95bc-e2eea4e98c8b.png)

### suvash
username, host, directory, git branch and rvm gemset

![](http://i.imgur.com/MyJ9kxn.png)

### terminalparty
There is a party every day.

![terminalparty](https://cloud.githubusercontent.com/assets/2618447/6316767/51fc28fc-ba00-11e4-9129-953048acce0a.png)

### theunraveler
Minimal, informative when it needs to be.
![theunraveler](https://cloud.githubusercontent.com/assets/1441704/6315413/6d28ed9e-ba01-11e4-98ad-7ae9a713e95c.png)

### tjkirch
Based on dst, plus a lightning bolt and return codes.

![tjkirch](https://cloud.githubusercontent.com/assets/2618447/6316768/520565e8-ba00-11e4-98ad-4665f72882ac.png)

### tonotdo
![](http://img.skitch.com/20091228-1mm8nuyik55iych3mpn1qjm4a7.jpg)

### trapd00r
![](http://i.imgur.com/qLSIo3x.png)

### wedisagree
![wedisagree](https://cloud.githubusercontent.com/assets/2618447/6316769/5205cc54-ba00-11e4-9d2b-e7b632f74997.png)

Instructions to further customize the theme are available as comments in the theme file.

### wezm
![wezm](https://cloud.githubusercontent.com/assets/1441704/6315419/915f6ca6-ba01-11e4-95b3-2c98114b5e5c.png)

### wuffers
![wuffers](https://cloud.githubusercontent.com/assets/2618447/6316770/52071794-ba00-11e4-9122-c7194f5188f4.png)

### xiong-chiamiov
![xiong-chiamiov](https://cloud.githubusercontent.com/assets/1441704/6315428/ded1e6ee-ba01-11e4-8b9d-a67485476e9f.png)

### xiong-chiamiov-plus
![xiong-chiamiov-plus](https://cloud.githubusercontent.com/assets/1441704/6315427/d02464d2-ba01-11e4-8546-9c8dc984be79.png)

### ys
Clean, simple, compatible and meaningful. ([more info](http://blog.ysmood.org/my-ys-terminal-theme/))

[![How it looks like on Mac.](https://f.cloud.github.com/assets/1415488/252783/25a3055e-8bb4-11e2-9b9f-95c0d6f870fb.jpg)](https://f.cloud.github.com/assets/1415488/252783/25a3055e-8bb4-11e2-9b9f-95c0d6f870fb.jpg)

### zhann
![zhann](https://cloud.githubusercontent.com/assets/2618447/6316771/520a5170-ba00-11e4-9561-78f0c76e996c.png)

## Theme Description Format

The theme descriptions should contain:
* The name of the theme.
* A screenshot. Preferably in PNG format.
* Instructions for any configuration besides setting `ZSH_THEME` in `~/.zshrc`. For example, font installation, terminal colorscheme configuration, or optional environment variables that affect the theme.
* Any dependencies outside Oh My Zsh.

We use manually-constructed screenshots because some of the themes require additional terminal configuration to look their best, and so the code in example shell sessions can showcase the theme's features. There is also a separate collection of automatically-generated screenshots linked [at the bottom of this page](#screenshots-of-each-theme).

##  (Don’t) Send us your theme! (for now)

We have enough themes for the time being. Please fork the project and add on in there, you can let people know how to grab it from there.

##  Screenshots of Each Theme

[Screenshots of each theme](https://www.dropbox.com/sh/u532agyv1hyash1/LS9yNESRlQ?lst) (as of 2013-04-10), in OS X Terminal.app using Consolas 13pt and Pro color scheme, inside a folder containing both a git and a mercurial repo. Each screenshot displays the output of the `pwd` command. It has shortcomings (plugins for some themes might be missing), but it offers a convenient and uniform overview of each theme. Plugins used were battery, rvm, hg prompt, among others.