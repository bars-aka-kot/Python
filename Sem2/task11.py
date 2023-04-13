'''Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1.
Input:     5
Output: 6'''

a = int(input("Enter a whole number: "))
firstNumber = 0
secondNumber = 1
count = 2
nextNumber = 0
if a >= 2:
    while nextNumber < a:
        nextNumber = firstNumber + secondNumber
        firstNumber = secondNumber
        secondNumber = nextNumber
        count += 1
    if nextNumber != a:
        print(f"Number {a} not the number of Fibonacci")
    else:
        print(f"The position of the number {a} -> {count}")
elif a == 1:
    print(f"The position of the number {a} -> 2 и 3")
else:
    print(f"The position of the number {a} -> 1")

# Второй метод без вывода count для чисел 0 и 1
print("The second option")
while nextNumber != a:
    nextNumber = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = nextNumber
    count += 1
    if nextNumber > a:
        print(f"Number {a} not the number of Fibonacci")
        break
else:
    print(f"The position of the number {a} -> {count}")
