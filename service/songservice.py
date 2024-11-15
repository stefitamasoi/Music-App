from domain.song import Song


class SongService:

    def __init__(self, song_repository):
        self._song_repository = song_repository
        self._song_repository.add(Song("NotM", "Nothing Else Matters", "Metallica", "Metal", "212626"))
        self._song_repository.add(Song("ToxS", "Toxicity", "System of a down", "Heavy Metal", "10800"))
        self._song_repository.add(Song("WhyN", "Why", "NF", "Rap", "10812"))
        self._song_repository.add(Song("MedE", "Meditate", "EARTHGANG", "Hip hop", "14401"))

    def add_song(self, id, title, artist, genre, duration):
        """
        Adds a new song to the list
        :param id: id of the song
        :param title: title of the song
        :param artist: artist of the song
        :param genre: genre of the song
        :param duration: duration of the song
        """
        self._song_repository.add(Song(id, title, artist, genre, duration))

    def delete_song(self, id):
        """
        Deletes a song
        :param id: id of the song you want to delete
        """
        self._song_repository.delete(Song(id, "", "", "", 0))

    def all_songs(self):
        """
        Returns all songs in the list
        :return: Songs list
        """
        return self._song_repository.get_all()
