from pynux.col import *
from pynux.log import *
import pickle

def uname(cmd_args_lst, username, hostname):
    if len(cmd_args_lst) == 0:
        print('Arguments for ' + blue('uname') + ':\n[username] - Set the default username.')
        return

    elif len(cmd_args_lst) == 1:
        username = cmd_args_lst[0]
        suc('set the default username to ' + username + '.')

        with open('root/etc/user.txt', 'wb') as f:
                pickle.dump([username, hostname], f, protocol=2)

        return username

    else:
        err('One or more argument(s) couldn\'t be processed.', '2')

def hname(cmd_args_lst, hostname, username):
    if len(cmd_args_lst) == 0:
        print('Arguments for ' + blue('hname') + ':\n[hostname] - Set the default hostname.')
        return

    elif len(cmd_args_lst) == 1:
        hostname = cmd_args_lst[0]
        suc('set the default hostname to ' + hostname + '.')

        with open('root/etc/user.txt', 'wb') as f:
                pickle.dump([username, hostname], f, protocol=2)

        return hostname

    else:
        err('One or more argument(s) couldn\'t be processed.', '2')