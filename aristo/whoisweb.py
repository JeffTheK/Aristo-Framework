import pythonwhois  # i'm using this http://cryto.net/pythonwhois
import color
from color import *

def whoisweb():
    print(''+R+'Example - example.com')
    h = raw_input(''+T+'' + color.UNDERLINE + 'Website>' + color.END)
    domains = [h]
    for dom in domains:
        details = pythonwhois.get_whois(dom)
        print(details['contacts']['registrant'] )