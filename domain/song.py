class Song:
    def __init__(self, id, title, artist, genre, duration):
        self._id = id
        self._title = title
        self._artist = artist
        self._genre = genre
        self._duration = duration

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        self._title = new_title

    def get_artist(self):
        return self._artist

    def set_artist(self, new_artist):
        self._artist = new_artist

    def get_genre(self):
        return self._genre

    def set_genre(self, new_genre):
        self._genre = new_genre

    def get_duration(self):
        return self._duration

    def set_duration(self, new_duration):
        self._duration = new_duration

    def __eq__(self, music):
        return self.get_id() == music.get_id()

    def __str__(self):
        return self._title + ", " + self._artist + ", " + self._genre + ", " + self._duration + ", " + str(self._id)
