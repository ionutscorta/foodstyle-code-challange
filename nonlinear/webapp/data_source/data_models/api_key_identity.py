class ApiKeyIdentity(dict):
    def __init__(self, id, identity_datetime):
        dict.__init__(self, id=id, identity_datetime=identity_datetime)

        self.id = id
        self.identity_datetime = identity_datetime
