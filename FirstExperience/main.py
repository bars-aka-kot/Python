# n = int(input("Введите число: "))
# sum = 0
# while n > 0:
#     x = n % 10
#     sum = sum + x
#     n = n // 10
# print(sum)

# i = 0
# while i < 5:
#     i += 1
# else:
#     print("Достаточно")
#     print("Хватит")
# print(i)

# n = int(input("Введите число: "))
# flag = True
# i = 2
# if n == 0:
#     print("Введенное число равно 0, операция завершена")
# else:
#     # Можно написать flag == True (Можно не писать, так как по умолчанию там True)
#     while flag:
#         if n % i == 0:
#             flag = False
#             print(i)
#         elif i > n // 2:  # Делитель числа не может превышать введенное число, деленное на два
#             print(n)
#             flag = False
#         i += 1

# for i in 1, -2, 3, 14, 5:
#     print(i)

# r = range(100, 0, -20)
# for i in r:
#     print(i)

# a = "qwerty"
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# срезы
"""
text = "СъЕШЬ ещё этих МяГкИх французских булок"
# print(len(text)) # выдает длину строки
# print("ещё" in text) # показывает, есть ли такое значение в строке
# print(text.lower()) # переводит все символы в строчные
# print(text.upper()) #переводит все символы в прописные
# print(text.replace("ещё", "ЕЩЁ")) # заменяет значение 1 на значение 2
print(text[0])              # С
print(text[1])              # ъ
print(text[2])              # E
print(text[len(text)-1])    # к
print(text[-1])             # к
print(text[-5])             # б
print(text[:])              # СъЕШЬ ещё этих МяГкИх французских булок
print(text[:2])             # Съ
print(text[len(text)-2])    # ок
print(text[2:9])            # ЕШЬ ещё
print(text[6:-18])          # ещё этих МяГкИх
print(text[0:len(text):6])  # Сеикакл
print(text[::6])            # Сеикакл
print(text[2:10] + text[-5] + text[-6] + text[:2])  # ЕШЬ ещё б Съ
"""
