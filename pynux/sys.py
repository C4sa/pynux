from time import *
import pyautogui
from pynux.log import *

# pynux/sys_handler (cmd)
def sys_handler(cmd_args_lst):
    if len(cmd_args_lst) > 0:            
        for arg in cmd_args_lst:
            if arg == 'sd':
                if len(cmd_args_lst) == 1:
                    print('Sending \033[1;31mshutdown signal \033[0mto Pynux...')
                    sleep(0.4)
                    print('Response accepted, terminating...')
                    exit()
                elif cmd_args_lst[1] == '-q':
                    print('Executing ' + red('quick shutdown') + '...')
                    exit()
                elif cmd_args_lst[1] == '-f':
                    exec(open('pynux/altf4up.pyw'))
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('f4')                    
            else:
                err('The argument(s) ' + arg + ' couldn\'t be processed.', '2')
    else:
        print('Arguments for \033[1;34msys\033[0m:\n\tsd - System shutdown.\n\t\t-q - Quick shutdown.\n\t\t-f - Forcibly close the terminal (useful for devs).')