#!/usr/bin/python

import color
from color import *

def encode1():
    Str = inputT+'' + color.UNDERLINE + 'String to encode>' + color.END)
    Str = Str.encode('hex','strict')
    print(""+G+"Encoded: " + Str)
def decode1():
    Str = inputT+'' + color.UNDERLINE + 'String to decode>' + color.END)
    Str = Str.decode('hex','strict')
    print(""+G+"Decoded String: " + Str)
