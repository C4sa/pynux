def gray(str):
    return col(str, 30)

def red(str):
    return col(str, 31)

def green(str):
    return col(str, 32)

def yellow(str):
    return col(str, 33)
    
def blue(str):
    return col(str, 34)

def magenta(str):
    return col(str, 35)

def cyan(str):
    return col(str, 36)

def col(msg, color):
    return '\033[1;' + str(color) + 'm' + msg + '\033[0m'