# list comprehension
# a = [i if i < 9 else 0 for i in range(10)]
# print(a)

# enumerate

# a = [0, 1, 2, (3, 2, 5), "sdfs"]
# for indx, val in enumerate(a):
#     print(indx, val)

# zip
# a = (1, 2, 4, 5, 6)
# b = "abcd"
# c = {12: "fr", 45: "ge", 23: "ru"}
# for i in zip(a, b, c.values()):
#     print(i)

# lambda
# когда один раз используется функция
# def summa(a, b):
#     return a+b

# def a(x, y): 
#     return x+y if x == 3 else 0
# print(a(5, 4))
# print(lambda x,y: x+y if x%2 == 0 else 0)

# map
# a = [1, 2, 3, 4, 5, 6]
# a = list(map(lambda el: el if el % 2 == 0 else el+1, a))
# print(a)

# filter оставляет только те значения, которые удовлетворяют условию
# a = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda el: True if el % 2 == 0 else False, a))
# print(a)
