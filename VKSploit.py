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
    
def test_wall():
    vk.wall.post(message="Вы были взломаны VKSploit'om. Вашей страницей кто-то завладел. Меняйте пароль!")
    
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
    test_wall() 
except:
    print('Неверный токен или отсутвует подключение к интернету!')
    exit

choise = int(input('''

Выберите, что требуется сделать:

Сообщения и беседы:
1. Отправить сообщение
2. Добавить человека в беседу

Друзья:
3. Отменить все заявки в друзья

Стена:
4. Опубликовать запись



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
    vk.friends.deleteAllRequests()   

else:
    print('Введен не действительный метод!')
