import urllib
import color
from color import *

def web():
    try:
        web = raw_input(''+G+'' + color.UNDERLINE + 'Website>' + color.END)
    except IOError:
        print(''+G+'' + color.UNDERLINE + '[!] Host is in wrong format - e.g. http://example.com' + color.END)
        response = urllib.urlopen(web)
        print('RESPONSE:', response)
        print('URL     :', response.geturl())

        headers = response.info()
        print('DATE    :', headers['date'])
        print('HEADERS :')
        print('---------')
        print(headers)

        data = response.read()
        print('LENGTH  :', len(data))
        print('---------')
