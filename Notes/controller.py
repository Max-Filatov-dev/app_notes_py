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
                resp_read_path = view.search_note(nt.path_note)
                view.show_note(path=resp_read_path) if resp_read_path else None
            case 3:
                print(f'\nSelect: {response}\n{"-" * 30}\n{text.main_menu[response]}')
                resp_new_note = view.data_new_note()
                if resp_new_note:
                    nt.add_note(data=resp_new_note)
                    nt.save_note()
                    print(text.true_note_add)
                else:
                    print(text.false_note_add)
            case 4:
                pass
            case 5:
                resp_del_path = view.search_note(path=nt.path_note)
                if resp_del_path:
                    nt.del_note(del_path=resp_del_path)
                    print(text.del_note)
            case 6:
                print(text.exit_msg)
                break
