from pynux.log import *
from pynux.col import *

# pynux/sudoer (cmd)

def sudoer_mng(cmd_args_lst, current_user, sudoers_list):
    if len(cmd_args_lst) == 0:
        print('Arguments for ' + blue('sudoer') + ':\n\tadd [\'self\'/username] - Add an user to the sudoers list.\n\tremove [\'self\'/username] - Remove an user from the sudoers list.')
        return

    if cmd_args_lst[0] == 'add':
        if len(cmd_args_lst) == 2:
            if cmd_args_lst[1] == 'self' or cmd_args_lst[1] == current_user:
                sudoers_list.append(current_user)
                suc('added ' + current_user + ' to the sudoers list.')
        else:
            err('Expected 2 arguments (add/remove [username])', '3')
    else:
        err('One or more argument(s) couldn\'t be processed.', '2')