# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def arithmetic_progression(a1, d, n):
    progression = []
    for i in range(n):
        element = a1 + i * d
        progression.append(element)
    return progression


a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progression = arithmetic_progression(a1, d, n)
for element in progression:
    print(element, end=" ") # end=" " служит для продолжения вывода на той же строке, разделяя значения пробелом, а не переходя на новую строку