'''Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит 
в последовательность)”. Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. 
Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.'''

# Первый вариант
n = int(input(f"Введите элемент последовательности: "))
maxNumber = 0
while n != 0:
    if n > maxNumber:
        maxNumber = n
    n = int(input(f"Введите элемент последовательности: "))
print(
    f"Наибольший элемент последовательности -> {maxNumber}")

# Второй вариант
max_Num = 0
for i in range(int(input("Введите количество элементов последовательности: "))):
    i = int(input("Введите элемент: "))
    if i == 0:
        break
    else:
        if i > max_Num:
            max_Num = i
print(max_Num)