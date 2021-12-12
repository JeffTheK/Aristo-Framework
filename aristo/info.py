import os, io, platform, sys, socket
from time import sleep
from urllib.request import urlopen
import color
from color import *

mac_address = os.popen("cat /sys/class/net/eth0/address").read()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
localaddr = s.getsockname()[0] # local subnet
ipaddr = urlopen('http://ip.42.pl/raw').read()
def_gw_device = os.popen("route | grep '^default' | grep -o '[^ ]*$'").read()

def info():
    print(""+W+"+--------------------------+")
    print("|"+C+" Mac Address: " + mac_address + ""+W+"+--------------------------+")
    print("|"+R+" Local address: " + localaddr)
    print(""+W+"+--------------------------+")
    print("|"+G+" IP: " + ipaddr)
    print(""+W+"+--------------------------+")
    print("|"+T+" Operating System: " + platform.system())
    print(""+W+"+--------------------------+")
    print("|"+P+" Name: " + platform.node())
    print(""+W+"+--------------------------+")
    print("|"+O+" Interface: " + def_gw_device +W+"+--------------------------+")
