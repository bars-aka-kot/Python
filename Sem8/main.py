# r - read, w - write (перезапись), a - запись (дозапись)
# open("file.txt", "w") #w - если нет файла - создает
# создает файл и записывает файл в переменную file для дальнейшей работы
# file = open("Sem8/file1.txt", "w")
# with open("Sem8/file.txt", "w") as file:  # с параметром with можно прописать несколько команд, которые будут распространяться на один и тот же file.txt
#     a = ["asd\n", "aahggggggggggg\n", "asdada\n"]
#     file.writelines(a)
#     file.write("asdfjf")
# with open("Sem8/file.txt", "r") as file:
#     for i in range(3):
#         # останавливается на начале 4 строки
#         # .strip() - удаляет символ переноса строки /n
#         print(file.readline().strip())
#     file.seek(0)  # на начало файла
#     print(file.read())  # читает снова с начала
#     file.seek(0)
#     # выводит все строки файла в виде списка
#     lst = file.readlines()

# a = [(2, 3, 4), (1, 3, 7), (5, 5, 9)]
# b = ["asz", "weo", "erny"]
# a.sort(key=lambda x: (x[1], x[2])) # сортировка по второму элементу и одновременно по третьему в кортежах
# b.sort(key=lambda x: x[2])
# print(a)
# print(b)

# a = [(2, 3, 4), (1, 3, 7), (5, 5, 9)]
# # выдает кортеж с максимальным первым элементом
# print(max(a, key=lambda x: x[1]))

# a = [(2, -1, 4), (1, -2, 7), (5, 5, 9)]
# a = sorted(a, key=lambda x: (x[1], x[2]))
# print(a)
