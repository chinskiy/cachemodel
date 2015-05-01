import cachestorage


class MRU():
    def __init__(self, lencache):
        self.cachestorage = cachestorage.Cachemem(lencache)

    def makestep(self, adress):
        pass