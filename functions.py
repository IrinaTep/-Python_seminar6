def readint():
    num = int(input("Введите число: "))

    return num

def list_difference(list_1, list_2):
    list_dif = list()
    for i in list_1:
        for j in list_2:
            if i == j:
                break
        else:
            list_dif.append(i)
    return list_dif

# к 41 задаче
def find_top(list_1: list) -> int:
    count = 0
    for i in range(1, len(list_1)-1):
        if list_1[i] > list_1[i-1] and list_1[i] > list_1[i+1]: # запись удобнее: if list_1[i-1] < list_1[i] > list_1[i+1]:
            count += 1
    return count

# к 43 задаче
def find_doubles(list_1: list):
    double = 0
    for i in range(len(list_1) - 1):
        for j in range(i + 1, len(list_1)):
            if list_1[i] == list_1[j]:
                double += 1
    return double

# к 45 задаче
def find_sum_delitel(num: int) -> int:
    summ = 0
    for i in range(1, num // 2 +1):
        if (num % i == 0):
            summ += i
    return summ

# к 32_домашней задаче
def find_indexes(arr, min_value, max_value):
    indexes = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indexes.append(i)
    return indexes
    