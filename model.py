from NoteBook import filehandler
from NoteBook.note import Note


class Model:

    def __init__(self):
        self.notes = list()

    def add_note(self, title, body, timestamp):
        last = 0
        for i in self.notes:
            if i.note_id > last:
                last = i.note_id
        note_id = last + 1
        note = Note(note_id, title, body, timestamp)
        self.notes.append(note)
        self.write()

    def write(self):
        filehandler.save_notes(self.notes)


