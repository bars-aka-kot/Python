# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] [7, 11]
# Вывод: [1, 9, 13, 14, 19]

# First method
lst_input = list(input(
    "Введите элементы массива через запятую: ").split(", "))
lst = list(
    input("Введите границы через запятую: ").split(", "))
lst_output = list()

for i in range(len(lst_input)):
    if int(lst[0]) <= int(lst_input[i]) <= int(lst[1]):
        lst_output.append(i)

print(lst_output)

# second method
print(list(filter(lambda x: int(lst[0]) <= int(
    lst_input[x]) <= int(lst[1]), list(range(len(lst_input))))))
