import vk_api
from course import *

token = 'vk1.a.TDFuWa8oEWwB9lf0ToWXdzN8S0moi0aCYaX2nRp_8L2cCGo4arhSC5TDy-eIHkobhszIzpGo8NJZjjRfGWvPjNf69DNdlqUEsCaCbUp2zDPXOQomwUo1ZyZKTVKt9HkjQQEwLelPpimIh2TNVkb4-fr6fTUfOl7tW8TjKYth204K9H6v5OrRXb4Sba-66xXKQVgDe-76fMhYWoLIDrm46A'
vk = vk_api.VkApi(token=token)

messages = vk.method('messages.getConversations', {'count' : 20, 'filter' : 'unanswered'})

while True:
    messages = vk.method('messages.getConversations', {'count' : 20, 'filter' : 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if message_text.lower() == 'курс':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message' : get_course('R01235')})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message' : 'неизвестная команда'})