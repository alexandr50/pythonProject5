from lesson_6.utils import read_from_file, game, write_file, print_info_history

if __name__ == '__main__':
    # Ввод имени пользователя
    user_input_name = input('Программа: Введите ваше имя ')
    print(f'Пользователь: {user_input_name}')

    result_of_reading = read_from_file('words.txt')

    result_of_game = game(result_of_reading)

    write_file('history.txt', result_of_game, user_input_name)

    print_info_history()


