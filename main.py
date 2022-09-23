# imports
from pynux import *
import webbrowser
import pickle
import getpass

# variables
username = 'user'
hostname = 'host'

current_user = username
current_path = '~'

win_user = getpass.getuser()
win_home_drive = os.getenv('HOMEDRIVE')
win_home_path = os.getenv('HOMEPATH')

default_path = win_home_drive + win_home_path
current_path = default_path

prefix_user = cyan('┌──(') + blue(username + '@' + hostname) + cyan(') - [') + green(current_path) + cyan(']') + cyan('\n└─') + blue('$ ')

sudoers = []

show_welcome_msg = True

# load options using pickle
with open('root/etc/options.txt', 'rb') as f:
    show_welcome_msg = pickle.load(f)

# motd
welcome_file = open('root/lib/welcome')
welcome_text = welcome_file.read()

if os.path.exists('root/etc/custom_motd.txt'):
    custom_motd_file = open('root/etc/custom_motd.txt')
else:
    custom_motd_file = open('root/lib/custom_motd.txt')

custom_motd_text = custom_motd_file.read()

if show_welcome_msg == True:
    print(welcome_text + '\n\n' + custom_motd_text + '\n')
else:
    print(custom_motd_text + '\n')

# main
while True:
    if current_path == default_path:
        display_path = '~'
    else:
        display_path = current_path
        #display_path = display_path.replace(default_path, '')

    prefix_user = cyan('┌──(') + blue(username + '@' + hostname) + cyan(') - [') + green(display_path) + cyan(']') + cyan('\n└─') + blue('$ ')

    cmd = input(prefix_user)
    cmd_args_lst = cmd.split()

    if len(cmd_args_lst) == 0:
        # blank command, or space
        continue
    else:
        cmd = cmd_args_lst[0]
        if cmd == 'instr':
            # TODO: instructions / help
            print('instructions will go here soon™');

        elif cmd == 'blank':
            blank()

        elif cmd == 'clear' or cmd == 'cls':
            clear()

        elif cmd == 'ls':
            ls()

        elif cmd == 'repo':
            repo()

        elif cmd == 'motd':
            motd()

        elif cmd == 'sudoer':
            sudoer_mng(cmd_args_lst[1:], current_user, sudoers)

        elif cmd == 'sys':
            sys_handler(cmd_args_lst[1:])

        elif cmd == 'wlctoggle':
            toggle_welcome_msg(cmd_args_lst[1:], show_welcome_msg)

        elif cmd == 'wlcstatus':
            welcome_msg_status(show_welcome_msg)

        elif cmd == 'cat':
            cat(cmd_args_lst[1:])

        elif cmd == 'prd':
            prd()

        elif cmd == 'pwd':
            pwd(current_path)

        elif cmd == 'cd':
            current_path = cd(cmd_args_lst[1:], current_path)

        elif cmd == 'aaa':
            aaa()
            
        else:
            err('Command \"' + cmd + '\" is not defined.', '1')