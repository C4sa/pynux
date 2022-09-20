# imports
from pynux import *
import webbrowser

# variables
username = 'user'
hostname = 'host'

current_user = username

prefix_user = '\033[1;36m┌──(\033[1;34m' + username + '@' + hostname + '\033[1;36m)-[\033[1;32m~\033[1;36m]\n└─\033[1;34m$ \033[0m'

sudoers = []

# motd
welcome_file = open('root/lib/welcome')
welcome_text = welcome_file.read()

if os.path.exists('root/etc/custom_motd.txt'):
    custom_motd_file = open('root/etc/custom_motd.txt')
else:
    custom_motd_file = open('root/lib/custom_motd.txt')

custom_motd_text = custom_motd_file.read()
print(welcome_text + '\n\n' + custom_motd_text + '\n')

# main
while True: 
    cmd = input(prefix_user)
    cmd_args_lst = cmd.split()
    if len(cmd_args_lst) == 0:
        # blank command, or space
        continue
    else:
        cmd = cmd_args_lst[0]
        if cmd == 'instr':
            print('instructions will go here soon™')

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

        elif cmd == 'dbg':
            cyan('@@@ debug')

        elif cmd == 'sudoer':
            sudoer_mng(cmd_args_lst[1:], current_user, sudoers)

        elif cmd == 'sys':
            sys_handler(cmd_args_lst[1:])

        else:
            err('Command \"' + cmd + '\" is not defined.', '1')