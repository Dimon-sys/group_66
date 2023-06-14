import requests 
from bs4 import BeautifulSoup
import random


def get_interesting_fact():
    responce = requests.get('https://i-fakt.ru/')
    responce = responce.content
    html = BeautifulSoup(responce, 'lxml')
    fact = random.choice(html.find_all(class_ = 'p-2 clearfix'))
    print(fact.text)
    print(fact.a.attrs['herf'])


def get_event():
    responce = requests.get('https://kudago.com/msk/festival/')
    responce = responce.content
    html = BeautifulSoup(responce, 'lxml')
    fest = random.choice(html.find_all(class_ = 'post-title'))
    print(fest.text)
    print(fest.a.attrs['herf'])

def get_fest():
    responce = requests.get('https://kudago.com/msk/concerts/')
    responce = responce.content
    html = BeautifulSoup(responce, 'lxml')
    festival = random.choice(html.find_all(class_ = 'post-title'))
    print(festival.text)
    print(festival.a.attrs['herf'])

user_wish = ' '
while user_wish != 'хватит':
    user_wish = input('Чем бы вы хотели заняться?').lower()
    if 'факт' in user_wish:
        get_interesting_fact()
    elif 'концерт' in user_wish:
        get_fest()
    elif 'фестиваль' in user_wish:
        get_event()
    else:
        print('-')
