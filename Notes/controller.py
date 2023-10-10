import view
import model
import text


def start():
    """ """
    nt = model.Note()
    while True:
        response = view.select_option()
        match response:
            case 1:
                print(f'\nSelect: {response}\n{"-" * 30}\n{text.main_menu[response]}')
                view.show_list_notes(path=nt.path_note)
            case 2:
                print(f'\nSelect: {response}\n{"-" * 30}\n{text.main_menu[response]}')
                resp_search = view.search_note(nt.path_note)
                view.show_note(path=resp_search) if resp_search else None
            case 3:
                print(f'\nSelect: {response}\n{"-" * 30}\n{text.main_menu[response]}')
                resp_new_note = view.data_new_note()
                if resp_new_note:
                    nt.add_note(data=resp_new_note)
                    nt.save_note()
                    print(text.true_note)
                else:
                    print(text.false_note)
            case 4:
                pass
            case 5:
                pass
            case 6:
                print(text.exit_msg)
                break
