import pyaudio
import speech_recognition as sr
import pyttsx3
import random
import os
import webbrowser

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('Привет, я голосовой помощник')
voice.runAndWait()
list_hi = ['Привет', 'Hello', 'Приветики', 'Здравствуй', 'Хай']

while True:
    with sr.Microphone(device_index=0) as sourse:
        print('Скажи что-нибудь . . .')
        audio = r.listen(sourse)

    speech = r.recognize_google(audio, language='ru_Ru').lower()
    print('Вы сказали:' + speech)

    if speech.find('привет') >= 0 or speech.find('хай') >= 0 or speech.find('здравствуй') >= 0:
        voice.say(random.choice(list_hi))
        voice.runAndWait()

    elif speech.find('открой') >= 0:
        webbrowser.open('https://www.youtube.com/')
        voice.say('Ютуб запущен')
        voice.runAndWait()

    elif speech.find('создай') >= 0:
        os.mkdir('Новая папка 2')
        voice.say('Папка создана')
        voice.runAndWait()
    
    elif speech.find('пока') >= 0:
        voice.say('До встречи')
        voice.runAndWait()
        break
    else:
        voice.say('Я вас не понимаю')
        voice.runAndWait()
