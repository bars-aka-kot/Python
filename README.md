# Примеры кода

a = 5  
b = 3  
print("a = ", a, ", b =", b)  
c = a * b  
print("c = ", c)  
print("a + c = ", a + c)  
if a > c:  
    print("a > c")  
else:  
    print("a < c")

## Разные форматы вывода данных

a = 5  
b  = 5.89  
c = "Hello!"  
print(a, b, c) *в этом случае выводится строка, содержащая все 3 значения, разделенные пробелом*  
print(a, " - ", b, " - ", c) *в этом случае и двух следующих - выводится строка, содержащая все 3 значения, разделенные тире*  
print(f"{a} - {b} - {c}")  
print("{} - {} - {}".format(a, b, c))  

## Ввод и вывод данных (спойлер - складываются строковые переменные)

print("Введите первое число: ")  
a = input()  
b = input("Введите второе число: ")  
print(a, "+", b, "=", a + b)

## Приведение типа и вывод типов

c = 5.89  
print(c)  
print(type(c))  
c = int(c)  *тип float (число с плавающей точкой) -> тип integer ( целочисленный )*  
print(c)  
print(type(c))  
c = str(c)  *тип float (число с плавающей точкой) -> тип string ( строковый )*  
print(c + "56")  *строковые переменные можно складывать - результат строка*  
print(type(c))  
c = 1  
c = bool(c)  *тип boolean - логический (значения True или False)*  
print(c)  
print(type(c))

## Преобразование строковых переменных и складывание чисел

print("Введите первое число: ")  
a = int(input())  
b = int(input("Введите второе число: "))  
print(a, "+", b, "=", a + b)

## Арифметические операции  

a + b - сложение  
a - b - вычитание  
a * b - умножение  
a / b - деление (по умолчанию в вещественных числах)  
a % b - остаток от деления  
a // b - целочисленное деление  
a ** b - возведение в степень

## Приоритет арифметических операций

1. Возведение в степень
1. Умножение
1. Деление
1. Целочисленное деление
1. Остаток от деления
1. Сложение
1. Вычитание

## Логические операции

- ">" - больше
- "<" - меньше
- ">=" - больше или равно
- "<=" - меньше или равно
- "==" - равно ("=" - присвоение)
- "!=" - не равно

в python в одном выражении можно сравнивать больше 2-х переменных (a>b>c>d)  
round(a, b) - округление числа a до b цифр после запятой
Важно делать отступы (если указать неправильное число отступов, программа может работать неправильно)

if - elif - else - блок если - иначе если - иначе
if - else - блок если - иначе
if condition1 and condition2 - выполнение тогда и только тогда, когда выполняются оба условия
if condition1 or condition2 - выполняется тогда, когда хотя бы одно условие выполняется

## Циклы

While condition - пока выполняется условие (true)
while condition - else - блок else выполняется после того, как завершится цикл (завершится сам, без принудительных остановок типа **break**). Break - для ООП не очень. Обычно применяется flag
for i in enumeration - программа будет выполняться до тех пор, пока i будет не выйдет за пределы enumeration

## функция range(a,b,c)

Выдает значения из диапазона [a, b) с шагом c (а - включительно, b - не включительно)  
При отсутствии указания шага, по умолчанию берется шаг = 1  
При положительном шаге должно выполняться условие a < b, при отрицательном шаге - a > b

Примеры записей:

- r = range(5) # 0 1 2 3 4 - не указывается первый аргумент, по умолчанию берется 0
- r = range(2, 5) # 2 3 4
- r = range(0, -5) # ----
- r = range(1, 10, 2) # 1 3 5 7 9
- r = range(100, 0, -20) # 100 80 60 40 20

## Списки

Коллекция данных - структура данных, которая создана, чтобы содержать в себе некоторое количество объектов (одного или разных типов). Бывают разного вида:

- списки
- кортежи
- словари
- множества

1. список - это упорядоченный конечный набор элементов. В качестве ключа используется индекс
Создание списка:
list_1 = [] - создание пустого списка
list_1 = list() - создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17] - заполненный список

> Нумерация в списках начинается с нуля.  
> Для вывода конкретного элемента: print(list_1[0])  
> При выводе списка - команда print(list_1) - будет выведено [7, 9, 11, 13, 15, 17]. Если перед названием списка ввести **"*"** (*print(*list_1)*) - будут выведены значения без скобок [] и запятых - 7 9 11 13 15 17

    Список можно изменять:

- добавлять элементы **list_1.append(n)**, где n - значение элемента списка. Добавляется в конец списка
- удаление элемента из списка **list_1.pop()** - удаляет последний элемент в списке. **list_1.pop(i)** - удаление i-го элемента в списке.
- добавление элемента на конкретное место в списке **list_1.insert(2, 11)** - добавление элемента **11** на **2** позицию (по индексу)

2. кортеж - неизменяемый список. Работает быстрее и занимает меньше места.
Создание кортежа:
t = () - создание пустого кортежа
t = (1, 2, 3, ) - создание кортежа. Обязательно в конце ставить запятую
Можно тип list (список) преобразовать в кортеж (tuple).

> v = [2, 5, 3] - тип list
> v = tuple(v)

3. словарь - неупорядоченные коллекции произволльныз объектов с доступом по ключу. В качестве ключа используется не индекс, а значение ключа (значение элемента)

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←

***типы ключей могут отличаться***
print(dictionary['up']) # ↑
***типы ключей могут отличаться***
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
print('{}: {}'.format(item, dictionary[item])) # up: ↑ # down: ↓ # right: →

4. Множества содержат в себе уникальные элементы, не обязательно упорядоченные

> Одно множество может содержать значения любых типов

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

Неизменяемое или замороженное множество(frozenset) — множество, с которым
не будут работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

## Генератор списков list comprehension

list_1 = [exp for item in iterable]  # ппростой список
list_1 = [exp for item in iterable(if conditional)]  # список с условием

## Часто встречающиеся ошибки

SyntaxError(Синтаксическая ошибка)
number_first = 5
number_second = 7
if number_first > number_second  # !!!!!
print(number_first)

***Отсутствие :***

IndentationError(Ошибка отступов)
number_first = 5
number_second = 7
if number_first > number_second:
print(number_first) # !!!!!

***Отсутствие отступов***

TypeError(Ошибка типов)
text = 'Python'
number = 5
print(text + number)

***Нельзя складывать строки и числа***

ZeroDivisionError(Деление на 0)
number_first = 5
number_second = 0
print(number_first // number_second)

***Делить на 0 нельзя***

KeyError(Ошибка ключа)
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[3])

***Такого ключа не существует***

NameError(Ошибка имени переменной)
name = 'Ivan'
print(names)

***Переменной names не существует***

ValueError(Ошибка значения)
text = 'Python'
print(int(text))

***Нельзя символы перевести в целые значения***
