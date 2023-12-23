import datetime

from NoteBook import filehandler
from NoteBook.model import Model
from NoteBook.view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.model.notes = filehandler.load_notes()

    def add_note(self):
        title = self.view.add_new()
        body = self.view.add_body()
        timestamp = datetime.datetime.now().isoformat()
        self.model.add_note(title, body, timestamp)

    def edit_note(self):
        search_id = self.view.get_id_from_user()
        for item in self.model.notes:
            if item.note_id == search_id:
                item.title = self.view.change_title()
                item.body = self.view.add_body()
                item.timestamp = datetime.datetime.now().isoformat()
                self.model.write(self.model.notes)
                self.view.ok()
            else:
                self.view.not_found()

    def delete_note(self):
        search_id = self.view.get_id_from_user()
        for item in self.model.notes:
            if item.note_id == search_id:
                self.model.notes.remove(item)
                self.model.write(self.model.notes)
                self.view.ok()
            else:
                self.view.not_found()

    def show_by_date(self):
        date = self.view.date_from_user()
        date_list = [note for note in self.model.notes if note.timestamp.startswith(date)]
        if date_list:
            self.view.show_notes(date_list)
        else:
            self.view.no_data_found()

    def show_all(self):
        date_list = sorted(self.model.notes, key=lambda x: x.timestamp)
        self.view.show_notes(date_list)

