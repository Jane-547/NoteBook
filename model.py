from NoteBook import filehandler
from NoteBook.note import Note


class Model:

    def __init__(self):
        self.fh = filehandler.FileHandler()
        self.notes = []

    def add_note(self, title, body, timestamp):
        self.load_notes()
        last = 0
        for i in self.notes:
            if i.note_id > last:
                last = i.note_id
        note_id = last + 1
        note = Note(note_id, title, body, timestamp)
        self.notes.append(note)
        self.write()

    def write(self):
        self.fh.save_notes(self.notes)

    def load_notes(self):
        self.notes = self.fh.load_notes()
