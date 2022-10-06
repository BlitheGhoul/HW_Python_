'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт 
сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

def sum_of_odd(some_lst : list):
    sum = 0
    for i in range(1, len(some_lst)):
        if i % 2 != 0:
            sum = sum + some_lst[i]
    print(f'Сумма элементов на нечетных позициях: {sum}')

lst = []
count = int(input("Введите желаемый размер списка: "))
for i in range(count):
    j = int(input(f'Введите {i} число: '))
    lst.append(j)
sum_of_odd(lst)

