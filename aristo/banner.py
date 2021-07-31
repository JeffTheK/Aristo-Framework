# coding: utf-8
#!/usr/bin/env python
from random import *
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
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
def banner():
    header = color.RED + """
 █████╗ ██████╗ ██╗███████╗████████╗ ██████╗ 
██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔═══██╗
███████║██████╔╝██║███████╗   ██║   ██║   ██║
██╔══██║██╔══██╗██║╚════██║   ██║   ██║   ██║
██║  ██║██║  ██║██║███████║   ██║   ╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝    ╚═════╝
"""


    oblique = color.PURPLE + """
 █████  ██████  ██ ███████ ████████  ██████  
██   ██ ██   ██ ██ ██         ██    ██    ██ 
███████ ██████  ██ ███████    ██    ██    ██ 
██   ██ ██   ██ ██      ██    ██    ██    ██ 
██   ██ ██   ██ ██ ███████    ██     ██████  
"""

    modular = color.YELLOW + """
     _    ____  ___ ____ _____ ___  
    / \  |  _ \|_ _/ ___|_   _/ _ \ 
   / _ \ | |_) || |\___ \ | || | | |
  / ___ \|  _ < | | ___) || || |_| |
 /_/   \_\_| \_\___|____/ |_| \___/                                    
"""

    speed = color.GREEN + """
  /$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$ 
 /$$__  $$| $$__  $$|_  $$_/ /$$__  $$|__  $$__//$$__  $$
| $$  \ $$| $$  \ $$  | $$  | $$  \__/   | $$  | $$  \ $$
| $$$$$$$$| $$$$$$$/  | $$  |  $$$$$$    | $$  | $$  | $$
| $$__  $$| $$__  $$  | $$   \____  $$   | $$  | $$  | $$
| $$  | $$| $$  \ $$  | $$   /$$  \ $$   | $$  | $$  | $$
| $$  | $$| $$  | $$ /$$$$$$|  $$$$$$/   | $$  |  $$$$$$/
|__/  |__/|__/  |__/|______/ \______/    |__/   \______/
"""



    skull = color.CYAN + """
  ,------,------------------------------,------.
  |      |             Aristo           |      |
  |      |                              |      |
  |      |------------------------------|      |
  |      ||............................||      |
  |      ||     Hack Facebook? (y/n)   ||      |
  |      ||___                      ___||      |
  |      ||---`--------------------'---||      |
  `------'|____________________________|`------'               
"""
    lastthing = color.OKBLUE + """
 ▄▄▄       ██▀███   ██▓  ██████ ▄▄▄█████▓ ▒█████  
▒████▄    ▓██ ▒ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒
▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒
░██▄▄▄▄██ ▒██▀▀█▄  ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░
 ▓█   ▓██▒░██▓ ▒██▒░██░▒██████▒▒  ▒██▒ ░ ░ ████▓▒░
 ▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ 
  ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░    ░      ░ ▒ ▒░ 
  ░   ▒     ░░   ░  ▒ ░░  ░  ░    ░      ░ ░ ░ ▒  
      ░  ░   ░      ░        ░               ░ ░  
                                                       
"""
    lol = color.WARNING + """
         _nnnn_                      
        dGGGGMMb     
       @p~qp~~qMb     Aristo Rules! 
       M|@||@) M|   _;
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' 
"""
    headers = [header, oblique, modular, speed, skull, lastthing, lol]
    print headers[randint(0,6)]
