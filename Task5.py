'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

Fn = F(n+2)-F(n+1).
'''

def fibonacci(n):
    num_1 = 0
    num_2 = 1
    lst_ = [num_1, num_2]
    for i in range(2, n + 1):
        num_1, num_2 = num_2, num_1 - num_2
        lst_.insert(0, num_2)
    num_1 = 0
    num_2 = 1
    for i in range(2, n + 1):
        num_1, num_2 = num_2, num_1 + num_2
        lst_.append(num_2)
    print(lst_)  

my_number = int(input("Введите Ваше число: "))

fibonacci(my_number)
