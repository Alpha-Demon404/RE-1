
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : decs_23.pyc
# Bytecode Version : 2.7
# Time : Tue Aug 11 16:43:54 2020
#---------------------------------------

import os
import sys
import time
print '\x1b[30;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\xe2\x95\x91\x1b[30;1m\xe2\x9e\xa2 Author : RANDIOLOY                       \x1b[30;1m\xe2\x95\x91\n\xe2\x95\x91\x1b[30;1m\xe2\x9e\xa3 YouTube: RANDI OLOYY                     \x1b[30;1m\xe2\x95\x91\n\xe2\x95\x91\x1b[30;1m\xe2\x9e\xa2 Github : https://github.com/RANDIOLOY    \x1b[30;1m\xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[0;37m'

try:
    a = raw_input('\x1b[30;1m\xe2\x94\x8c\xe2\x94\x80[\x1b[30;1m Input File\x1b[30;1m\n\x1b[30;1m\xe2\x94\x94\xe2\x94\x80[\x1b[31;1mRandiSr\x1b[0;37m]> \x1b[33;1m')
    b = open(a).read().replace('exec', 'x=')
    c = open('xyz.py', 'w')
    if 'marshal' in b:
        c.write('from sys import stdout\nfrom uncompyle6.main import decompile\n' + b + '\ndecompile(2.7, x, stdout)')
        c.close()
    elif 'marshal' not in b:
        c.write(b + '\nprint (x)')
        c.close()
    d = a.replace('.py', '-decompiled.py')
    os.system('python2 xyz.py > ' + d)
    e = open(d).read()
    f = open(d, 'w')
    f.write('# Decompiled By RandiSr\n# Github : https://github.com/RANDIOLOY\n' + e)
    f.close()
    os.system('rm -rf xyz.py')
    print '\x1b[31;1m[\x1b[0;37m+\x1b[31;1m]\x1b[0;37m File saved as\x1b[32;1m %s' % d
except IndexError:
    print '\n\x1b[31;1m[\x1b[0;37m!\x1b[31;1m] \x1b[0;37mthere is an error'
    sys.exit()
except KeyboardInterrupt:
    print '\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m ctrl+c detected'
    print '\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m trying to exit'
    time.sleep(3)
    sys.exit()
except EOFError:
    print '\n\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m ctrl+d detected'
    print '\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m trying to exit'
    time.sleep(3)
    sys.exit()
except:
    print '\n\x1b[31;1m[\x1b[0;37m!\x1b[31;1m] \x1b[0;37m Exit'
    sys.exit()
