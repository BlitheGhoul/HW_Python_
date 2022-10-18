'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Примерно так:
Дано: Строка "aaaaaaaaaaabbbbb333hhh"
После сжатия: "9a2a5b3_33h"
После восстановления: "aaaaaaaaaaabbbbb333hhh"
'''
def compression(same_str):
    count = 1
    cmpr_list = []
    for i in range(len(same_str)):
        if i < len(same_str) - 1:
            if same_str[i] == same_str[i+1]:
                if count < 9:
                    count += 1
                else:
                    if not same_str[i].isdigit():
                        cmpr_list.append(str(count) + same_str[i])
                        count = 1
                    else:
                        cmpr_list.append(str(count) + '_' + str(same_str[i]))
                        count = 1
            else:
                if not same_str[i].isdigit():
                    cmpr_list.append(str(count) + same_str[i])
                    count = 1
                else:
                    cmpr_list.append(str(count) + '_' + str(same_str[i]))
                    count = 1
        else:
            if not same_str[i].isdigit():
                cmpr_list.append(str(count) + same_str[i])
                count = 1
            else:
                cmpr_list.append(str(count) + '_' + str(same_str[i]))
                count = 1
    return cmpr_list

def decompression(any_list:list):
    
    final_str = ''
    for i in range(len(any_list)):
        count = 0
        for j in range(len(any_list[i])):
            if not any_list[i][j].isdigit():
                if any_list[i][j]!= "_":
                    final_str += int(count) * any_list[i][j]
            else:
                count = any_list[i][j]
            if any_list[i][j] == '_' and j == len(any_list[i]) - 1:
                final_str += int(count) * any_list[i][j]
            elif any_list[i][j] == '_':
                final_str += int(count) * any_list[i][j + 1]
    return final_str

str_to_compress = input('Введите символы для сжатия: ')
str_after_compress = compression(str_to_compress)

print(f'Cимволы после сжатия: {str_after_compress}')

print('Cимволы после восстановления: ', decompression(str_after_compress))