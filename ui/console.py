class UI:
    def __init__(self, song_service, listener_service, statistics_service):
        self.__song_service = song_service
        self.__listener_service = listener_service
        self.__statistics_service = statistics_service

    def __validate_age(self, age):
        """
        Checks if the age is an integer
        :param age: age of the listener
        :return: error if it is not an int
        """
        if type(age) != int:
            raise ValueError("Age must be an integer!")

    def print_all_songs(self):
        """
        Returns the list of all songs
        :return: songs list
        """
        print("Songs in console are: ")
        for song in self.__song_service.all_songs():
            print(song)

    def __add_song(self):
        """
        Adds a new song
        """
        title = input("Title: ")
        artist = input("Artist: ")
        genre = input("Genre: ")
        duration = input("Duration in seconds: ")
        id = title[0] + title[1] + title[2] + artist[0]
        self.__song_service.add_song(id, title, artist, genre, duration)
        print("Successfully added!")

    def delete_song(self):
        """
        Deletes a song by ID
        """
        id = input("ID od the song: ")
        self.__song_service.delete_song(id)
        print("Song was deleted successfully! ")

    def update_song(self):
        """
        Function that updates a song
        """
        id = input("ID of song that you want to change: ")
        self.__song_service.delete_song(id)
        print("Type the new values of your song!")
        title = input("Title: ")
        artist = input("Artist: ")
        genre = input("Genre: ")
        duration = input("Duration in seconds: ")
        new_id = title[0] + title[1] + title[2] + artist[0]
        self.__song_service.add_song(new_id, title, artist, genre, duration)
        self.__statistics_service.listeners_with_song_after_update(title, new_id, id)
        print("Song updated!")

    def print_all_listeners(self):
        """
        Returns all listeners
        :return: listeners list
        """
        print("Listeners: ")
        for listener in self.__listener_service.all_listeners():
            print(listener)

    def __add_listener(self):
        """
        Add a new listener
        """
        name = input("Name: ")
        age = input("Age: ")
        title = input("Song's title you want to listen: ")
        artist = input("Song's artist of the song you want to listen: ")
        genre = input("Song's genre of the song you want to listen: ")
        duration = input("Song's duration in seconds: ")
        id = name[0] + name[1] + str(age)
        self.__validate_age(int(age))
        self.__listener_service.add_listener(name, age, title, id)
        self.__song_service.add_song(id, title, artist, genre, duration)
        print("Listener was added successfully!")

    def __delete_listener(self):
        """
        Deletes a listener by name from
        """
        id = input("ID of listener you want to delete: ")
        self.__listener_service.delete_listener(id)
        print("Listener was deleted successfully!")

    def update_listener(self):
        """
        Function that updates a listener
        """
        id = input("ID od the listener that you want to change: ")
        old_song_id = self.__statistics_service.songs_with_listener_after_update(id)
        self.__listener_service.delete_listener(id)
        print("Type the new values of the listener")
        name = input("Name: ")
        age = input("Age: ")
        title = input("Song's title you want to listen: ")
        artist = input("Song's artist you want to listen: ")
        genre = input("Song's genre you want to listen: ")
        duration = input("Song's duration in seconds: ")
        self.__validate_age(int(age))
        song_id = title[0] + title[1] + title[2] + title[3] + artist[0]
        self.__listener_service.add_listener(name, age, title, song_id)
        self.__song_service.delete_song(old_song_id)
        self.__song_service.add_song(song_id, title, artist, genre, duration)
        print("Listener was updated successfully")

    def __print_average_age_of_listeners(self):
        """
        Returns the average age of all listeners
        """
        average_age = self.__statistics_service.average_age_of_listeners()
        print("Average age of all listeners is: {0} ".format(average_age))

    def __print_average_duration_of_songs(self):
        """
         Function that show the medium duration of music

        """
        average_duration = self.__statistics_service.average_song_duration()
        print("Average duration of all songs is: {0} ".format(average_duration))

    def __songs_without_listener(self):
        """
        Returns the songs which have no listener
        """
        no_listener_list = self.__statistics_service.get_songs_without_listener()
        print("Songs without listeners: ")
        for song in no_listener_list:
            print(song)

    def __most_popular_genre(self):
        """
        Shows the most popular genre
        """
        print(self.__statistics_service.most_popular_genre())

    def __most_popular_artist(self):
        """
        Shows the most popular artist
        """
        print(self.__statistics_service.most_popular_artist())

    def run(self):
        while True:
            print("Options:\n\n"
                  "1 - Add song\n"
                  "2 - Delete song\n"
                  "3 - Print all songs\n\n"
                  "4 - Add listener\n"
                  "5 - Delete listener\n"
                  "6 - Print all listeners\n\n"
                  "7 - Average age of all listeners\n"
                  "8 - Average duration of all songs\n"
                  "9 - Songs with no listener\n\n"
                  "10 - Update a song\n"
                  "11 - Update a listener\n\n"
                  "0 - Exit\n")
            command = input(">")
            try:
                if command == "0":
                    return
                if command == "1":
                    self.__add_song()
                if command == "2":
                    self.delete_song()
                if command == "3":
                    self.print_all_songs()
                if command == "4":
                    self.__add_listener()
                if command == "5":
                    self.__delete_listener()
                if command == "6":
                    self.print_all_listeners()
                if command == "7":
                    self.__print_average_age_of_listeners()
                if command == "8":
                    self.__print_average_duration_of_songs()
                if command == "9":
                    self.__songs_without_listener()
                if command == "10":
                    self.update_song()
                if command == "11":
                    self.update_listener()

            except Exception as ex:
                print("\n", ex)
