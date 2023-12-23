import datetime

from NoteBook.model import Model
from NoteBook.view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()

    def add_note(self):
        title = self.view.add_new()
        body = self.view.add_body()
        timestamp = datetime.datetime.now()
        self.model.add_note(title, body, timestamp)
        self.view.ok()

    def edit_note(self):
        self.model.load_notes()
        search_id = self.view.get_id_from_user()
        flag = 0
        for item in self.model.notes:
            if item.note_id == search_id:
                flag = 1
                item.title = self.view.change_title()
                item.body = self.view.add_body()
                item.timestamp = datetime.datetime.now()
                self.model.write()
                self.view.ok()
        if flag == 0:
            self.view.not_found()

    def delete_note(self):
        self.model.load_notes()
        flag = 0
        search_id = self.view.get_id_from_user()
        for item in self.model.notes:
            if item.note_id == search_id:
                self.model.notes.remove(item)
                self.model.write()
                self.view.ok()
        if flag == 0:
            self.view.not_found()

    def show_by_date(self):
        self.model.load_notes()
        date = self.view.date_from_user()
        date_list = [note for note in self.model.notes if note.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f").startswith(date)]

        if date_list:
            self.view.show_notes(date_list)
        else:
            self.view.no_data_found()

    def show_all(self):
        self.model.load_notes()
        self.view.show_notes(self.model.notes)
