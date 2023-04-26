# def sumNumbers(n, y="Hello, world!"):
#     # print("qwerty")
#     sum = 0
#     for i in range(n+1):
#         sum += i
#     print(sum)


# n = int(input("Input the number: "))
# sumNumbers(n)

# Если вызвать в теле метода вывод такого же

''' Второй вариант через return'''


def sumNumbers(n, y="Hello"):
    print(y)
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


n = int(input("Input the number: "))
y = input("Введите фразу: ")
print(sumNumbers(n), y)
