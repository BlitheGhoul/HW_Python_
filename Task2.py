'''
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
from math import ceil


def multiplication(some_lst : list):
    multipls = []
    for i in range(ceil(len(some_lst) / 2)):
        multipls.append(some_lst[i] * some_lst[-i - 1])
    print(f'Произведения пар чисел списка: {multipls}')

lst = []
count = int(input("Введите желаемый размер списка: "))
for i in range(count):
    j = int(input(f'Введите {i} число: '))
    lst.append(j)
multiplication(lst)