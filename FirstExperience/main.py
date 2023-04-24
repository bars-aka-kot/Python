# Множественное присваивание
a, b, c = 1, 2, 3

n = int(input("Введите число: "))
sum = 0
while n > 0:
    x = n % 10
    sum = sum + x
    n = n // 10
print(sum)

i = 0
while i < 5:
    i += 1
else:
    print("Достаточно")
    print("Хватит")
print(i)

n = int(input("Введите число: "))
flag = True
i = 2
if n == 0:
    print("Введенное число равно 0, операция завершена")
else:
    # Можно написать flag == True (Можно не писать, так как по умолчанию там True)
    while flag:
        if n % i == 0:
            flag = False
            print(i)
        elif i > n // 2:  # Делитель числа не может превышать введенное число, деленное на два
            print(n)
            flag = False
        i += 1

for i in 1, -2, 3, 14, 5:
    print(i)

r = range(100, 0, -20)
for i in r:
    print(i)

a = "qwerty"
for i in a:
    print(i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

'''Подстановка окончаний в зависимости от числа
words = ['день', 'дня', 'дней']

if all((value % 10 == 1, value % 100 != 11)):
    return words[0]
elif all((2 <= value % 10 <= 4,
          any((value % 100 < 10, value % 100 >= 20)))):
    return words[1]
return words[2]
'''

# срезы

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


# Списки
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])                # 1
print(list_1[1])                # 2
print(list_1[len(list_1)-1])    # 10
print(list_1[-1])               # 10
print(list_1[-5])               # 6
print(list_1[:])                # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])               # [1, 2]
print(list_1[len(list_1)-2])    # 9
print(list_1[2:9])              # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])            # []
print(list_1[0:len(list_1):6])  # [1, 7]
print(list_1[::6])              # [1, 7]

# Кортежи
t = ()
print(type(t))  # <class 'tuple'>

# Разъединение кортежа
t = (1, 2, 3,)
a, b, c = t
print(a, "***", b, "***", c)


dictionary = {}
dictionary['up'] = '↑'
print(dictionary)  # {'up': '↑'}

dictionary['left'] = '←'
print(dictionary)  # {'up': '↑', 'left': '←'}

# множества

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)  # i = {8, 2, 5}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}

# неизменяемые множества

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)  # frozenset({1, 2, 3, 5, 8})


# Генератор списков list comprehension

# list_1 = [exp for item in iterable]  # ппростой список
# list_1 = [exp for item in iterable(if conditional)]  # список с условием

list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)  # [1, 2, 3,..., 100]

# Второй вариант
list_1 = [i for i in range(1, 101)]  # [1, 2, 3,..., 100]
list_1 = [i for i in range(1, 101) if i % 2 == 0]  # [2, 4, 6,..., 100]

list_1 = [(i, i) for i in range(1, 101) if i %
          2 == 0]  # [(2, 2), (4, 4),...,(100, 100)]

list_1 = [i * 2 for i in range(10) if i % 2 == 0]  # [0, 4, 8, 12, 16]

list_1 = [int(input("Введите элемент: ")) for i in range(
    int(input("Введите количество элементов последовательности: ")))]
