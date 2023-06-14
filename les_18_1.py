from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.geometry('400x350+300+300')
window.title('Курс валют')

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today().strftime('%d/%m/%Y')

payload = {'date_req' : today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'lxml')

def getCourse(id):
    return xml.find('valute', {'id':id}).value.text


img_logo = PhotoImage(file = 'logo.png')
logo = Label(window, image=img_logo)
logo.place(x=0, y=0)


lab = Label(window, text='Курс валют \n MAXIMUM банк', fg='black', font= 'Arial 22') 
lab.place(x=150, y=25)

course_info = Label(text='Курс на: ' + today.replace('/', '.'), font='Arial 18')
course_info.place(x=90, y=150)

course_USD = Label(window, text='$: ' + getCourse('R01235') + ' руб.', bg='blue', fg='green', font='Arial 18',)
course_USD.place(x=90, y=190)

course_EUR = Label(window, text='€: ' + getCourse('R01239') + ' руб.', bg='purple', fg='orange', font='Arial 18')
course_EUR.place(x=90, y=230)

course_UAN = Label(window, text='¥: ' + getCourse('R01375') + ' руб.', bg='#FF5463', fg='gold', font='Arial 18')
course_UAN.place(x=90, y=270)

window.resizable(width=False, height=False)

window.mainloop()