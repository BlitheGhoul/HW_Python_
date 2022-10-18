


'''
Создайте программу для игры в ""Крестики-нолики"".
'''
from random import randint, random

#ПЕРЕДЕЛАЙ ПРОВЕРКУ НА ПОБЕДИТЕЛЯ! ОНА КРИВАЯ! СМ ТЕСТ


def game(name1, name2):
    play_field = [[{},{},{}],[{},{},{}],[{},{},{}]]
    print('Поле для игры выглядит так: ')
    for i in range(len(play_field)):
        print(play_field[i])
    print('\nДля того чтобы сходить, Вам нужно будет указать номер столбца и номер строки.\
        \nНужно вводить только числа \'1\', \'2\' или \'3\'.')
    print('Вид поля: ')
    for i in range(len(play_field)):
        print(play_field[i])
    turn_to_move = randint(1,10)
    while True:
        if turn_to_move % 2 == 0:
            print(f'\n Ходит {name1}\n')
            line = input('Введите номер строки: ')
            if not line.isdigit():
                print('Введите число: \'1\', \'2\', или \'3\'')
                continue
            line = int(line)
            column = input('Введите номер столбца: ')
            if not column.isdigit():
                print('Введите число: \'1\', \'2\', или \'3\'')
                continue
            column = int(column)
            if line > 3 or line < 1 or column > 3 or column < 1:
                print('Введите число: \'1\', \'2\', или \'3\'')
                continue
            if play_field[line - 1][column - 1] == 'X' or play_field[line - 1][column - 1] == 'O':
                print('\nВыберите другую строку или столбец!')
                continue
            play_field[line - 1][column - 1] = 'X'
            print('\nВид поля: ')
            for i in range(len(play_field)):
                print(play_field[i])
            if play_field[0][0] == play_field[0][1] == play_field[0][2] == 'X' or play_field[1][0] == play_field[1]\
                [1] == play_field[1][2]  == 'X' or play_field[2][0] == play_field[2][1] == play_field[2][2]\
                 == 'X' or play_field[0][0] == play_field[1][0] == play_field[2][0]  == 'X' or play_field[0][1] == play_field[1][1]\
                 == play_field[2][1]  == 'X' or play_field[0][2] == play_field[1][2] == play_field[2][2]  == 'X' or \
                 play_field[0][0] == play_field[1][1] == play_field[2][2]  == 'X' or play_field[0][2] == play_field[1][1]\
                 == play_field[2][0]  == 'X':
                 return name1
            turn_to_move -= 1
        else:
            print(f'\n Ходит {name2}\n')
            line = input('Введите номер строки: ')
            if not line.isdigit():
                print('Введите число: \'1\', \'2\', или \'3\'')
                continue
            line = int(line)
            column = input('Введите номер столбца: ')
            if not column.isdigit():
                print('Введите число: \'1\', \'2\', или \'3\'')
                continue
            column = int(column)
            if line > 3 or line < 1 or column > 3 or column < 1:
                print('Введите число: \'1\', \'2\', или \'3\'')
                continue
            if play_field[line - 1][column - 1] == 'X' or play_field[line - 1][column - 1] == 'O':
                print('\nВыберите другую строку или столбец!')
                continue
            play_field[line - 1][column - 1] = 'O'
            print('\nВид поля: ')
            for i in range(len(play_field)):
                print(play_field[i])
            if play_field[0][0] == play_field[0][1] == play_field[0][2] == 'O' or play_field[1][0] == play_field[1]\
                [1] == play_field[1][2]  == 'O' or play_field[2][0] == play_field[2][1] == play_field[2][2]\
                 == 'O' or play_field[0][0] == play_field[1][0] == play_field[2][0]  == 'O' or play_field[0][1] == play_field[1][1]\
                 == play_field[2][1]  == 'O' or play_field[0][2] == play_field[1][2] == play_field[2][2]  == 'O' or \
                 play_field[0][0] == play_field[1][1] == play_field[2][2]  == 'O' or play_field[0][2] == play_field[1][1]\
                 == play_field[2][0] == 'O':
                 return name2
            turn_to_move += 1
    

first_player_name = input('Введите имя первого игрока: ')
second_player_name = input('Введите имя второго игрока: ')

winner = game(first_player_name, second_player_name)
print(f'Победил {winner}')