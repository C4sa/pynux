import os
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