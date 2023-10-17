import json
import os
from datetime import datetime


class Note:
    """ """

    def __init__(self):
        """ Constructor """
        self.path_note = 'notes/'
        self.note_data = {}

    def add_note(self, data: list):
        """ """
        all_notes, cur_index = [files[2] for files in os.walk(self.path_note)][0], 1
        for item in all_notes:
            with open(self.path_note + item) as r:
                data_nt = json.load(r)
            cur_index += 1 if cur_index == data_nt['id'] else 0

        self.note_data.update({
            'id': cur_index,
            'title': data[0],
            'content': data[1],
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    def edit_note(self, path_edit: str, data_edit: str):
        """ """
        with open(path_edit) as rd:
            edit_data = json.load(rd)
        edit_data['content'] = data_edit

        with open(path_edit, 'w', encoding='utf-8') as wr:
            json.dump(edit_data, wr, indent=4)

    def del_note(self, del_path: str):
        """ """
        os.remove(del_path)

    def save_note(self):
        """ """
        self.path_note += f'{self.note_data.get("title", None)}.json'
        with open(self.path_note, 'w', encoding='utf-8') as pb:
            json.dump(self.note_data, pb, indent=4, ensure_ascii=False)
