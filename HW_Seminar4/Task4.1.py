'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов
 (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
from random import randint


k = int(input('Задайте степень: '))
coeffs_count = randint(1, 4)
example = ""
one = '*x^'
two = '*x'
plus = " + "
for i in range(coeffs_count):
    example += str(randint(0, 100))
    example += one
    example += str(k)
    example += plus
    example += str(randint(0, 100))
    example += two
    if i == coeffs_count - 1:
        example += " = 0"
    else:
        example += plus

with open('Task5.2.txt', 'w') as pineapple:
    pineapple.write(example)