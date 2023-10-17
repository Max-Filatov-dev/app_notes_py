import os
import json
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


def show_note(path: str):
    """ """
    with open(path) as rd:
        note_data = json.load(rd)
    (
        [print(f'{k:<10} {v}') for k, v in note_data.items()]
    )


def show_list_notes(path: str):
    """ """
    all_notes = [files[2] for files in os.walk(path)][0]
    (
        [print(f'{title[0]}. {title[1].replace(".json", "")}') for title in enumerate(all_notes, start=1)]
    )


def select_option():
    """ """
    while True:
        show_menu()
        select = input(text.select_action)
        if select.isdigit() and 0 < int(select) <= len(text.main_menu) - 1:
            return int(select)
        else:
            print(text.main_menu_input_error)


def new_note(path_new: str) -> list:
    """ """
    temp_data, all_notes = [], [files[2] for files in os.walk(path_new)][0]
    for item in text.fields_new_note:
        while True:
            data_in = check_data(input(item))
            if data_in == 'false':
                break
            elif f'{data_in}.json' in all_notes:
                print(text.note_double)
                return
            elif data_in:
                temp_data.append(data_in)
                break
            else:
                print(f'{"-" * 30}\nПоле не может быть пустым!\nДля выхода наберите false\n')

    return temp_data if temp_data else None


def search_note(path: str):
    """ """
    name = input(text.search_note)
    if not os.path.isfile(f'{path}{name}.json'):
        print(text.false_search_note)
    else:
        return f'{path}{name}.json'


def edit_note_data() -> str:
    """ """
    while True:
        edit = check_data(input(text.fields_new_note[1]))
        if edit == 'false':
            break
        elif edit:
            return edit
        else:
            print(f'{"-" * 30}\nПоле не может быть пустым!\nДля выхода наберите false\n')
