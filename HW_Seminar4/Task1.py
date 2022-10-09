'''
#Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

d = float(input("Введите желаемую точность: "))

num1 = 0
num2 = 1.0
num3 = 1.0
while True:
    enough = 4 / num2
    num1 = num1 + num3 * enough
    if enough < d:
        print(num1)
        break 
    else:
        num3 = -num3
        num2 +=  2.0