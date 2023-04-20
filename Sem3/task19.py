'''Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо,  K – положительное число.
Input:   [1, 2, 3, 4, 5] k = 2
Output:  [4, 5, 1, 2, 3]'''

n = int(input("Введите количество элементов списка: "))
list_1 = [int(input("Введите элемент: ")) for i in range(n)]
print(list_1)
k = int(input("Введите K: "))
lst_2 = list_1[len(list_1)-k:] + list_1[:len(list_1)-k]
if k > 0:
    for i in range(k):
        list_1.insert(0, list_1.pop())
else:
    for i in range(abs(k)):
        list_1.append(list_1.pop(0))
print(f"По первому методу {list_1}")
print(
    f"По второму методу {lst_2}")
