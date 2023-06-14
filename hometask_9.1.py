import requests 
from bs4 import BeautifulSoup


def get_heads():
    responce = requests.get('http://www.columbia.edu/~fdc/sample.html')
    responce = responce.content
    html = BeautifulSoup(responce, 'lxml')
    heads = []
    headss = html.find_all(class_= 'h3', id ="contents")
    heads.append(headss)

get_heads()