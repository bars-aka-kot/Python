'''Задача №45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n 
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа 
получает на вход одно натуральное число k, не превосходящее 10000. Программа должна вывести все 
пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в 
строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую 
пару не дает). timeline = 1:47:31
Ввод:               Вывод:
300                 220 284'''

from time import time
import math

#  Первый способ k = 50000 время выполнения 0.6000034809112549 с


def divider(n):
    i = 2
    sum = 1
    while i * i < n:
        if n % i == 0:
            sum += i
            sum += n // i
        i += 1
    return sum + i if i * i == n else sum


k = int(input("Введите число: "))
st = time()
if k <= pow(10, 9):
    for i in range(2, k + 1):
        b = divider(i)
        if k >= b > i == divider(b):
            print(i, b)
else:
    print("Задано слишком большое число")
print(f"{time() - st} с")

#  Второй способ k = 50000 время выполнения 81.58599472045898 с
k = int(input("Введите число: "))
st = time()

for n in range(1, k):
    m = 0
    sum2 = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            m += i
    for j in range(1, m//2 + 1):
        if m % j == 0:
            sum2 += j
    if sum2 == n and m > n:
        print(n, m)
print(f"{time() - st} с")

#  Третий способ k = 50000 время выполнения 172.71105289459229 с
k = int(input("Введите число: "))
nums = []
st = time()
for i in range(k):
    summ = 0
    for j in range(1, i//2 + 1):
        if i % j == 0:
            summ += j
    nums.append([i, summ])

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i][0] == nums[j][1] and nums[i][1] == nums[j][0] and i != j:
            print(*nums[i])
print(f"{time() - st} с")
