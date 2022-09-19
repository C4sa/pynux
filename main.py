# imports
from time import *

# variables
username = 'user'
hostname = 'host'

prefix_user = '\033[1;36m┌──(\033[1;34m' + username + '@' + hostname + '\033[1;36m)-[\033[1;32m~\033[1;36m]\n└─\033[1;34m$ \033[0m'

# methods
def err(err_msg, err_id):
    print('\033[1;31mError: \033[0m' + err_msg + '\033[1;30m[PN' + err_id + ']\n')

# main
while True:
    cmd = input(prefix_user)
    cmd_args_lst = cmd.split()
    if len(cmd_args_lst) == 0:
        # blank command, or space
        continue
    else:
        # one-word commands
        cmd = cmd_args_lst[0]
        if cmd == 'instr':
            print('instructions will go here soon™')

        else:
            err('Command \"' + cmd + '\" is not defined. \033[1;30m', '1')

    args = cmd_args_lst[1:]
    for arg in args:
        if arg == 'shutdown' and cmd == 'sys':
            print('\033[1;31mExiting Pynux...')
            sleep(0.4)
            exit()
        else:
            err('The following argument couldn\'t be processed: ' + arg)