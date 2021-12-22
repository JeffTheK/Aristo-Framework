import urllib.request
import color
from color import *

def siteexists():
    try:
        site = input(T+'' + color.UNDERLINE + 'Site>' + color.END)
        urllib2.urlopen(site)
    except urllib2.HTTPError as e:
        print(''+R+'Error:' + color.END)
        print(e.code)
    except urllib2.URLError as e:
        print(''+R+'Error:' + color.END)
        print(e.args)
    else:
        print(''+G+'[*] Page Exists!' + color.END)