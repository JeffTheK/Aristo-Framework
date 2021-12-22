#!/usr/bin/python

import color

def encode():
    Str = inputT+'' + color.UNDERLINE + 'String to encode>' + color.END)
    Str = Str.encode('base64','strict')
    print(""+G+"Encoded: " + Str)
def decode():
    Str = inputT+'' + color.UNDERLINE + 'String to decode>' + color.END)
    Str = Str.decode('base64','strict')
    print(""+G+"Decoded String: " + Str)