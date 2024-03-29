'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и 
возводит число А в целую степень B с помощью рекурсии.'''


def recurs(a, b):

    if b < 0:
        return 1/a * recurs(a, b + 1)
    if b == 0:
        return 1
    return a * recurs(a, b - 1)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(recurs(a, b))
