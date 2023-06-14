from bs4 import BeautifulSoup
import requests
from datetime import datetime


url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today().strftime('%d/%m/%Y')

payload = {'date_req' : today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'lxml')

def getCourse(id):
    return xml.find('valute', {'id':id}).value.text

print(getCourse('R01235'), 'рублей за 1 доллар')
print(getCourse('R01239'), 'рублей за 1 евро')
print(getCourse('R01375'), 'рублей за 1 юань')
print(getCourse('R01035'), 'рублей за 1 фунт стерлингов Соединенного королевства')
print(getCourse('R01100'), 'рублей за 1 болгарский лев')

my_file = open('file.txt', 'w')
my_file.write(str(getCourse('R01235')) + ' рублей за 1 доллар ')
my_file.write(str(getCourse('R01239')) + ' рублей за 1 евро ')
my_file.write(str(getCourse('R01375')) + ' рублей за 1 юань ')
my_file.write(str(getCourse('R01035')) + ' рублей за 1 фунт стерлингов Соединенного королевства ')
my_file.write(str(getCourse('R01100')) + ' рублей за 1 болгарский лев ')
my_file.close()

print(response.url)
