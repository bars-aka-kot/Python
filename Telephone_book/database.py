def add_data(data):
    with open("Telephone_book\database.txt", "a") as file:
        file.write(data)
        print("Запись внесена! \n")


def show_all():
    with open("Telephone_book\database.txt", "r") as file:
        print(file.read())


def show_name():
    with open("Telephone_book\database.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(i.split("; ")[1])


def search(text):
    with open("Telephone_book\database.txt", "r") as file:
        data = file.readlines()
        flag = False
        for i in data:
            if text in i:
                flag = True
                print(i)
            if flag == False:
                print("Нет данных. \n")


def sort_db_second_name():
    with open("Telephone_book\database.txt", "r") as file:
        data = file.readlines()
        data.sort()
    with open("Telephone_book\database.txt", "w") as file:
        file.writelines(data)
        print("Данные отсортированы по фамилии. \n")


def sort_db_phone_number():
    with open("Telephone_book\database.txt", "r") as file:
        data = file.readlines()
        data.sort(key=lambda x: (x[4]))
    with open("Telephone_book\database.txt", "w") as file:
        file.writelines(data)
        print(
            "Данные отсортированы по номеру телефона. \n")


def open_data():
    with open("Telephone_book\database.txt", "r") as file:
        text = file.readlines()
        return text


def add_new_data(data):
    with open("Telephone_book\database.txt", "w") as file:
        for i in data:
            file.writelines(i)
