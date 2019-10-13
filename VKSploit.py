try:
    from vk_api.longpoll import VkLongPoll, VkEventType
    import vk_api
    import os
    import random
    import json
    import time
except:
    print('Установите, пожалуйста нужные пакеты через pip install <Имя пакета>')

print('Пакеты успешно импортированы, запускаю программу!')

def close_programm():
    exit

def send(message=None, attachment=None, peer_id=None):
    vk.messages.send(peer_id=id, message=message, attachment=attachment, random_id=random.randint(-2147483648,+2147483648))

def add_chat(chat_id, user_id):
    vk.messages.addChatUser(chat_id=chat_id, user_id=user_id)
    
def wall_post(message, attachment=None):
    vk.wall.post(message=message, attachment=attachment)
    
def give_BAN(id):
    vk.account.ban(owner_id=id)
    
def takeAway_BAN(id):
    vk.account.unban(owner_id=id)
    
def give_warn(id, type, comment=None):
    vk.users.report(user_id=id, type=type, comment=comment)
    
def change_pass(old, new):
    vk.account.changePassword(old_password=old, new_password=new)
    
print('Получить токен можно тут: vkhost.github.io. Токен нужен ОБЯЗАТЕЛЬНО от Kate Mobile!')
token = input('Введите токен: ')

while(1 == 1):
    if(len(token) == 0):
        print('Вы не ввели токен!')
        token = input('Введите токен: ')
    else:
        pass
        break

print('Токен распознан. Пытаемся подключиться к серверам ВК...')

try:
    token1 = token
    vk_session = vk_api.VkApi(token=token1)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    print('Подключено!')
    print('ВНИМАНИЕ! ПРОГРАММА СОЗДАНА В ОБРАЗОВАТЕЛЬНЫХ ЦЕЛЯХ И ЕЙ НЕ ПОСТАВЛЕНА ЗАДАЧА КОМУ-ЛИБО НАВРЕДИТЬ! ДАННУЮ ПРОГРАММУ ВЫ ИСПОЛЬЗУЕТЕ, ПОНИМАЯ, ЧТО СОЗДАТЕЛЬ НЕ НЕСЁТ НИКАКОЙ ОТВЕТСТВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ. ВСЕ ДЕЛАЕТСЯ НА ВАШ СТРАХ И РИСК!')
except:
    print('Неверный токен или отсутвует подключение к интернету!')
    exit()

while(1 == 1):
    time.sleep(5)
    choise = input('''

    Выберите, что требуется сделать:
    
    Профиль:                                    Сообщения и беседы:
    1. Сменить пароль                           2. Отправить сообщение
                                                3. Добавить человека в беседу
                                                4. Просмотреть приходящие сообщения

    Друзья и ЧС:                                Стена:
    5. Отменить все заявки в друзья             9. Опубликовать запись
    6. Добавить человека в ЧС
    7. Убрать человека из ЧС
    8. Пожаловаться на пользователя
    
    
                                                99. Инфо о программе
                                                00. Выход
    
    Ваш выбор: ''')

    ch = int(choise)

    if(ch == 1):
        old = input('Введите старый пароль: ')
        new = input('Введите новый пароль: ')
        change_pass(old=old, new=new)
        print('Успешно!')

    elif(ch == 2):
        id = input('Введите id получателя/чата: ')
        message = input('Введите сообщение для отправки: ')
        attachment = input('Если требуется введите id вложения в формате photo<id>_<id>: ')
        if(len(attachment) == 0):
            attachment = None
        else:
            pass
        send(message=message, peer_id=id, attachment=attachment)

    elif(ch == 3):
        id = input('Введите id пользователя для добавления в беседу: ')
        cid = input('Введите id беседы куда надо добавить пользователя: ')
        add_chat(user_id=id, chat_id=cid)

    elif(ch == 4):
        print('Запускаю...')
        time.sleep(3)
        print('Запущено, начинаю логгирование :)')
        while(1 == 1):
            for event in longpoll.listen():
                if (event.type == VkEventType.MESSAGE_NEW):
                    f = open('log.txt', 'w')
                    text = event.text
                    if(event.from_chat):
                        cid = event.chat_id
                        text = 'Чат с id: ' +str(cid) +' написал ' + str(text)
                        f.write(text)
                        print(text)
                    elif(event.from_user):
                        id = event.user_id
                        text = 'Человек с id: ' +str(id) +' написал ' + str(text)
                        f.write(text)
                        print(text)

    elif(ch == 5):
        res = vk.friends.deleteAllRequests()
        print('Успешно')

    elif(ch == 6):
        id = input('Введите id человека для добавления в ЧС: ')
        res = give_BAN(id)
        print('Успешно')

    elif(ch == 7):
        id = input('Введите id человека для уборки из ЧС: ')
        res = takeAway_BAN(id)
        print('Успешно')

    elif(ch == 8):
        id = input('Введите id человека для подачи жалобы: ')
        type = input('''
        Выберите тип жалобы:
        
        porn — порнография;
        spam — рассылка спама;
        insult — оскорбительное поведение;
        advertisеment — рекламная страница, засоряющая поиск.
        
        Введите тип так же как и сверху:
        ''')
        type = type.lower()
        message = input('Если требуется введите сообщение для поддержки: ')
        if(len(message) == 0):
            message = None
        else:
            pass
        give_warn(id=id, type=type, comment=message)
        print('Успешно!')

    elif(ch == 9):
        message = input('Введите текст для поста: ')
        attachment = input('Если требуется введите id вложения в формате photo<id>_<id>: ')
        if(len(attachment) == 0):
            attachment = None
        else:
            pass
        wall_post(message=message, attachment=attachment)

    elif(ch == 00):
        exit()

    elif(ch == 99):
        print('''
        Версия программы: 1.3
        Создатель: Qwantman
        Описание: Программа для управления ВК при помощи токена
        ''')
        exit()

    else:
        print('Введен не действительный метод!')
