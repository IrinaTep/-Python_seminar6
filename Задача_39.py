# Даны два массива чисел. 
# Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
#
# Ввод:                             Вывод:
# 7                                 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1                    (каждое число вводится с новой строки)

import functions

# n = functions.readint()
list_n = [3, 1, 3, 4, 2, 4, 12]

# for i in range(n):
#    list_n.append(functions.readint())

# m = functions.readint()
list_m = [4, 15, 43, 1, 15, 1]

# for i in range(m):
#    list_m.append(functions.readint())

list_dif = functions.list_difference(list_n, list_m)

print(list_dif)

# # Другие способы
# list_res = []

# len_test_list1 = 7 # int(input("Введите количество элементов"))
# test_list1 = [3, 1, 3, 4, 2, 4, 12]

# for i in range(len_test_list1):
#     test_list1.append(int(input("Введите элементы: ")))
# print(test_list1)

# len_test_list2 = 6 # int(input("Введите количество элементов"))
# test_list2 = [4, 15, 43, 1, 15, 1]

# for i in range(len_test_list2):
#     test_list2.append(int(input("Введите элементы: ")))
# print(test_list2)

# # способ 1
# for i in test_list1:
#     if i not in test_list2:
#         list_res.append(i)
# print(list_res)

# # способ 2
# test_res = set(test_list1) - set(test_list2)
# print(test_res)
# for i in test_list1:
#     if i in test_res:
#         print(i)

# Способ через count
# def list_create_random(begin_num, end_num, length): # у создателя метода была написана функция для создания списка
#     import random
#     return [random.randint(begin_num, end_num) for _ in range(length)]

# def diff_lists(list_1, list_2):
#     for i in range(len(list_1)):
#         if list_2.count(list_1[i]) == 0:
#             print(list_1[i], end=" ")

# len_1st_list = int(input("Enter a number-length for 1st list: "))
# list_1st = list_create_random(1, 9, len_1st_list)

# len_2nd_list = int(input("Enter a number-length for 2nd list: "))
# list_2nd = list_create_random(1, 9, len_2nd_list)

# print(*list_1st)
# print(*list_2nd)

# diff_lists(list_1st, list_2nd)

# Превращаем решение1 в функцию
# for i in test_list1:
#     if i not in test_list2:
#         list_res.append(i)
# print(list_res)

def search_dif(list_1: list[int], list_2: list[int]) -> list[int]: # или вертнет кортеж интов И кортеж строк -> tuple[int] | tuple[str]
    list_res = []
    for i in list_1:
        if i not in list_2:
            list_res.append(i)
    return list_res

print(search_dif([1, 2, 3], [2, 3]))

