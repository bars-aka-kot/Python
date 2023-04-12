'''Требуется определить, можно ли от шоколадки размером n x m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no '''

text = input(
    "Enter the size of the chocolate in slices (M and N) and the number of slices that need to be broken off (K): ")
m = int(text.split()[0])
n = int(text.split()[1])
k = int(text.split()[2])

if k < m * n and (k % m == 0 or k % n == 0):
    print(
        f"You can break off {k} a lobster from the chocolate size {m} x {n}, breaking it only once in a straight line")
else:
    print(
        f"You can not break off {k} a lobster from the chocolate size {m} x {n}, breaking it only once in a straight line")
