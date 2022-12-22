import random


# функция считывания данных из файла
def read_from_file(file):
    with open(file, 'r', encoding='utf-8') as file:

    #  складываем в список считанные слова
        return list(map(lambda x: x.strip('\n'), file.readlines()))

#  функция записи в файл
def write_file(file, data_for_write: str, user_name: str):
    with open(file, 'a') as fl:
        result = f'{user_name} {data_for_write}'
        fl.write(result)




# функция игры
def game(lst: list):
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
    data_for_write = f'{str(points)}\n'
    return data_for_write




#  функция вывода информации из истории
def print_info_history():


    res = read_from_file('history.txt')
    record = 0

        # находим максимальный результат
    for i in res:
        data_after_split = i.split(' ')
        score = int(data_after_split[1])
        if score > record:
            record = score

    #  вывод иформации
    print(f'Всего игр сыграно: {len(res)}')
    print(f'Максимальный рекорд: {record}')


#  основная функция
def main():
    # Ввод имени пользователя
    user_input_name = input('Программа: Введите ваше имя ')
    print(f'Пользователь: {user_input_name}')

    result_of_reading = read_from_file('words.txt')

    result_of_game = game(result_of_reading)

    write_file('history.txt', result_of_game, user_input_name)

    print_info_history()








