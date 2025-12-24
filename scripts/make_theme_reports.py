#!/usr/bin/env python3
# The script goes through all the .zsh-thmes files and makes a dedicated file. with the theme's report.
# It is very possible that the scripts gets false positives.
import os
import re
import tempfile
import argparse
# all ways to find things.
WAYS_TO_FIND={
    "username": re.compile(r'%n'),
    "hostname":re.compile(r'%m|%M|HOST|host_repr'),
    "time":re.compile(r'%D|%T|%t|%\*'),
    "last_failure":re.compile(r'%\?|%\(\?|%\?\)|RETVAL|RETURN|FAIL|ret_status'),
    "pwd_num":re.compile(r'%([0-9]+)~'),
    "pwd_basename":re.compile(r'%c'),
    "pwd_short":re.compile(r'%~'),
    "pwd_full":re.compile(r'%/|%d'),
    "extra":{
        "git":re.compile(r'git_prompt_info|git_prompt_status|git_prompt|vcs_branch|\bgit\b'),
        "hg":re.compile(r'hg_prompt_info|\bhg\b|hg_prompt'),
        "svn": re.compile(r'svn_prompt_info|\bsvn\b'),
        "vcs_info":re.compile(r'vcs|VCS'),
        "virtualenv":re.compile(r'VIRTUAL_ENV|virtualenv_prompt_info|virtualenv|CONDA_DEFAULT_ENV|conda_prompt'),
        "ruby": re.compile(r'ruby_prompt_info|\bRVM\b|ruby_prompt|rvm'),
        "fortune_commandlinefu":re.compile(r'fortune|commandlinefu|wget -qO-|curl -fsL'),
        "history_number":re.compile(r'%!|%h'),
        "root_indicator":re.compile(r'%#|%\(\!|UID\s*-eq\s*0|\$EUID\ \-ne\ 0|\"\$USERNAME"\ \=\ \"root\"|_LIBERTY\s*=.*#|\%\(\#\,'),
        "aws":re.compile(r'AWS_PROFILE'),
        "terraform":re.compile(r'tf_prompt_info|terraform'),
        "vi-mode":re.compile(r'vi_mode_prompt_info|vi_mode'),
        "kube":re.compile(r'kube_ps1|kube_prompt|kubernetes'),
        'conda': re.compile(r'conda_prompt|CONDA_DEFAULT_ENV'),
        'rvm': re.compile(r'ZSH_THEME_RVM_PROMPT_OPTIONS|rvm|RVM'),
        'nodejs': re.compile(r'node_version_prompt|node_prompt_info|nvm'),
        'battery': re.compile(r'battery_prompt_info|battery'),
        'ssh_indicator': re.compile(r'ssh|SSH'),
        'bzr': re.compile(r'bzr_prompt_info|\bbzr\b'),
        'command_duration': re.compile(r'duration|cmd_timestamp'),
        'jenv': re.compile(r'jenv_prompt_info|jenv'),
        'customizable': re.compile(r'MLH'),
    }
}
class themes:
    def __init__(self, name, conf,cfpath,repath):
        """this class contains all info about a theme

        Args:
            name (str): theme's name
            conf (str): the contents of a theme's config file
            path (str): the path of the config file
        """
        self.name = name
        self.config = conf
        self.cfpath = cfpath
        self.repath = repath
        self.capabilities = {
            "basic":{
                "username":bool,
                "hostname":bool,
                "time":bool,
                "last_failure":bool,
                "pwd":str,
            },
            "extras":[]
        }
        self.fill_data()
    def fill_data(self):
        """gathers all the info on the theme
        """
        self.capabilities["basic"]["username"]=True if WAYS_TO_FIND["username"].search(self.config) else False
        self.capabilities["basic"]["hostname"]=True if WAYS_TO_FIND["hostname"].search(self.config) else False
        self.capabilities["basic"]["time"]=True if WAYS_TO_FIND["time"].search(self.config) else False
        self.capabilities["basic"]["last_failure"]=True if WAYS_TO_FIND["last_failure"].search(self.config) else False
        #pwd determination:
        pwd_style='shortened path'
        n=WAYS_TO_FIND["pwd_num"].search(self.config)
        if n:
            pwd_style=f'shortened path ({n.group(1)} folders)'
        elif WAYS_TO_FIND["pwd_basename"].search(self.config):
            pwd_style='basename (current directory name)'
        elif WAYS_TO_FIND["pwd_short"].search(self.config):
            pwd_style='shortened path'
        elif WAYS_TO_FIND["pwd_full"].search(self.config):
            pwd_style='full path'
        self.capabilities["basic"]["pwd"]=pwd_style
        #checking for the extras
        #? theory: I will loop through the keys in WAYS_TO_FIND['extra'] in order to have the name of the tool
        #?          then i will verify if it applies. If it does, then I will add the key to the capabilities extra list.
        for key in WAYS_TO_FIND['extra'].keys():
            if WAYS_TO_FIND['extra'][key].search(self.config):
                self.capabilities['extras'].append(key)
            else:continue #sounded harder in my head.
    def generate_report(self) -> str:
        """Generating the report, returns a string formated as a markdown list.
        """
        extras=', '.join(self.capabilities["extras"]) if self.capabilities["extras"] else ''
        lines=[
            f"# Report for {self.name}",
            f"- Name: {self.name}",
            f"- Shows username: {self.capabilities["basic"]["username"]}",
            f"- Shows hostname: {self.capabilities["basic"]["hostname"]}",
            f"- Shows time/date: {self.capabilities["basic"]["time"]}",
            f"- Shows last command failure: {self.capabilities["basic"]["last_failure"]}",
            f"- PWD style: {self.capabilities["basic"]["pwd"]}",
            f"- Other info: {extras}"
        ]
        report='\n'.join(lines)+'\n'
        return report

def main():
    p = argparse.ArgumentParser(description='Generate reports/summary.md and reports/summary.csv')
    p.add_argument('--reports-dir',required=True , help='Directory containing report files')
    p.add_argument('--theme-dirs',required=True,help="Where theme files are. Multiple allowed",action="append")
    p.add_argument('--alias',help="anykind of name change to be made. (wezm+ -> wezmplus) Multiple allowed",metavar="'b4:after'",action="append")
    args = p.parse_args()
    #making the aliases into something usefull.
    alias={}
    if args.alias:
        for i in args.alias:
            x=i.split(":", 2) #split the alias in a temp var
            alias[x[0]]=x[1] #making the before be the key and the after be the value
    #making documentation is harder then i thought ngl, i am not a programmer lol
    themeDict: list[type[themes]]
    themeDict=[] 
    #Looping through all theme directory
    for theme_dir in args.theme_dirs:
        #? step 1 - verify if dir actually exists
        if not os.path.isdir(theme_dir):
            continue
        #? step 2 - loop through all files in dir
        for theme in sorted(os.listdir(theme_dir)):
            if not theme.endswith('.zsh-theme'): #verification that the file is actually a theme file
                continue
            #now i need to obtain the important data...
            themeName=theme[:-10] #remove the file extension from name
            if alias:
                if themeName in alias.keys: themeName=alias[themeName]
            themePath=os.path.join(theme_dir,theme)
            rePath=os.path.join(args.reports_dir,themeName)
            try:
                with open(themePath,'r',errors='ignore') as fh:
                    themeConfig=fh.read()
            except Exception as e:
                print("Failed to read config file: "+themePath)
                print(e)
                continue
            #Now adding to the theme dict the class for the theme.
            themeDict.append(themes(themeName,themeConfig,themePath,rePath))
    for th in themeDict:
        th.fill_data()
        report=th.generate_report()
        try:
            with open(th.repath, "w") as f:
                f.write(report)
        except Exception as e:
            print("failed write")
            exit(1)


if __name__ == '__main__':
    main()
