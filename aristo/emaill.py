import os
import sys
import color
from color import *

def spoofemail():
     fromm = raw_input(''+T+'' + color.UNDERLINE + 'From name>' + color.END)
     emaill = raw_input(''+T+'' + color.UNDERLINE + 'From email>' + color.END)
     too = raw_input(''+T+'' + color.UNDERLINE + 'To email>' + color.END)
     subject = raw_input(''+T+'' + color.UNDERLINE + 'Subject>' + color.END)
     isp = raw_input(''+T+'' + color.UNDERLINE + 'Your isp>' + color.END)
     print(C + "Type your message here, and when your done, press Ctrl-d." + W)
     os.system('sendEmail -f "' + fromm + '<' + emaill + '>" -t ' + too + ' -u "' + subject + '" -s ' + isp)