import view
import model
import text


def start():
    """ """
    while True:
        response = view.select_option()
        match response:
            case 1:
                print("Select 1")
                resp_new_note = view.data_new_note()
                if resp_new_note:
                    print(resp_new_note)
                else:
                    print(text.false_note)
            case 2:
                print("Select 2")
            case 3:
                print("Select 3")
            case 4:
                print("Select 4")

            case 5:
                print("Select 5")
            case 6:
                print(text.exit_msg)
                break
