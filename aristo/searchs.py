from googlesearch import search
import color
from color import *

def googleSearch():
    lol = raw_input(color.UNDERLINE + ""+T+"Query>" + color.END)
    for url in search(lol, tld='com', lang='es', stop=50):
        print(""+G+"Site: "+W+"" + url)
