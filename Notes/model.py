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
        cur_index = len([files[2] for files in os.walk(self.path_note)][0]) + 1
        self.note_data.update({
            'id': cur_index,
            'title': data[0],
            'content': data[1],
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    def edit_note(self, path_edit: str, data_edit: list):
        """ """
        pass

    def save_note(self):
        """ """
        self.path_note += f'{self.note_data.get("title", None)}.json'
        with open(self.path_note, 'w', encoding='utf-8') as pb:
            json.dump(self.note_data, pb, indent=4, ensure_ascii=False)
