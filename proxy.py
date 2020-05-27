#! /usr/bin/python
"""
    @Author_name : Arsham mohammadi nesyshabori
    @Author_email : arshammoh1998@gmail.com
    @Author_nickname : apep
    @date : 
    @version : 
"""
import requests
from time import sleep
from bs4 import BeautifulSoup


def get_proxys(https=""):
    https = https.lower()
    p_list = []
    for _ in range(3):
        try:
            r = requests.get("https://free-proxy-list.net/")
            break
        except:
            sleep(3)
    else:
        raise(Exception("open website error"))

    soup = BeautifulSoup(r.content,"html.parser")
    soup = soup.find_all("td")
    for i in range(0,2400,8):
        temp=str(soup[i])
        temp=temp.replace("<td>","").replace("</td>","")
        if https in soup[i+6].text:
            port=soup[i+1].text
            p_list.append(temp+":"+port)
    return p_list

if __name__ == '__main__':
    print(get_proxy())
    