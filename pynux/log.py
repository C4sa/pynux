from pynux.col import *
from win10toast import ToastNotifier

notif = ToastNotifier()

err_title = 'Pynux'
err_desc = 'Pynux ran into an error while running. Please review if you made a typo. Error code: '
icon_path = 'root/lib/icon.ico'

def err(err_msg, err_id):
    print(red('Error: ') + err_msg + gray(' [PN' + err_id + ']\n'))
    notif.show_toast(err_title, err_desc + err_id, icon_path=icon_path, duration=0)

def suc(suc_msg):
    print(green('Successfully ') + suc_msg)