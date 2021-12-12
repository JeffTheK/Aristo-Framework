import random, string, smtplib
from time import sleep
from getpass import getpass
from subprocess import call
import color
from color import *

def sms():
    print(""+T+" ")
    print("Put the @ sign before the provider")
    provider = input(color.UNDERLINE + 'Enter cellular provider>' + color.END)
    print(""+T+" ")
    phone_num = input(color.UNDERLINE + 'Victims phone number>' + color.END) + provider
    print(""+T+" ")
    gmail = input(color.UNDERLINE + 'Your email>' + color.END)
    print(""+T+" ")
    password = getpass(color.UNDERLINE + 'Password>' + color.END)

    o = smtplib.SMTP("smtp.gmail.com:587")
    o.starttls()
    o.login(gmail, password)

    message = input(color.UNDERLINE + 'Message>' + color.END)
    print(""+T+" ")
    counter = input(color.UNDERLINE + 'How many times>' + color.END)
    print(""+T+" ")
    spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(gmail, phone_num, message)
    print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
    for i in range(counter):
        o.sendmail(gmail, phone_num, spam_msg)
    sleep(0.1)
    print (color.UNDERLINE + ''+G+'[*] Successfully sent!' + color.END)