import os
import shutil
from symbol import del_stmt
import webbrowser

def ls():
    for file in os.listdir():
        if os.path.isfile(file):
            if file.startswith('.'):
                print('\033[1;30m' + file)
            else:
                print('\033[0m' + file)
        elif os.path.isdir(file):
            if file.startswith('.'):
                print('\033[1;30    m' + file)
            else:
                print('\033[1;34m' + file)
            
def blank():
    os.system('cmd /c "ssh novc@blank"')

def clear():
    os.system('cmd /c "cls"')

def repo():
    webbrowser.open('http://gitea.local:3000/novc/pynux')

def motd():
    print('Opening text editor for MOTD editing...')

    motd_file_in_etc = os.path.join('root', 'etc', 'custom_motd.txt')
    motd_file_in_lib = os.path.join('root', 'lib', 'custom_motd.txt')
    motd_file_in_tmp = os.path.join('root', 'tmp', 'custom_motd.txt')

    if os.path.exists(motd_file_in_etc):
        shutil.copy(motd_file_in_etc, motd_file_in_tmp)
    else:
        shutil.copy(motd_file_in_lib, motd_file_in_tmp)

    motd_file_before_edit_time = os.path.getmtime(motd_file_in_tmp)
    os.system(motd_file_in_tmp)
    motd_file_after_edit_time = os.path.getmtime(motd_file_in_tmp)
    
    if motd_file_after_edit_time > motd_file_before_edit_time:
        shutil.move(motd_file_in_tmp, motd_file_in_etc)
    else:
        os.remove(motd_file_in_tmp)
