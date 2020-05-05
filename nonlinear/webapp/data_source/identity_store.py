from nonlinear.webapp.data_source.data_models.api_key_identity import ApiKeyIdentity
from nonlinear.webapp.data_source.mongo_client import MongoClient
import uuid
import datetime


class IdentityStore:
    # Singleton pattern
    _Instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if IdentityStore._Instance is None:
            IdentityStore()
        return IdentityStore._Instance

    def __init__(self):
        """ Virtually private constructor. """
        if IdentityStore._Instance is not None:
            raise Exception("This class is a singleton!")
        else:
            IdentityStore._Instance = self

        self.mongo_client = MongoClient(host="mongodb://localhost:27017/", db_name="DataStore", collection="Identity")

    def generate_api_key(self):
        api_identity = ApiKeyIdentity(str(uuid.uuid4()), datetime.datetime.now(tz=datetime.timezone.utc))

        self.mongo_client.insert(api_identity)

        return api_identity.id

    def get_identity(self, api_key):
        identity = self.mongo_client.get({"id": api_key})
        if identity is not None:
            return ApiKeyIdentity(identity['id'], identity_datetime=identity['identity_datetime'])
