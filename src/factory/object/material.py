
class Material:
    def __init__(self, id, name, storage=0, max_store=0, extra_store=0):
        self.id = id
        self.name = name
        self.storage = storage
        self.max_storage = max_store
        self.extra_storage = 0
        self.max_extra_storage = extra_store

    def __repr__(self):
        return ("")

    def