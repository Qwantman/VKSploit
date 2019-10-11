try:
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.keyboard import VkKeyboard, VkKeyboardColor
    import vk_api
    import os
except:
    print('Установите, пожалуйста нужные пакеты через pip install <Имя пакета>')

print('Пакеты успешно импортированы, запускаю программу!')

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
