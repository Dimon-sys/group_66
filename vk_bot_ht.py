import vk_api
import requests
import json
from course import *

token = 'vk1.a.TDFuWa8oEWwB9lf0ToWXdzN8S0moi0aCYaX2nRp_8L2cCGo4arhSC5TDy-eIHkobhszIzpGo8NJZjjRfGWvPjNf69DNdlqUEsCaCbUp2zDPXOQomwUo1ZyZKTVKt9HkjQQEwLelPpimIh2TNVkb4-fr6fTUfOl7tW8TjKYth204K9H6v5OrRXb4Sba-66xXKQVgDe-76fMhYWoLIDrm46A'
vk = vk_api.VkApi(token=token)

messages = vk.method('messages.getConversations', {'count' : 20, 'filter' : 'unanswered'})

url = 'http://swapi.dev/api/'

responce = requests.get(url).json()

people_api = responce.get('people')
planets_api = responce.get('planets')
starships_api = responce.get('starships')

def max_diameter(url):
    diameters_list = []
    for i in range(1, 11):
        responce = requests.get(f'{url}/{i}').json()
        diameters_list.append(int(responce.get('diameter')))
    return max(diameters_list)

def max_speed(url):
    max_speed_list = []
    for i in range(1, 11):
        responce = requests.get(f'{url}/{i}').json()
        max_speed_list.append(int(responce.get('max_atmosphering_speed')))
    return max(max_speed_list)


while True:
    messages = vk.method('messages.getConversations', {'count' : 20, 'filter' : 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if message_text.lower() == 'курс':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message' : get_course('R01235')})
        elif message_text.lower() == 'планеты':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message' : max_diameter(url)})
        elif message_text.lower() == 'корабли':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message' : max_speed(url)})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message' : 'неизвестная команда'})