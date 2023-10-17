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
                print(f'\n{response} {"-" * 30}\n{text.main_menu[response]}')
                view.show_list_notes(path=nt.path_note)
            case 2:
                print(f'\n{response} {"-" * 30}\n{text.main_menu[response]}')
                resp_read_path = view.search_note(nt.path_note)
                view.show_note(path=resp_read_path) if resp_read_path else None
            case 3:
                print(f'\n{response} {"-" * 30}\n{text.main_menu[response]}')
                resp_new_note = view.new_note(path_new=nt.path_note)
                if resp_new_note and len(resp_new_note) >= 2:
                    nt.add_note(data=resp_new_note)
                    nt.save_note()
                    print(text.true_note_add)
                    break
                else:
                    print(text.false_note_add)
            case 4:
                print(f'\n{response} {"-" * 30}\n{text.main_menu[response]}')
                resp_edit_path = view.search_note(nt.path_note)
                if resp_edit_path:
                    resp_edit = view.edit_note_data()
                    nt.edit_note(path_edit=resp_edit_path, data_edit=resp_edit)
                    print(text.edit_note)
            case 5:
                resp_del_path = view.search_note(path=nt.path_note)
                if resp_del_path:
                    nt.del_note(del_path=resp_del_path)
                    print(text.del_note)
                    break
            case 6:
                print(text.exit_msg)
                break
