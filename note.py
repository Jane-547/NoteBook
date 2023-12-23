import json


class Note(object):

    def __init__(self, note_id, title, body, timestamp):
        self._note_id = note_id
        self._title = title
        self._body = body
        self._timestamp = timestamp

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    @property
    def note_id(self):
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        self._note_id = note_id

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    def __str__(self):
        return f'\nId заметки: {self.note_id}\nЗаголовок: {self.title}\nТекст: {self.body}\n' \
               f'Дата последнего изменения:{self.timestamp}\n'

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
