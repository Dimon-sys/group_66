import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'lxml')


def get_course(currency):
    return str(xml.find("valute", {'id': currency}).value.text)


if __name__ == '__main__':
    print(get_course("Доллар США"), "рублей за 1 доллар")
    print(get_course("Евро"), "рублей за 1 евро")
    print(get_course("Китайский юань"), "рублей за 10 юаней")
