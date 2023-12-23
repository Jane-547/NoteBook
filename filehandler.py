import json
import os

notes_file = "notes.json"


def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, 'r') as file:
            notes = json.load(file)
        return notes
    else:
        return {}


def save_notes(notes):
    with open(notes_file, 'w') as file:
        json.dump(notes, file, indent=4)
