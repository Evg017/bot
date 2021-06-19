# Данный бот способен прислать треки и информацию о музыкальной группе
# Бот умеет отправлять клавиатуру, inline клавиатуру и карусель
# Следует использовать API версии 5.131
  
# Импорт модулей
import vk_api
import random
from vk_api.bot_longpoll import VkBotEventType
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from carousel import * # Подключение карусели
from parser2 import * # Подключение парсера


vk = vk_api.VkApi(token="") # Ввод токена
vk._auth_token()
vk.get_api()
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
longpoll позволяет получать информацию о новых событиях с помощью «длинных запросов».
Сервер получает запрос, но отправляет ответ на него не сразу, а лишь тогда, когда произойдет какое-либо событие 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
longpoll = VkBotLongPoll(vk, ) # Ввод id группы (цифры)
concert = create_concert()


# Функция обработки сообщений
def send_message(user_id, text, keyboard=None, template=None):
    vk.method("messages.send", {"user_id": user_id, "message": text,
                                "random_id": random.randint(-9223372036854775807, 9223372036854775807),
                                "keyboard": keyboard, "template": template})     

try:                              
    for event in longpoll.listen(): # longpoll слушает сервер на наличие новых сообщений
        if event.type == VkBotEventType.MESSAGE_NEW:          
            if event.object.message['text'].lower() in ['начать', 'обновить']: # Пробуждает бота и присылает постоянную клавиатуру и первое сообщение
                keyboard = VkKeyboard(inline=False) # Если значение True, отправляется inline клаватура, если False постоянная клавиатура
                keyboard.add_button('Прислать клавиатуру', color=VkKeyboardColor.POSITIVE) # Кнопка, которая отправляет сообщение от имени пользователя
                keyboard.add_line() # Перенос кнопки на следующую строчку. 
                keyboard.add_button('График концертов', color=VkKeyboardColor.PRIMARY)
                send_message(event.object.message["from_id"], "Привет, данный бот содержит все вышедшие треки группы 'Anacondaz'.\nИспользование бота наипростейшее - с помощью кнопок.", keyboard=keyboard.get_keyboard()) # Отправка пользователю сообщения с текстом
                        
            elif event.object.message['text'].lower() in ['прислать клавиатуру']: # Присылает inline клавиатуру в сообщении
                keyboard = VkKeyboard(inline=True)
                keyboard.add_button('Альбомы (LP)', color=VkKeyboardColor.PRIMARY) # Кнопка с цветом (Всего 4 цвета).
                keyboard.add_line() 
                keyboard.add_button('EP, фиты, синглы и неизданное', color=VkKeyboardColor.PRIMARY)
                keyboard.add_line() 
                keyboard.add_button('Live', color=VkKeyboardColor.PRIMARY)
                keyboard.add_line() 
                keyboard.add_button('Информация о группе', color=VkKeyboardColor.POSITIVE)
                keyboard.add_line() 
                keyboard.add_button('FAQ и связь с автором бота', color=VkKeyboardColor.POSITIVE)
                send_message(event.object.message["from_id"], "Выбери, что нужно", keyboard=keyboard.get_keyboard())           

            elif event.object.message["text"].lower() == "альбомы (lp)": # Реагирует на нажатие кнопки "Альбомы (LP)", присылает новую клавиатуру с выбором
                if event.object.client_info["carousel"] == True:
                    send_message(event.object.message["from_id"], "Сборник всех альбомов!", template=carousel)

            elif event.object.message["text"].lower() == "ep, фиты, синглы и неизданное": # Реагирует только на текст "EP, фиты, синглы и неизданное", если нужно сделать реагирование на несколько команд, то нужно изменить на "if event.object.message['text'] in ['EP, фиты, синглы и неизданное', 'Еще текст']:"
                if event.object.client_info["carousel"] == True: # Разрешает присылать карусель
                    send_message(event.object.message["from_id"], "Здесь собраны все доступные EP, фиты, синглы и неизданные треки:", template=carousel2)
            
            elif event.object.message["text"].lower() == "live":
                if event.object.client_info["carousel"] == True:
                    send_message(event.object.message["from_id"], "Записанные треки с концертов:", template=carousel3)

            elif event.object.message['text'].lower() in ['информация о группе']: # Реагирует на нажатие кнопки "Информация о группе", присылает кнопки ссылками и отправкой карусели
                keyboard = VkKeyboard(inline=True)
                keyboard.add_button('Состав группы', color=VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_openlink_button('Официальный сайт', 'https://anacondaz.ru') # Кнопка с ссылкой. Если кнопка с ссылкой, то цвет кнопки поменять нельзя (из документации)
                keyboard.add_line()
                keyboard.add_openlink_button('YouTube канал', 'https://www.youtube.com/c/rapanacondaz') # Сначала прописывается название кнопки, затем ссылка
                keyboard.add_line()
                keyboard.add_openlink_button('Группа в VK', 'https://vk.com/anacondaz')
                keyboard.add_openlink_button('Канал в Telegram', 'https://t.me/anacondaz_official')
                keyboard.add_line()
                keyboard.add_openlink_button('Instagram', 'https://www.instagram.com/rap_anacondaz')
                keyboard.add_openlink_button('Twitter', 'https://twitter.com/rap_anacondaz')
                keyboard.add_line()
                keyboard.add_openlink_button('Anacondaz в Facebook', 'https://www.facebook.com/rapanacondaz')                
                send_message(event.object.message["from_id"], 'Данные на группу', keyboard=keyboard.get_keyboard())

            elif event.object.message['text'].lower() in ['состав группы']:
                if event.object.client_info["carousel"] == True:
                    send_message(event.object.message["from_id"], "Состав группы и ссылки на их соц.сети:", template=sostav)

            elif event.object.message['text'].lower() in ['twitter - утерян', 'twitter - не найден']:
                    send_message(event.object.message["from_id"], "Ну и зачем ты тыкнул?")
                    
            elif event.object.message['text'].lower() == 'faq и связь с автором бота':
                keyboard = VkKeyboard(inline=True)
                keyboard.add_openlink_button('Евгений Селиванов', 'https://vk.com/evg_017')
                send_message(event.object.message["from_id"], "В: Вышел новый трек, а в боте его нет.\nО: Я стараюсь оперативно обновлять список треков, если трека нет, то можно мне об этом напомнить (ссылка ниже).")
                send_message(event.object.message["from_id"], "В: Ничего не работает!\nО: Да такое может быть. Нужно обновить клиент VK до последней версии.")
                send_message(event.object.message["from_id"], "Написать с предложениями по улучшению и дополнению функционала можно мне в ЛС. Если это будет в моих силах, то я обязательно это добавлю.", keyboard=keyboard.get_keyboard())

            elif event.object.message["text"].lower() == "график концертов": # Присылает график концертом с помощью парсера
                con = ''
                for i in range(len(concert)):
                    con =  str(con) + f'• {concert[i].get("Город")} ({concert[i].get("Когда")}) - {concert[i].get("Место")} ({concert[i].get("Ссылка на мероприятие")})\n\n'
                send_message(event.object.message["from_id"], con)
                send_message(event.object.message["from_id"],'Если ссылка ведёт на паблик Anacondaz, значит встреча еще не создана.\nTBA - To Be Announced (Будет Объявлено).')
                

            elif event.object.message['text'].lower() in ['прислать клавиатуру!']:
                keyboard = VkKeyboard(inline=False)
                keyboard.add_button('Прислать клавиатуру', color=VkKeyboardColor.POSITIVE)
                keyboard.add_line() # Перенос кнопки на следующую строчку. 
                keyboard.add_button('График концертов', color=VkKeyboardColor.PRIMARY)
                send_message(event.object.message["from_id"], "Бот был обновлён. Кнопки обновлены.", keyboard=keyboard.get_keyboard())
            # Для обновления клавиатуры на новую. Если обновлю нижние кнопки (автоматически не обновляются).
            
            else:
                send_message(event.object.message["from_id"], "Неправильная команда. Пользуйся кнопками, ничего более писать не нужно.") # Если пользователь пишет то, что не надо, ему придёт это сообщение

# Не выключает бота после обновления серверов                
except Exception as ex:
    print(ex)
