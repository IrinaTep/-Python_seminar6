# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 10^5 (10 в 5 степени). 
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:                 Вывод:
# 300                   220 284


# def find_divisors_sum(num):
#     divisors_sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             divisors_sum += i
#     return divisors_sum

# def find_friendly_numbers(k):
#     friendly_pairs = []
#     for n in range(1, k + 1):
#         sum_n = find_divisors_sum(n)
#         if sum_n > n and find_divisors_sum(sum_n) == n:
#             friendly_pairs.append((n, sum_n))
#     return friendly_pairs

# k = 100000
# friendly_pairs = find_friendly_numbers(k)
# print("Количество пар дружественных чисел для k =", k, ":", len(friendly_pairs))
# print("Пары дружественных чисел:", friendly_pairs)

# Решение в группе
import functions
'''
def find_sum_delitel(num: int) -> int:
    summ = 0
    for i in range(1, num // 2 +1):
        if (num % i == 0):
            summ += i
    return summ
'''
k = functions.readint()

for i in range(1, k):
    temp_1 = functions.find_sum_delitel(i)
    temp_2 = functions.find_sum_delitel(temp_1)
    if ((temp_2 == i) and (temp_1 != temp_2) and (temp_1 < temp_2)):
        print(temp_1, temp_2)

# Решение от препода
def find_sum_delitel(num: int) -> int:
    summ = 0
    for i in range(1, num // 2 + 1):
        if (num % i == 0):
            summ += i
    return summ

k = 300

for num_1 in range(2, k):
    num_2 = find_sum_delitel(num_1) # можно перебрать и второе число for num_2 range(num_1 + 1, k), но мы схитрили, чтобы не делать два перебора

    if (find_sum_delitel(num_2) == num_1) and (num_1 < num_2):
        print(num_1, num_2)

# Другое решение:
# def sum_deltit(n):
#     sum = 0
#     for j in range(1, i//2+1):
#         if i % j == 0:
#             sum += j
#     return

# def dict_friendly(k):
#     dict = {}
#     for i in range(2, k + 1):
#         sum = 0
#         for j in range(1, i//2+1):
#             if i % j == 0:
#                 sum += j
#         dict[i] = sum

#     dict2 = []
#     for i in range(2, len(dict)):
#         for j in dict.values():
#             if i == dict.get(j) and j == dict.get(i) and i != j:
#                 key1 = str(i)+" "+str(j)
#                 key2 = str(j)+" "+str(i)
#                 if (key1 not in dict2) and (key2 not in dict2):
#                     dict2.append(key1)
#     return dict2

# number = int(input("Enter a number K: "))
# print(dict_friendly(number))