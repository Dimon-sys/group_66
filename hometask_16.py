from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today().strftime('%d/%m/%Y')
payload = {'date_req' : today}
response = requests.get(url, params=payload)
xml = BeautifulSoup(response.content, 'lxml')

def course(valute_from, valute_to, amount):
    

valute_from = input() #EUR
valute_to = input() #USD
amount = int(input())
print(course(valute_from, valute_to, amount))