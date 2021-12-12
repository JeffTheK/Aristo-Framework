import requests
import color
from color import *

def xss():
    fname = "payloads.txt"
    with open(fname) as f:
        content = f.readlines()
    payloads = [x.strip() for x in content]
    print(T + "Works best if there is a query at the end. eg. http://example.com?search=" + W)
    url = raw_input(''+T+'' + color.UNDERLINE + 'Full URL> ' + color.END)
    vuln = []
    for payload in payloads:
        payload = payload
        xss_url = url+payload
        r = requests.get(xss_url)
        if payload.lower() in r.text.lower():
            print(G + "[+] Vulnerable: " + W + payload)
            if(payload not in vuln):
                vuln.append(payload)
        else:
            print(R + "[!] Not vulnerable!" + W)

    print("--------------------\n" + G + "Available Payloads:" + W)
    print('\n'.join(vuln))


