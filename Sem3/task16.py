# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

n = int(input("Введите количество чисел: "))
x = int(input("Введите число X: "))
count = 0
for i in range(1, n+1):
    print(i, end=" ")
    if i == x:
        count += 1
print()
print(count)