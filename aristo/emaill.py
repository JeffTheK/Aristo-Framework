import os
import sys
import color
from color import *

def spoofemail():
     fromm = input(''+T+'' + color.UNDERLINE + 'From name>' + color.END)
     emaill = input(''+T+'' + color.UNDERLINE + 'From email>' + color.END)
     too = input(''+T+'' + color.UNDERLINE + 'To email>' + color.END)
     subject = input(''+T+'' + color.UNDERLINE + 'Subject>' + color.END)
     isp = input(''+T+'' + color.UNDERLINE + 'Your isp>' + color.END)
     print(C + "Type your message here, and when your done, press Ctrl-d." + W)
     os.system('sendEmail -f "' + fromm + '<' + emaill + '>" -t ' + too + ' -u "' + subject + '" -s ' + isp)