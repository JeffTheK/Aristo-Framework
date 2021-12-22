import os
import sys
import color
from color import *

def spoofemail():
     fromm = input + color.UNDERLINE + 'From name>' + color.END)
     emaill = input + color.UNDERLINE + 'From email>' + color.END)
     too = input + color.UNDERLINE + 'To email>' + color.END)
     subject = input + color.UNDERLINE + 'Subject>' + color.END)
     isp = input + color.UNDERLINE + 'Your isp>' + color.END)
     print(C + "Type your message here, and when your done, press Ctrl-d." + W)
     os.system('sendEmail -f "' + fromm + '<' + emaill + '>" -t ' + too + ' -u "' + subject + '" -s ' + isp)