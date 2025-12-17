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
    "pwdre_pwd_num":re.compile(r'%([0-9]+)~'),
    "re_pwd_c":re.compile(r'%c'),
    "re_pwd_tilde":re.compile(r'%~'),
    "ex_git":re.compile(r'git_prompt_info|git_prompt_status|git_prompt|vcs_branch|\bgit\b'),
    "ex_hg":re.compile(r'hg_prompt_info|\bhg\b|hg_prompt'),
    "ex_svn": re.compile(r'svn_prompt_info|\bsvn\b'),
    "ex_vcs_info":re.compile(r'vcs|VCS'),
    "ex_virtualenv":re.compile(r'VIRTUAL_ENV|virtualenv_prompt_info|virtualenv|CONDA_DEFAULT_ENV|conda_prompt'),
    "ex_ruby": re.compile(r'ruby_prompt_info|\bRVM\b|ruby_prompt|rvm'),
    "ex_fortune_commandlinefu":re.compile(r'fortune|commandlinefu|wget -qO-|curl -fsL'),
    "ex_history_number":re.compile(r'%!|%h'),
    "ex_root_indicator":re.compile(r'%#|%\(\!|UID\s*-eq\s*0|\$EUID\ \-ne\ 0|\"\$USERNAME"\ \=\ \"root\"|_LIBERTY\s*=.*#|\%\(\#\,'),
    "ex_aws":re.compile(r'AWS_PROFILE'),
    "ex_terraform":re.compile(r'tf_prompt_info|terraform'),
    "ex_vi-mode":re.compile(r'vi_mode_prompt_info|vi_mode'),
    "ex_kube":re.compile(r'kube_ps1|kube_prompt|kubernetes'),
    'ex_conda': re.compile(r'conda_prompt|CONDA_DEFAULT_ENV'),
    'ex_rvm': re.compile(r'ZSH_THEME_RVM_PROMPT_OPTIONS|rvm|RVM'),
    'ex_nodejs': re.compile(r'node_version_prompt|node_prompt_info|nvm'),
    'ex_battery': re.compile(r'battery_prompt_info|battery'),
    'ex_ssh_indicator': re.compile(r'ssh|SSH'),
    'ex_bzr': re.compile(r'bzr_prompt_info|\bbzr\b'),
    'ex_command_duration': re.compile(r'duration|cmd_timestamp'),
    'ex_jenv': re.compile(r'jenv_prompt_info|jenv'),
    'ex_customizable': re.compile(r'MLH'),

}
# re_username = re.compile(r'%n')
# re_hostname = re.compile(r'%m|%M|HOST|host_repr')
# re_time = re.compile(r'%D|%T|%t|%\*')
# re_last_failure = re.compile(r'%\?|%\(\?|%\?\)|RETVAL|RETURN|FAIL|ret_status')
# re_pwd_num = re.compile(r'%([0-9]+)~')
# re_pwd_c = re.compile(r'%c')
# re_pwd_tilde = re.compile(r'%~')

# extras = [
#     ('git', re.compile(r'git_prompt_info|git_prompt_status|git_prompt|vcs_branch|\bgit\b')),
#     ('hg', re.compile(r'hg_prompt_info|\bhg\b|hg_prompt')),
#     ('svn', re.compile(r'svn_prompt_info|\bsvn\b')),
#     ('vcs_info', re.compile(r'vcs|VCS')),
#     ('virtualenv', re.compile(r'VIRTUAL_ENV|virtualenv_prompt_info|virtualenv|CONDA_DEFAULT_ENV|conda_prompt')),
#     ('ruby', re.compile(r'ruby_prompt_info|\bRVM\b|ruby_prompt|rvm')),
#     ('fortune/commandlinefu', re.compile(r'fortune|commandlinefu|wget -qO-|curl -fsL')),
#     ('history number', re.compile(r'%!|%h')),
#     ('root indicator', re.compile(r'%#|%\(\!|UID\s*-eq\s*0|\$EUID\ \-ne\ 0|\"\$USERNAME"\ \=\ \"root\"|_LIBERTY\s*=.*#|\%\(\#\,')),
#     ('aws', re.compile(r'AWS_PROFILE')),
#     ('terraform', re.compile(r'tf_prompt_info|terraform')),
#     ('vi-mode', re.compile(r'vi_mode_prompt_info|vi_mode')),
#     ('kube', re.compile(r'kube_ps1|kube_prompt|kubernetes')),
#     ('conda', re.compile(r'conda_prompt|CONDA_DEFAULT_ENV')),
#     ('rvm', re.compile(r'ZSH_THEME_RVM_PROMPT_OPTIONS|rvm|RVM')),
#     ('nodejs', re.compile(r'node_version_prompt|node_prompt_info|nvm')),
#     ('battery', re.compile(r'battery_prompt_info|battery')),
#     ('ssh indicator', re.compile(r'ssh|SSH')),
#     ('bzr', re.compile(r'bzr_prompt_info|\bbzr\b')),
#     ('command duration', re.compile(r'duration|cmd_timestamp')),
#     ('jenv', re.compile(r'jenv_prompt_info|jenv')),
#     ('customizable', re.compile(r'MLH')),
# ]
for td in TH_DIRS:
    if not os.path.isdir(td):
        continue
    for fname in sorted(os.listdir(td)): #loop through all files
        if not fname.endswith('.zsh-theme'): #verification that the file is actually a theme file
            continue
        base=fname[:-10] #remove the file extension from name
        path=os.path.join(td,fname)
        try:
            with open(path,'r',errors='ignore') as fh:
                txt=fh.read()
        except Exception as e:
            failed.append((path,str(e)))
            continue
        processed+=1
        shows_username='yes' if re_username.search(txt) else 'no'
        shows_hostname='yes' if re_hostname.search(txt) else 'no'
        shows_time='yes' if re_time.search(txt) else 'no'
        shows_last='yes' if re_last_failure.search(txt) else 'no'
        #PWD checking - if there are multiple paths displayed, it might have false positives
        pwd_style='shortened path'
        m=re_pwd_num.search(txt)
        if m:
            pwd_style=f'shortened path ({m.group(1)} folders)'
        elif re_pwd_c.search(txt):
            pwd_style='basename (current directory name)'
        elif re_pwd_tilde.search(txt):
            pwd_style='shortened path'
        else:
            if re.search(r'%/|%d',txt):
                pwd_style='full path'
        #checking for the extras
        other=[]
        for name,rx in extras:
            if rx.search(txt):
                other.append(name)
        if re.search(r'git_prompt_info|git_prompt_status|git_prompt|vcs_branch|\bgit\b',txt) and 'git' not in other:
            other.insert(0,'git') #No clue what this is since git is in extras but don't feel like checking and testing
        #generating the array for the report
        other_info=', '.join(other) if other else '' # make the array into a string
        lines=['```yaml']
        lines.append(f'  Theme: {base}')
        lines.append(f'  Shows username: {shows_username}')
        lines.append(f'  Shows hostname: {shows_hostname}')
        lines.append(f'  Shows time/date: {shows_time}')
        lines.append(f'  Shows last command failure: {shows_last}')
        lines.append(f'  PWD style: {pwd_style}')
        if other_info:
            lines.append(f'  Other info: {other_info}')
        lines.append('```')
        content='\n'.join(lines)+'\n' #make into a string
        #making report
        try:
            report_name=find_report_name(base) #get the correct file name
            outpath=os.path.join(R_DIR,report_name) #get the file path
            fd, tmp = tempfile.mkstemp(dir=R_DIR) #make a temp file
            with os.fdopen(fd,'w',encoding='utf-8') as f: #add text to temp file
                f.write(content)
                f.flush(); os.fsync(f.fileno())
            os.replace(tmp, outpath) #make temp file into perm file
            changed.append(report_name)
        except Exception as e:
            failed.append((outpath,str(e)))

class themes:
    
    def __init__(self, name, conf,):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)


def main():
    p = argparse.ArgumentParser(description='Generate reports/summary.md and reports/summary.csv')
    p.add_argument('--reports-dir',required=True , help='Directory containing report files')
    p.add_argument('--theme-dir',required=True,help="Where theme files are. Multiple allowed",action="append")
    p.add_argument('--alias',help="anykind of name change to be made. (wezm+ -> wezmplus) Multiple allowed",metavar="'b4:after'",action="append")
    args = p.parse_args()

    #making the aliases into something usefull.
    alias={}
    for i in args.alias:
        x=i.split(":", 2) #split the alias in a temp var
        alias[x[0]]=x[1] #making the before be the key and the after be the value
    #making documentation is harder then i thought ngl, i am not a programmer lol

if __name__ == '__main__':
    main()
    quit()



reports = set(os.listdir(R_DIR)) if os.path.isdir(R_DIR) else set()



changed=[]
processed=0
failed=[]

def find_report_name(base):
    if base in reports:
        return base
    alt = base.replace('+','plus') #was worried that a + in a file name messed something up.
    if alt in reports:
        return alt
    if base.startswith('xiong-'): #omg i made a small mistake in creating files and it copilot punishes me like that...
        cand='w'+base
        if cand in reports:
            return cand
    low = base.lower()
    if low in reports:
        return low
    return alt


print('SAFE WRITE DONE. themes processed:', processed, 'reports updated:', len(changed))
if failed:
    print('FAILED:')
    for p,e in failed:
        print(p, e)
if changed:
    print('\nUPDATED REPORTS:')
    for r in sorted(set(changed)):
        print(r)
