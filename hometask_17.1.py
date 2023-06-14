import pyaudio
import speech_recognition as sr
import pyttsx3
import random

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('Привет, я голосовой помощник')
voice.runAndWait()
list_hi = ['Привет', 'Hello', 'Приветики', 'Здравствуй', 'Хай']
list_film = ['Форрест Гамп', 'Бойцовский клуб', 'Назад в будущее', 'Терминатор']

while True:
    with sr.Microphone(device_index=0) as sourse:
        print('Скажи что-нибудь . . .')
        audio = r.listen(sourse)

    speech = r.recognize_google(audio, language='ru_Ru').lower()
    print('Вы сказали:' + speech)

    if speech.find('привет') >= 0:
        voice.say(random.choice(list_hi))
        voice.runAndWait()

    elif speech.find('фильм') >= 0:
        voice.say('Советую вам фильм ' + random.choice(list_film))
        voice.runAndWait()

