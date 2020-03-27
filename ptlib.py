#! /usr/bin/env python3

ver='1.0'

import os
import subprocess

def shell(command):
    cmd=command.split(' ')
    obj=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out=obj.communicate()[0].decode('ascii')
    return out

def cat(file):
    if os.path.isfile(file) == True:
        obj=open(file, 'r')
        return obj.read()
    else:
        print('PTLIB-cat path is not existent or is not a file')

def echotofile(file, txt):
    with open(file, 'w') as f:
        f.write(txt)
        f.close

class html:
    def a(txt):
        out='<a>'+txt+'</a>'
        return out

    def p(txt):
        out='<p>'+txt+'</p>'
        return out


    def center(txt):
        out='<center>'+txt+'</center>'
        return out

    def html(txt):
        out='<html>'+txt+'</html>'
        return out

    def title(txt):
        out='<title>'+txt+'</title>'
        return out

    def header(txt):
        out='<header>'+txt+'</header>'
        return out

    def body(txt):
        out='<body>'+txt+'</body>'
        return out

    def css(file):
        out='<link rel=\'stylesheet\' href=\''+file+'\'>'
        return out

# print(cat('ptlib.py'))
