'''Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Пример:
4 4 -> 2 2
5 6 -> 2 3 '''

import math

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

# Первый вариант через квадратное уравнение

x = int(0.5 * (s + math.sqrt(s * s - 4 * p)))
y = int(0.5 * (s - math.sqrt(s * s - 4 * p)))

print(f"Первый вариант решения: Два загаданных числа -> {x} и {y}")

# Второй вариант через перебор

for x in range(1001):
    for y in range(1001):
        if x + y == s and x * y == p:
            print(f"Второй вариант решения: Два загаданных числа -> {x} и {y}")