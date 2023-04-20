# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.
import random
lst = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    lst.insert(i, random.randint(0, 100))
    print(lst[i], end=" ")
print()
print(len(set(lst)))
