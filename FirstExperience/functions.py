# # def math(op, a, b, c):
# #     print(op(a, b, c))


# # math(lambda x, y, z: x*y // z, 4, 5, 2)

# '''1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]'''

# # list = [1, 2, 3, 5, 8, 15, 23, 38]
# # list1 = []
# # for i in list:
# #     if i % 2 == 0:
# #         list1.append((i, i**2))
# # print(list1)


# # def select(f, col):
# #     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# out = map(int, list1)
# out = filter(lambda x: x % 2 == 0, out)
# out = list(map(lambda x: (x, x**2), out))
# print(out)


# # list_1 = [x for x in range(1, 20)]
# # print(list_1)

# # list_1 = list(map(lambda x: x+10, list_1))
# # print(list_1)

# # data = "12 3 2 3 4 56 3 434 23 2"

# # data = list(map(int, data.split()))
# # print(data)

# data = [12, 65, 9, 15, 3, 8, 25, 2]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 6, 7, 8]
# data = list(zip(users, ids))
# # [('user1', 4), ('user2', 5), ('user3', 6), ('user4', 7), ('user5', 8)]
# print(data)

# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# # [('user1', 4, 111), ('user2', 5, 222), ('user3', 6, 333)] - по минимальному набору данных
# print(data)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
# [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]
print(data)
