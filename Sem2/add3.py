'''Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до B включительно; 
при этом каждое число должно выводиться столько раз, каково его значение (например, число 3 выводится 3 раза).'''

a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
while a <= b:
    for i in range(a):
        print(a)
    a += 1
