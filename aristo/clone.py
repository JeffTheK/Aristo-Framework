import urllib.request
import sys
import io
import color
from color import *

def clone():
    print (''+T+'Remember to put https:// in front of the website!')
    hey = inputT+'' + color.UNDERLINE + 'Website>' + color.END)
    response = urllib2.urlopen(hey)
    page_source = response.read()

    with io.FileIO("websitesource.html", "w") as file:
        file.write(page_source)
    print (''+G+'[*] Finished!')