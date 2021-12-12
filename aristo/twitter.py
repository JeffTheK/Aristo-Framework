#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup as So
import urllib ,sys
import color
from color import *

def twitter():
    def get(twitter):
        try:
            u = urllib.urlopen(twitter)
            data = u.read()
            s = So(data, 'html.parser')
            details = s.find_all("span" ,{"data-is-compact":"false"})
            following = details[1].text.encode("utf-8")
            name = s.find("a" ,{"href":"/"+twitter.split("/")[-1]}).text.encode("utf-8").replace("  ","").replace("\n","")
            followers = details[2].text.encode("utf-8")
            likes = details[3].text.encode("utf-8")
            pic = s.find("a" ,{"class":"ProfileAvatar-container u-block js-tooltip profile-picture"})["href"].encode("utf-8")
            date = s.find("span" ,{"class":"ProfileHeaderCard-joinDateText js-tooltip u-dir"})["title"].encode("utf-8")
            print(G + " Name: " + W + name)
            print(G + " Following: " + W + following)
            print(G + " Followers: " + W + followers)
            print(G + " Likes: " + W + likes)
            print(G + " This Account was made on: " + W + date)
            print(G + " Full Profile Picture: " + W + pic)
        except:
            print(R + "Error <Twitter_Profile_link>/<username> is not correct")
            sys.exit(0)


    u = input(''+T+'' + color.UNDERLINE + 'Username>' + color.END)



    if "twitter.com" not in u:
        get("https://twitter.com/" + u)
    else:
        get(u)
