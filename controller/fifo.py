import cachestorage


class FIFO:
    def __init__(self, lencache):
        self.cachestorage = cachestorage.Cachemem(lencache)
        self.lencache = lencache
        self.iter = 0

    def makestep(self, adress):
        index = self.cachestorage.findindexaddr(adress)
        if index == -1:
            self.cachestorage.addmemfromds(self.iter, adress)
            self.iter = (self.iter + 1) % self.lencache
            return 0
        else:
            return 1
