'''Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

Input: 5
Output: yes'''


# def funk(n):
#     if n == 1:
#         return n
#     if n % (n - 1) > 0:
#         funk(n)
#     print(n)


n = int(input("Введите число: "))

# def funk(n):
#     m = 2
#     while n > m:
#         if n % m == 0:
#             return "false"
#         else:
#             m += 1
#     return "true"

# print(funk(n))


# def isprime(n, d):
#     if n % d == 0:
#         print(f"{n} -> Число не простое")
#         return False
#     if d**2 > n:
#         print(f"{n} -> Число простое")
#         return True
#     return isprime(n, d+1)


# print(isprime(n, 2))

# def prime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n


# print(prime(n))

def simple(n):
    for i in range(2, int(pow(n, 0.5))):
        if n % i == 0:
            return False
    return True


print(simple(n))
