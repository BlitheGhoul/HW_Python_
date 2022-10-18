'''
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
'''

from random import random
def game1(name1, name2, n1, n2):
    turn_to_move = random.randint(1, 10) 
    count = n1
    take = 0
    for i in range(n1 + 1):
        if turn_to_move % 2 == 0:
            print(f'\nХодит {name1}')
            take = abs(int(input('\nСколько конфет вы хотите вязть? Введите число: ')))
            if take > count:
                print(f'\nНа столе осталось всего {count} конфет, возьмите меньше.')
                continue
            if take > n2:
                print(f'\nМы договорились брать только {n2} конфет, попробуйте ещё раз')
                continue
            if take == 0:
                take = 1
                print(f'{name2} пытается схитрить, но всё же берёт 1 конфету')
            count -= take
            if count == 0:
                return name1
            else:
                turn_to_move += 1
                print(f'\nНа столе осталось {count} конфет')
                continue
        else:
            print(f'\nХодит {name2}')
            take = abs(int(input('\nСколько конфет вы хотите вязть? Введите число: ')))
            if take > count:
                print(f'\nНа столе осталось всего {count} конфет, возьмите меньше.')
                continue
            if take > n2:
                print(f'\nМы договорились брать только {n2} конфет, попробуйте ещё раз')
                continue
            if take == 0:
                take = 1
                print(f'{name2} пытается схитрить, но всё же берёт 1 конфету')
            count -= take
            if count == 0:
                return name2
            else:   
                turn_to_move += 1
                print(f'\nНа столе осталось {count} конфет')
                continue

def game2(name1, name2, n1, n2):
    turn_to_move = random.randint(1, 10) 
    count = n1
    take = 0
    for i in range(n1 + 1):
        if turn_to_move % 2 == 0:
            print(f'\nХодит {name1}')#БОТ
            take = random.randint(1,n2)
            while take > count:
                take = random.randint(1, count)
            while take > n2:
                take = take = random.randint(1,n2)
            print(f'\n{name1} утащил {take} конфет')
            count -= take
            if count == 0:
                return name1
            else:
                turn_to_move += 1
                print(f'\nНа столе осталось {count} конфет')
                continue
        else:
            print(f'\nХодит {name2}')
            take = abs(int(input('\nСколько конфет вы хотите вязть? Введите число: ')))
            if take > count:
                print(f'\nНа столе осталось всего {count} конфет, возьмите меньше.')
                continue
            if take > n2:
                print(f'\nМы договорились брать только {n2} конфет, попробуйте ещё раз')
                continue
            if take == 0:
                take = 1
                print(f'{name2} пытается схитрить, но всё же берёт 1 конфету')
            count -= take
            if count == 0:
                return name2
            else:   
                turn_to_move += 1
                print(f'\nНа столе осталось {count} конфет')
                continue

        

print("На столе лежит сколько-то конфет\nПервый ход определяется жеребьёвкой.\
    \nЗа один ход можно забрать только определенное количество конфет, ноль кофет взять нельзя\
    \nВсе конфеты оппонента достаются сделавшему последний ход")
amount_1 = int(input("\nСколько конфет будет лежать на столе? Введите число: "))
amount_2 = int(input("\nСколько конфет можно взять за один ход? Введите число: "))
game_mod = int(input('Выберите режим игры:\nВведите 1 - если хотите играть против бота\
    \nВведите 2 - если хотите играть против человека\n'))
if game_mod == 1:
    print('\nВыбран режим игры против бота')
    fn = ['Прекрасный ', 'Вредный ' , 'Хитрый ' , 'Дерзкий ' , 'Одноногий ' , 'Зелёный ' , 'Мужественный ']
    ln = ['Ананас', 'Мыш', 'Пират', 'Бурундук', 'Рыцарь', 'Осьминог', 'Самец']
    player_name = input('\nВведите имя первого игрока: ')
    bot_name = fn[random.randrange(1,len(fn))] + ln[random.randrange(1,len(ln))]
    print('Бота для игры с Вами зовут:', bot_name)
    winner = game2(bot_name, player_name, amount_1, amount_2)
elif game_mod == 2:
    print('Выбран режим игры против человека\n')
    first_player_name = input('Введите имя первого игрока: ')
    second_player_name = input('Введите имя второго игрока: ')
    print('\nОтлично, начнём!\n') 
    winner = game1(first_player_name, second_player_name, amount_1, amount_2)
else:
    print('Ошибка не выбран режим игры, перезапустите программу')

print(f'Победил: {winner}')