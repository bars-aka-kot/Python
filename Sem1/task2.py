''' Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) | '''

n = int(input("Enter the number: "))
sum = 0
while n > 0:
    x = n % 10
    sum = sum + x
    n = n // 10
print(f"The sum of the numbers of the number {n} -> {sum}")

# a = int(input())
# n3 = a%10
# n2 = a//10%10
# n1 = a//100
# print(n1+n2+n3)
# a = input()
# print(int(a[0])+int(a[1])+int(a[2]))
