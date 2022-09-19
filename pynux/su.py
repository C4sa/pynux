from pynux.log import *

# pynux/sudoer (cmd)

# ! NEEDS FIXES & TWEAKS
def sudoer_mng(cmd_args_lst, current_user, sudoers_list):
    if len(cmd_args_lst) > 0:            
        for arg in cmd_args_lst:
            if arg == 'add':
                if arg == 'self' or arg == current_user:
                    sudoers_list.append(current_user)
                    print('Successfully added \033[1;34m' + current_user + ' \033[0mto the sudoers list.')
            else:
                err('The argument(s) ' + arg + ' couldn\'t be processed.', '2')
    else:
        print('Arguments for \033[1;34msudoer\033[0m:\n\tadd [\'self\' / username] - Add an user to the sudoers list.')