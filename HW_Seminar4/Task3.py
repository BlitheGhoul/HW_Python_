'''
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
'''


my_list = list( map(int, input('Введите последовательность, через пробел: '). split()))
second_lst = []
for i in range(len(my_list)):
    j = 1
    if i >= j:
        j = 0 
    while j <= len(my_list) - 1:
        if i == j:
            if j == len(my_list) - 1 and my_list[i] == my_list[j]:
                second_lst.append(my_list[i])
            j += 1
            continue
        if my_list[i] != my_list[j]:
            j += 1
        elif my_list[i] == my_list[j]:
            break
        if j == len(my_list) - 1 and my_list[i] != my_list[j]:
            second_lst.append(my_list[i])

print(second_lst)