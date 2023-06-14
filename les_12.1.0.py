import telebot 
import requests
from bs4 import BeautifulSoup
import random


token = '5729287599:AAFnjPFilsmihmaeJQ_88dxRvcNzIS_3KuE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start', 'help'])
def send_welcome(message, res = False):
    welcome_text = """
    Привет! Я знаю много интересных фактов и могу отправлять разные фотографии, ещё могу порекомендовать какую-нибудь игру
    """

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('Факт')
    button2 = telebot.types.KeyboardButton('Стихотворение')
    button3 = telebot.types.KeyboardButton('Котики')
    button4 = telebot.types.KeyboardButton('Стикер')
    button5 = telebot.types.KeyboardButton('Игра')
    keyboard.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


@bot.message_handler(commands= ['fact'])
def send_fact():
    responce = requests.get('https://i-fakt.ru/')
    responce = responce.content
    html = BeautifulSoup(responce, 'lxml')
    fact = random.choice(html.find_all(class_ = 'p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    fact_text = fact.text
    bot.send_message(fact.chat.id, fact_link + fact_text)

@bot.message_handler(commands= ['poem'])
def send_poem(message):
    poem_text = "Погиб поэт! Невольник чести..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardButton(row_width=1)
    button_url = telebot.types.InlineKeyboardButton('Перейти ', url = 'https://stihi.ru/')
    keyboard.add(button_url)
    bot.send_message(message.chat.id, 'Больше стихов по ссылке ниже', reply_markup=keyboard)

@bot.message_handler(commands=['picture'])
def send_cat(message):
    cat_number = str(random.randint(1, 9))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, 'rtagudnkegvnjrwe')

@bot.message_handler(commands=['music'])
def send_song(message):
    song = open('happy.mp3', 'rb')
    bot.send_audio(message.chat.id, song)

@bot.message_handler(commands=['game'])
def send_game(message):
    bot.send_message(message.chat.id, 'Рекомендую игру Astroneer. Очень расслабляет')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.strip() == 'Факт':
        send_fact(message)
    elif message.text.strip() == 'Стихотворение':
        send_poem(message)
    elif message.text.strip() == 'Котики':
        send_cat(message)
    elif message.text.strip() == 'Стикер':
        send_sticker(message)
    elif message.text.strip() == 'Игра':
        send_game(message)


bot.infinity_polling()