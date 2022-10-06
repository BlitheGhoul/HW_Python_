'''
Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

def find (any_lst: list):
    max = 0
    min = lst_[0]
    for i in range(len(any_lst)):
        if any_lst[i] % 1 != 0:
            if any_lst[i] % 1 > max:
                max = any_lst[i] % 1
            elif any_lst[i] % 1 < min:
                min = any_lst[i] % 1
    print('Разница между максимальным и минимальным значением дробной части элементов: ', round(max - min, 2))

def filling(any_lst: list):
    count = int(input("Укажите сколько элементов будет в списке: "))
    for i in range(count):
        j = float(input(f'Введите {i} число: '))
        any_lst.append(j)


lst_ = []
filling(lst_)
find(lst_)

