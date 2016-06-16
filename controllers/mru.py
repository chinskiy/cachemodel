from storages.cachestorage import Cachestorage


class MRU:
    def __init__(self, lencache):
        self.cachestorage = Cachestorage(lencache)
        self.start, self.lencache = 0, lencache
        self.lastadd = -1

    def makestep(self, adress):
        index = self.cachestorage.findindexaddr(adress)
        if self.start < self.lencache:
            if index == -1:
                self.cachestorage.addmemfromds(self.start, adress)
                self.lastadd = self.start
                self.start += 1
                return 0
            else:
                self.lastadd = index
                return 1
        else:
            if index == -1:
                self.cachestorage.addmemfromds(self.lastadd, adress)
                return 0
            else:
                self.lastadd = index
                return 1
