'''
2. Напишите программу, удаляющую из текста все слова, содержащие "абв". <- filter
'''

with open ('words.txt', 'a', encoding='UTF-8') as data:
    data.write('ананас вотрушко георгин лебедь')

with open('words.txt', 'r', encoding='UTF-8') as data:
    words = list(map(str, data.readline().split()))
print(f'Слова в начальном тексте {words}')

def my_words(x:list):
    sumbol = ['а', 'б', 'в']
    for i in range(len(sumbol)):
        x = list(filter(lambda y: True if y.find(sumbol[i]) == -1 else False, x))
    return x

new_words = my_words(words)

print(new_words)