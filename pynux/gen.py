import os
import shutil
import pickle
import webbrowser
from pathlib import Path
from pynux.col import *
from pynux.log import *

def ls():
    for file in os.listdir():
        if os.path.isfile(file):
            if file.startswith('.'):
                print('\033[1;30m' + file)
            else:
                print('\033[0m' + file)
        elif os.path.isdir(file):
            if file.startswith('.'):
                print('\033[1;30m' + file)
            else:
                print('\033[1;34m' + file)
            
def blank():
    os.system('cmd /c "ssh novc@blank"')

def clear():
    os.system('cmd /c "cls"')

def repo():
    webbrowser.open('http://gitea.local:3000/novc/pynux')

def motd():
    print('Opening text editor for MOTD editing...')

    motd_file_in_etc = os.path.join('root', 'etc', 'custom_motd.txt')
    motd_file_in_lib = os.path.join('root', 'lib', 'custom_motd.txt')
    motd_file_in_tmp = os.path.join('root', 'tmp', 'custom_motd.txt')

    if os.path.exists(motd_file_in_etc):
        shutil.copy(motd_file_in_etc, motd_file_in_tmp)
    else:
        shutil.copy(motd_file_in_lib, motd_file_in_tmp)

    motd_file_before_edit_time = os.path.getmtime(motd_file_in_tmp)
    os.system(motd_file_in_tmp)
    motd_file_after_edit_time = os.path.getmtime(motd_file_in_tmp)

    if motd_file_after_edit_time > motd_file_before_edit_time:
        shutil.move(motd_file_in_tmp, motd_file_in_etc)
    else:
        os.remove(motd_file_in_tmp)

def toggle_welcome_msg(cmd_args_lst, show_welcome_msg):
    if len(cmd_args_lst) == 0:
        print('Arguments for ' + blue('wlctoggle') + ':\n\ton - Turn on the welcome message.\n\toff - Turn off the welcome message.')
        return

    if len(cmd_args_lst) == 1:
        if cmd_args_lst[0] == 'on':
            print('The welcome message will be ' + green('visible') + '.')
            show_welcome_msg = True
            # pickle save
            with open('root/etc/options.txt', 'wb') as f:
                pickle.dump(show_welcome_msg, f, protocol=2)
        elif cmd_args_lst[0] == 'off':
            print('The welcome message will ' + red('no longer') + ' be visible.')
            show_welcome_msg = False
            # pickle save
            with open('root/etc/options.txt', 'wb') as f:
                pickle.dump(show_welcome_msg, f, protocol=2)
        else:
            err('One or more argument(s) couldn\'t be processed.', '2')
    else:
        err('Expected only 1 argument (on/off)', '3')

def welcome_msg_status(show_welcome_msg):
    if show_welcome_msg == True:
        print(green('on'))
    elif show_welcome_msg == False:
        print(red('off'))
    else:
        print(magenta('The options file (root/etc/options) is corrupt, please submit an issue if it doesn\'t exist\nalready on the GitHub repo issues page via the repo command.'))

def cat(cmd_args_lst):
    if len(cmd_args_lst) == 0:
        print('Arguments for ' + blue('cat') + ':\n\t[path] - Path for the file you are concatenating.')
        return

    if len(cmd_args_lst) == 1:
        catdir_arg = cmd_args_lst[0]
        if os.path.exists(catdir_arg):
            catdir = open(catdir_arg, 'r')
            print(catdir.read())
        else:
            err('The path you entered is invalid.', '2')
    else:
        err('Expected only 1 argument ([path])', '3')

def prd():
    running_path = os.path.dirname(os.path.abspath('main.py'))
    print(running_path)
    return running_path

def pwd(current_path):
    print(current_path)

def cd(cmd_args_lst, current_path):
    if len(cmd_args_lst) == 0:
        print('Arguments for ' + blue('cd') + ':\n\t[directory] - Directory you are going into.')
        return current_path

    if len(cmd_args_lst) == 1:
        cddir_arg = cmd_args_lst[0]
        if os.path.exists(cddir_arg):
            # ! CD NEEDS TO BE FIXED HERE
            if len(str(Path(os.getcwd()).resolve())) < len(current_path):
                print('@@@ cant go more out')
            else:
                os.chdir(cddir_arg)
                current_path = str(Path(os.getcwd()).resolve())
        else:
            err('The directory you entered is invalid.', '2')
    else:
        err('Expected only 1 argument ([directory])', '3')
    
    return current_path