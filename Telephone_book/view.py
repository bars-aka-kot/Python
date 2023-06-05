import database


def user_input():
    ask = int(input("Выбери ниже:\n 1 - Записать пользователя в телефонную книгу\n 2 - найти в телефонной книге\n \
3 - сортировать записи по фамилии\n 4 - сортировать записи по номеру телефона\n 5 - вывести все записи\n 6 - вывод имен \n \
7 - поменять запись в базе \n 8 - удалить запись из базы \n 0 - выход\n"))
    return ask


def input_man():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    surname = input("Введите отчество: ")
    birthdate = input("Введите дату рождения: ")
    phone_num = input("Введите телефон: ")
    data = last_name + "; " + first_name + "; " + surname + \
        "; " + birthdate + "; " + phone_num + "; " + "\n"
    return data.lower()


def search_man():
    text_search = input(
        "Введите ключ для поиска: ").lower()
    return text_search


'''Если разбили с помощью сплит, то либо сначала сделайте из списка строку с помощью метода join() 
(гляньте в интернете принцип работы), либо можете проходиться циклом по списку и писать каждый элемент отдельно 
с помощью write и формата открытия файла "a"'''


def change_man():
    print(database.open_data())
    p = database.open_data()
    man_number = int(input("Введите номер записи: "))
    p.pop(man_number).strip("\n").split(", ")
    data = str(p) + input_man()
    return data


def del_man():
    print(database.open_data())
    p = database.open_data()
    man_number = int(input("Введите номер записи: "))
    p.pop(man_number).strip("\n").split(", ")
    data = str(p)
    return data
