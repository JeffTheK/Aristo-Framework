import requests
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
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


