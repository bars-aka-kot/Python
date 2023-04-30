# Подсчитайте сумму всех дружественных чисел меньше заданного.
from time import time


# def get_sum(n):
#     s = 0
#     for i in range(1, n):
#         if n % i == 0:
#             s += i
#     return s


# def gen_friendlys(n):
#     res = []
#     for i in range(1, n):
#         if i not in res:
#             tmp = get_sum(i)
#             if i == get_sum(tmp) and i != tmp:
#                 res.append(i)
#                 res.append(tmp)
#     return res

# print(sum(gen_friendlys(int(input("Введите число: ")))))

# Вывод пар друдественных чисел
st = time()

for num1 in range(1, 10001):
    num1_del = [num for num in range(1, num1) if num1 % num == 0]
    num2 = sum(num1_del)
    num2_del = [num for num in range(1, num2) if num2 % num == 0]
    if num1 == sum(num2_del) and num2 == sum(num1_del) and num1 != num2:
        print(f'{num1} and {num2} is friend!')

print(f"{time() - st} c")
