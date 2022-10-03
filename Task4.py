#Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на позициях a и b.
#Значения N, a и b вводит пользователь с клавиатуры.

def elements(num):
    lst =[]
    for i in range(num):
        lst.append(-num + i)
    a = 0
    while a <= num:
        lst.append(num - (num - a))
        a += 1
    print(lst)
    a = int(input('Введите число "a": '))
    b = int(input('Введите число "b": '))
    prod = lst[a] * lst[b]
    print(prod)

n = int(input("Введите значение N: "))
elements(n)