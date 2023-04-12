'''Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10'''

s = int(input("Enter the total number of cranes made: "))
if s % 6 != 0:
    print("It is impossible to say exactly how many cranes every")
else:
    # The integer division is used (//), because the division of the material (/) gives the result - float
    a = s // 6

print(f"The number of cranes made by Petr -> {a}")
print(f"The number of crane made by Sergey -> {a}")
print(f"The number of cranes made by Katya -> {4*a}")
