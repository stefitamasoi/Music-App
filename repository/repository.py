class Repository:

    def __init__(self):
        self._entitieslist = []

    def find_position(self, entity):
        """
        Returns the position of an entity
        :param entity: given entity
        :return: the position of the entity in the list, -1 if not found
        """
        for pos in range(len(self._entitieslist)):
            if self._entitieslist[pos] == entity:
                return pos
        return -1

    def add(self, entity):
        """
        Adds an entity to the list
        :raise: Exception if it already exists
        :param entity: given entity
        """
        if self.find_position(entity) != -1:
            raise Exception("Already exists!")
        self._entitieslist.append(entity)

    def delete(self, entity):
        """
        Deletes an entity from the list
        :raise: Exception if the entity does not exist
        :param entity: given entity
        """
        position = self.find_position(entity)
        if position == -1:
            raise Exception("Does not exist!")
        del self._entitieslist[position]

    def get_all(self):
        """
        Returns all the entities
        :return: All the entities
        """
        return self._entitieslist
