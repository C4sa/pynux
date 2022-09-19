# imports
from pynux import *
import os

# variables
username = 'user'
hostname = 'host'

current_user = username

prefix_user = '\033[1;36m┌──(\033[1;34m' + username + '@' + hostname + '\033[1;36m)-[\033[1;32m~\033[1;36m]\n└─\033[1;34m$ \033[0m'

sudoers = []

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

        if cmd == 'blank':
            blank()

        if cmd == 'clear' or cmd == 'cls':
            clear()

        elif cmd == 'ls':
            ls()

        elif cmd == 'sudoer':
            sudoer_mng(cmd_args_lst, current_user, sudoers)

        elif cmd == 'sys':
            sys_handler(cmd_args_lst[1:])

        else:
            err('Command \"' + cmd + '\" is not defined. \033[1;30m', '1')