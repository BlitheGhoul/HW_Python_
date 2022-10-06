'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
def print_how_number(any_number):
    lst_ = []
    print(f'Число {any_number} в двоичном коде выглядит так: ', end = '')
    while any_number >= 1:
        lst_.append(int(any_number % 2))
        any_number /= 2
    for i in range(len(lst_)):
        print(lst_[-i - 1], end = '')

my_number = int(input('Введите число, которое Вы хотите перевести в двоичный код: '))
print_how_number(my_number)


