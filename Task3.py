#Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки.

#Пример:

#Для n = 6 -> 14.072

def func(num):
    lst = []
    sum = 0
    for i in range(1, 6+1):
        lst.append((1 + (1 / i)) ** i)
    for i in range(len(lst)):
        sum += lst[i]
    print(round(sum, 3))

n = int(input("Введите число: "))
func(n)