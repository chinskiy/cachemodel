import cachestorage


class LRU():
    def __init__(self, lencache):
        self.cachestorage = cachestorage.Cachemem(lencache)
        self.start, self.lencache = 0, lencache

    def makestep(self, adress):
        pass