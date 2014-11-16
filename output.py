#!/usr/bin/python
import os
import datetime
import sys
import string
from math import *

#Taken from: http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])

def drawToCMD(inString):
    os.system("clear")
    (width, height) = getTerminalSize()
    list = string.split(inString, "=")
    equation = list[1]
    i=0

    while i < height+1:
            sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (i, width/2, "|"))
            sys.stdout.flush()
            i = i+1
    i=0
    while i< width+1:
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (height/2, i, "-"))
        sys.stdout.flush()
        i = i+1

    for x in range(width/2*-1,width/2):
        row = height/2-eval(equation)
        if row > 0 and row < height+1:
            sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (row, x+width/2, "X"))
            sys.stdout.flush()

    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (height, 0, "Press enter to exit"))
    sys.stdout.flush()
    close = raw_input()
    os.system("clear")

def writeToCMD(equation):
    list = string.split(equation, "=")
    print list[1], "="
    print eval(list[1])

def printError(location, message):
    #This function has been deprecated
    if location == "cmd":
        print message
    elif location == "std":
        print message, "print on gui"
    elif location == "graph":
        print message, "print on graph"

def logger(type, message, exception):
    filename = str(datetime.date.today())
    filename+=".log"
    logs = open(filename, "a")

    if(type == "exception"):
        logs.write("Time: %s. Error Type: %s.\tMessage: %s.\tException: %s\n" % (datetime.datetime.now().time(), type, message, exception))
    else:
        logs.write("%s.\t%s." % (type, message))
    logs.close()

logger("exception", "this needs to be logged", "Exception Business")
drawToCMD("y=-abs(x)")
