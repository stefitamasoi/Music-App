class StatisticsService:

    def __init__(self, song_repository, listener_repository):
        self._song_repository = song_repository
        self._listener_repository = listener_repository

    def average_age_of_listeners(self):
        """
        Calculates the average age of all listeners
        :return: (int) average age
         """
        listener_list = self._listener_repository.get_all()
        sum = 0
        for listener in listener_list:
            sum += int(listener.get_age())
        return str(sum / len(listener_list))

    def average_song_duration(self):
        """
        Calculates the average duration in seconds
        :return: (int) average duration
        """
        songs_list = self._song_repository.get_all()
        sum = 0
        for song in songs_list:
            sum += int(song.get_duration())
        return str(sum / len(songs_list))

    def __has_got_listener(self, song_title):
        """
        Checks if a song has listener or not
        :param song_title: Song title
        :return: True if it has, false otherwise
        """
        for listener in self._listener_repository.get_all():
            if listener.get_song() == song_title:
                return True
        return False

    def get_songs_without_listener(self):
        """
        Returns the list of songs that has no listener
        :return: [list] songs without listener
        """
        songs_list = self._song_repository.get_all()
        no_listener_list = []
        for song in songs_list:
            if not self.__has_got_listener(song.get_title()):
                no_listener_list.append(song)
        return no_listener_list

    def most_popular_genre(self):
        """
        Determinate the genre that is the most listened to
        :return: the most popular genre
        """
        playlist = []
        most_popular = []
        for song in self._song_repository.get_all():
            OK = 0
            for i in range(len(playlist)):
                if song.get_genre() == playlist[i]:
                    most_popular[i] += 1
                    OK = i
                    break

            if OK == 0:
                playlist.append(song.get_genre())
                most_popular.append(1)

        most = 0
        pos_max = 0
        for i in range(len(most_popular)):
            if most_popular[i] > most:
                most = most_popular[i]
                pos_max = i
        return playlist[pos_max]

    def listeners_with_song_after_update(self, title, new_id, id):
        """
        What listener has a song after update
        :param id: id of the song
        :param new_id: new id of the song
        :param title: the new title after update
        """

        for listener in self._listener_repository.get_all():
            if listener.get_song_id() == id:
                listener.set_song(title)
                listener.set_song_id(new_id)
                break

    def songs_with_listener_after_update(self, listener_id):
        """
        What songs have a listener by his ID
        :param listener_id: ID of the listener
        :return: the song ID
        """
        for listener in self._listener_repository.get_all():
            if listener.get_id() == listener_id:
                return listener.get_song_id()
