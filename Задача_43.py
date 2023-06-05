# Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:                   Вывод:
# 1 2 3 2 3               2
# 1 2 1 2 2 3             4

import functions

'''
def find_doubles(list_1: list):
    double = 0
    for i in range(len(list_1) - 1): # последний элемент нам проверять уже не нужно
        for j in range(i + 1, len(list_1)):
            if list_1[i] == list_1[j]:
                double += 1
    return double
'''

# n = functions.readint()
list_n = [1, 2, 3, 2, 2, 3]

# for i in range(n)
#     list_n.append(functions.readint())

doubles = functions.find_doubles(list_n)
print(doubles)

'''
# Другой способ
def how_many_pairs(new_list):
    counter = 0
    for i in range(len(new_list) - 1):
        for j in range(i + 1, len(new_list)):
            if new_list[i] == new_list[j]:
                counter += 1
    return(counter)

def make_a_list(n):
    new_list = []
    for i in range (n):
        new_list.append(int(input("Input a num: ")))
    return(new_list)

new_list = make_a_list(int(input("Input a quantity of elements in lists: ")))
print(f"There are {how_many_pairs(new_list)} pairs in list")
'''