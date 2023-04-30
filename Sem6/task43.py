'''Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые 
два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список 
чисел. Все числа списка находятся на разных строках.

Ввод:               Вывод:

1 2 3 2 3              2'''

lst = list(input("Введите числа через пробел: ").split(" "))
count = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            count += 1
print(count)

# Оптимизация
# lst = list(input("Введите числа через пробел: ").split(" "))
# count = 0
# for i in range(len(lst)):
#     if lst[i] in lst[i+1:]:
#         count += 1
# print(count)