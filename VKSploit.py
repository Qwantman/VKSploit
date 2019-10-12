try:
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.keyboard import VkKeyboard, VkKeyboardColor
    import vk_api
    import os
    import random
except:
    print('Установите, пожалуйста нужные пакеты через pip install <Имя пакета>')

print('Пакеты успешно импортированы, запускаю программу!')

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
except:
    print('Неверный токен или отсутвует подключение к интернету!')
    exit

choise = int(input('''

ВНИМАНИЕ! ПРОГРАММА СОЗДАНА В ОБРАЗОВАТЕЛЬНЫХ ЦЕЛЯХ И ЕЙ НЕ ПОСТАВЛЕНА ЗАДАЧА КОМУ-ЛИБО НАВРЕДИТЬ! ДАННУЮ ПРОГРАММУ ВЫ ИСПОЛЬЗУЕТЕ, ПОНИМАЯ, ЧТО СОЗДАТЕЛЬ НЕ НЕСЁТ НИКАКОЙ ОТВЕТСТВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ. ВСЕ ДЕЛАЕТСЯ НА ВАШ СТРАХ И РИСК!

Выберите, что требуется сделать:

Сообщения и беседы:
1. Отправить сообщение
2. Добавить человека в беседу

Друзья и ЧС:
3. Отменить все заявки в друзья
4. Добавить человека в ЧС
5. Убрать человека из ЧС
6. Пожаловаться на пользователя

Стена:
7. Опубликовать запись



Ваш выбор: '''))

ch = choise

if(ch == 1):
    id = input('Введите id получателя/чата: ')
    message = input('Введите сообщение для отправки: ')
    attachment = input('Если требуется введите id вложения в формате photo<id>_<id>: ')
    if(len(attachment) == 0):
        attachment = None
    else:
        pass
    send(message=message, peer_id=id, attachment=attachment)
    
elif(ch == 2):
    id = input('Введите id пользователя для добавления в беседу: ')
    cid = input('Введите id беседы куда надо добавить пользователя: ')
    add_chat(user_id=id, chat_id=cid)
    
elif(ch == 3):
    res = vk.friends.deleteAllRequests()
    print('Успешно')
        
elif(ch == 4):
    id = input('Введите id человека для добавления в ЧС: ')
    res = give_BAN(id)
    print('Успешно')
        
elif(ch == 5):
    id = input('Введите id человека для уборки из ЧС: ')
    res = takeAway_BAN(id)
    print('Успешно')
    
elif(ch == 6):
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
        
elif(ch == 7):
    message = input('Введите текст для поста: ')
    attachment = input('Если требуется введите id вложения в формате photo<id>_<id>: ')
    if(len(attachment) == 0):
        attachment = None
    else:
        pass
    wall_post(message=message, attachment=attachment)
    
else:
    print('Введен не действительный метод!')
