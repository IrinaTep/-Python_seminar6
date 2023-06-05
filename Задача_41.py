# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.

# Ввод:                                  Ввод:
# 5                                      5
# 1 2 3 4 5                              1 5 1 5 1
# Вывод:                                 Вывод:
# 0                                      2
# (каждое число вводится с новой строки)

import functions

'''
Во вкладке functions находится метод:
def find_top(list_1: list) -> int:
    count = 0
    for i in range(1, len(list_1)-1):
        if list_1[i] > list_1[i-1] and list_1[i] > list_1[i+1]: # запись удобнее: if list_1[i-1] < list_1[i] > list_1[i+1]:
            count += 1
    return count
'''

# n = functions.readint()
list_n = [1, 5, 1, 5, 1]
count = 0

# for i in range(n)
#     list_n.append(functions.readint())


count_top = functions.find_top(list_n)
print(count_top)
