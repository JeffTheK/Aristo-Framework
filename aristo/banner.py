# coding: utf-8
#!/usr/bin/env python
from random import *
import color
from color import *

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
    print(headers[randint(0,6)])
