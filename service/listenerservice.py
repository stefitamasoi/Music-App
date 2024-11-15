from domain.listener import Listener


class ListenerService:
    def __init__(self, listener_repository):
        self._listener_repository = listener_repository
        self._listener_repository.add(Listener("St17", "Stefania", "17", "Nothing Else Matters", "NotM"))
        self._listener_repository.add(Listener("Ca19", "Carla", "19", "Toxicity", "ToxS"))
        self._listener_repository.add(Listener("An27", "Ana", "27", "Why", "WhyN"))
        self._listener_repository.add(Listener("El30", "Elena", "30", "", ""))

    def add_listener(self, name, age, song, song_id):
        """
        Adds a listener
        :param name: name of the listener
        :param age: age of the listener
        :param song: songs to he/she listens
        :param song_id: id of the song he/she listens
        """
        id = name[0] + name[1] + str(age)
        self._listener_repository.add(Listener(id, name, age, song, song_id))

    def delete_listener(self, id):
        """
        Deletes a listener by id
        :param id: id of the listener you want to delete
        """
        self._listener_repository.delete(Listener(id, "", 0, "", ""))

    def all_listeners(self):
        """
        Returns all listeners
        :return: list of all listeners
        """
        return self._listener_repository.get_all()
