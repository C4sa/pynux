from pynux.col import *

def err(err_msg, err_id):
    print(red('Error: ') + err_msg + gray(' [PN' + err_id + ']\n'))

def suc(suc_msg):
    print(green('Successfully ') + suc_msg)