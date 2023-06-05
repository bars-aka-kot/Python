from time import time


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


i = "N"
while True:
    n = int(input(
        "Введите порядковый номер числа Фибоначчи: "))
    st = time()
    print(fib(n))
    print(f"{round((time() - st),5)} c")
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)
