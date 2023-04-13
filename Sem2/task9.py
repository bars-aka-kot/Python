'''По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while
Input:       5
Output: 120'''

n = int(input("Enter the whole number: "))
faq = 1
i = 1
if n > 0:
    while i <= n:
        faq *= i
        i += 1
elif n == 0:
    print("0! = 1")
else:
    print("A negative number has been introduced!")
print(f"The factor of the number {n} -> {faq}")
