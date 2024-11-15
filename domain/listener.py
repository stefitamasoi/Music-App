class Listener:
    def __init__(self, id, name, age, song, song_id):
        self._id = id
        self._name = name
        self._age = age
        self._song = song
        self._song_id = song_id

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    def get_song(self):
        return self._song

    def set_song(self, new_song):
        self._song = new_song

    def get_song_id(self):
        return self._song_id

    def set_song_id(self, new_song_id):
        self._song_id = new_song_id

    def __eq__(self, listener):
        return self.get_id() == listener.get_id()

    def __repr__(self):
        return self._name + " " + str(self._age) + " " + self._song + " " + self._id

    def __str__(self):
        return self._name + ", " + str(self._age) + ", " + self._song + ",6 " + self._id
