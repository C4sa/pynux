from time import *
from pynux.log import *

# pynux/sys_handler (cmd)
def sys_handler(cmd_args_lst):
    if len(cmd_args_lst) > 0:            
        for arg in cmd_args_lst:
            if arg == 'shutdown':
                print('Sending \033[1;31mshutdown signal \033[0mto Pynux...')
                sleep(0.4)
                print('Response accepted, terminating...')
                exit()
            else:
                err('The argument(s) ' + arg + ' couldn\'t be processed.', '2')
    else:
        print('Arguments for \033[1;34msys\033[0m:\n\tshutdown - System shutdown.')