class SongRepository:

    def __init__(self):
        self._songsList = []

    def find_position(self, song):
        """
        Returns the position of a song
        :param song: given song by title
        :return: position of song, -1 if it is not found
        """
        for posSong in range(len(self._songsList)):
            if self._songsList[posSong] == song:
                return posSong
        return -1

    def add(self, title):
        """
        Adds a song to the list
        :param title: the title of the song we want to add
        :raise exception: if song already exists
        """
        if self.find_position(title) != -1:
            raise Exception("This song already exists!")
        self._songsList.append(title)

    def delete(self, title):
        """
        Deletes a given song
        :param title: the title of a certain song we want to delete
        :raise exception: if song does not exists
        """
        position = self.find_position(title)
        if position == -1:
            raise Exception("This song does not exist!")
        del self._songsList[position]

    def get_all(self):
        """
        Returns the list of songs
        :return: (list) list of songs
        """
        return self._songsList
