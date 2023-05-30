import view
import database


def main():
    while True:
        ask = view.user_input()
        if ask == 1:
            data = view.input_man()
            database.add_data(data)
        elif ask == 2:
            text = view.search_man()
            database.search(text)
        elif ask == 3:
            database.sort_db_second_name()
        elif ask == 4:
            database.sort_db_phone_number()
        elif ask == 5:
            database.show_all()
        elif ask == 6:
            database.show_name()
        elif ask == 7:
            new_data = view.change_man()
            database.add_new_data(new_data)
            print("Запись изменена! \n")
        elif ask == 8:
            new_data = view.del_man()
            database.add_new_data(new_data)
            print("Запись удалена! \n")
        elif ask == 0:
            break


main()
