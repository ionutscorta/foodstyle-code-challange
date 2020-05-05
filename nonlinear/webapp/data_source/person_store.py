from nonlinear.webapp.data_source.mongo_client import MongoClient


class PersonStore:
    # Singleton pattern
    _Instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if PersonStore._Instance is None:
            PersonStore()
        return PersonStore._Instance

    def __init__(self):
        """ Virtually private constructor. """
        if PersonStore._Instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PersonStore._Instance = self

        self.mongo_client = MongoClient(host="mongodb://localhost:27017/", db_name="DataStore", collection="Persons")

    def insert_person(self, person):
        return self.mongo_client.insert(person)

    def get_person(self, person_id):
        person = self.mongo_client.get({"id": person_id})
        if person is not None:
            return person
        else:
            raise Exception("Invalid person ID.")
