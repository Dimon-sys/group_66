import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from course import get_course
from wiki import get_wiki_article
from requests.exceptions import ReadTimeout, ProxyError
import requests
from bs4 import BeautifulSoup
import requests

token = 'vk1.a.TDFuWa8oEWwB9lf0ToWXdzN8S0moi0aCYaX2nRp_8L2cCGo4arhSC5TDy-eIHkobhszIzpGo8NJZjjRfGWvPjNf69DNdlqUEsCaCbUp2zDPXOQomwUo1ZyZKTVKt9HkjQQEwLelPpimIh2TNVkb4-fr6fTUfOl7tW8TjKYth204K9H6v5OrRXb4Sba-66xXKQVgDe-76fMhYWoLIDrm46A'
while True:
    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()

        longpoll = VkLongPoll(vk_session)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                msg = event.text.lower()
                user_id = event.user_id

                random_id = random.randint(1, 10 ** 10)
                if msg == '-к':
                    responce = '{0} рублей за 1 доллар\n{1} рублей за 1 евро\n'\
                            '{2} рублей за 10 юаней\n {3} рублей за 1 фунт'.format(
                                get_course('R01235'),
                                get_course('R01239'),
                                get_course('R01375'),
                                get_course('R01035')
                            )
                    vk.messages.send(user_id = user_id, random_id = random_id, message = responce)
        
                elif msg.startswith('-в'):
                    article = msg[3:]
                    responce = get_wiki_article(article)[:500]
                elif msg == 'максим кирпичников':
                    responce = 'Максим Кирпичников Валерьевич - самый главный форшмак среди форшмаков.\n Очень нехороший мальчик.\n Любит пиво и харкать в окружающих. \n Отрицает свои нетрадиционные садамазахистические увлечения. \n Замужем'
                    maksim_img = open('Maksiemen.png', 'rb')
                else:
                    responce = 'Неизвестная команда'

                vk.messages.send(user_id = user_id, random_id = random_id, message = responce)
    except (ReadTimeout, ProxyError):
        pass