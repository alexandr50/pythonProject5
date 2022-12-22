import random


# Ввод имени пользователя
user_input_name = input('Программа: Введите ваше имя')
print(f'Пользователь: {user_input_name}')


#  открытие файла на тчтение
with open('words.txt', 'r', encoding='utf-8') as file:

    #  складываем в список считанные слова
    lst = list(map(lambda x: x.strip('\n'), file.readlines()))

    #  переменная очков пользователя
    points = 0
    while len(lst) != 0:

        #  берем первое слово и делаем список из букв
        word_list = list(lst[0])

        # перемешиваем и делаес строку
        random.shuffle(word_list)
        word = ''.join(word_list)

        # ввод пользователя
        print(f'Программа: Угадайте слово: {word}')
        user_input = input(f'Пользователь: ')


        # логика угадал не угадал
        if user_input == lst[0]:
            print(f'Программа: Верно! Вы получаете 10 очков.')
            points += 10
        else:
            print(f'Программа: Неверно! Верный ответ – {lst[0]}.')
        lst.pop(0)

    #  делаем строку со статистикой для записи в файл
    data_for_write = f'{user_input_name} {str(points)}\n'

    # записываем в файл данные
    with open('history.txt', 'a') as fl:
        fl.write(data_for_write)

#  считывание данных истрии игры из файла
with open('history.txt', 'r') as file:
    res = list(map(lambda x: x.strip('\n'), file.readlines()))
    record = 0

    # на ходим максимальный результат
    for i in res[1:]:
        data_after_split = i.split(' ')
        score = int(data_after_split[1])
        if score > record:
            record = score

    #  вывод иформации
    print(f'Всего игр сыграно: {len(res)}')
    print(f'Максимальный рекорд: {record}')
