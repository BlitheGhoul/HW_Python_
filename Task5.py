#Задание 5 Реализуйте алгоритм перемешивания списка.



import random


def mixing(n):
    lst1 = []
    for i in range(n + 1):
        lst1.append(i)
    print(f'Ваш список: {lst1}')
    for_mix = lst1[0]
    for i in range(n + 1):
        rand_num = random.randint(i, n)
        if lst1[rand_num] != for_mix:
            for_mix = lst1[rand_num]
            lst1[rand_num] = lst1[i]
            lst1[i] = for_mix
    print(f'Ваш список перемешан: {lst1}')

elements = int(input("Сколько элементов будет в Вашем списке? Введите число: "))
mixing(elements)