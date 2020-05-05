from nonlinear.webapp.data_source.data_models.api_key_identity import ApiKeyIdentity
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

        # TODO create mongo database

    def generate_api_key(self):
        api_identity = ApiKeyIdentity(str(uuid.uuid4()), datetime.datetime.now(tz=datetime.timezone.utc))

        # TODO insert

        return api_identity.id

    def get_identity(self, api_key):
        raise NotImplementedError()
