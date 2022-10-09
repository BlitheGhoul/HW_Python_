'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

*Пример*

- при N=236     ->        [2, 2, 59]
'''

my_num = int(input('Введите число: '))
list_multi = []
i = 2
count = my_num
while i <= my_num:
    if my_num % i == 0:
        list_multi.append(i)
        my_num /= i
        print(1)
    elif my_num / i == 1:
        list_multi.append(i)
        break
    else:
        i += 1

print(list_multi)