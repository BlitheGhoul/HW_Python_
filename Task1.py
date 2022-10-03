#Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11

def sum_num(any_number):
    res = 0
    for i in range(len(any_number)):
        if any_number[i].isdigit() == True:
            res = res + int(any_number[i])
    print(f'Cумма цифр Вашего числа: {res}')

num = str(input("Введите число: "))
sum_num(num)



