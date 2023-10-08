import text


def check_data(data: str):
    """ """
    return data if data.strip() else False


def show_menu():
    """ """
    return [
        print("\t", f"{num}. {val}") if num else print(text.main_menu[0])
        for num, val in enumerate(text.main_menu)
    ]


def select_option():
    """ """
    while True:
        show_menu()
        select = input(text.select_action)
        if select.isdigit() and 0 < int(select) <= len(text.main_menu) - 1:
            return int(select)
        else:
            print(text.main_menu_input_error)


def data_new_note() -> list:
    """ """
    temp_data = []
    for item in text.fields_new_note:
        while True:
            data_in = check_data(input(item))
            if data_in:
                temp_data.append(data_in)
                break
            else:
                print(f'{"-" * 30}\nПоле не может быть пустым!\n')

    return temp_data if temp_data else None
