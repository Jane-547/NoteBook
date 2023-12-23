class Note:

    def __init__(self, note_id, title, body, timestamp):
        self._note_id = note_id
        self._title = title
        self._body = body
        self._timestamp = timestamp
        self._notes = []

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
        return f'\nId заметки: {self._note_id}\nЗаголовок: {self._title}\nТекст: {self._body}\n' \
               f'Дата последнего изменения:{self._timestamp}\n'

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self._notes):
            raise StopIteration
        value = self._notes[self.index]
        self.index += 1
        return value
