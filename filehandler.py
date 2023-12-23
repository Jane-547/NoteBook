import json
import os
from datetime import datetime

from NoteBook.note import Note


class FileHandler:

    def __init__(self):
        self.notes_file = "notes.json"

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as file:
                notes_data = json.load(file)

            notes = []
            for note_id, note_dict in notes_data.items():
                timestamp = datetime.fromisoformat(note_dict["_timestamp"])
                note = Note(note_dict["_note_id"], note_dict["_title"], note_dict["_body"], timestamp)
                notes.append(note)

            sorted_notes = sorted(notes, key=lambda x: x.timestamp)
            return sorted_notes
        else:
            return []

    def save_notes(self, notes):
        notes_data = {}
        for note in notes:
            timestamp_str = note.timestamp.isoformat()
            note_data = {
                "_note_id": note.note_id,
                "_title": note.title,
                "_body": note.body,
                "_timestamp": timestamp_str
            }
            notes_data[str(note.note_id)] = note_data

        with open(self.notes_file, 'w') as file:
            json.dump(notes_data, file, indent=4)
