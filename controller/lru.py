import cachestorage


class LRU():
    def __init__(self, lencache):
        self.cachestorage = cachestorage.Cachemem(lencache)
        self.start, self.lencache = 0, lencache
        self.cacheused = [0 for _ in range(lencache)]

    def makestep(self, adress):
        index = self.cachestorage.findindexaddr(adress)
        if self.start < self.lencache:
            if index == -1:
                self.cachestorage.addmemfromds(self.start, adress)
                for _ in range(self.start):
                    self.cacheused[_] += 1
                self.start += 1
                return 0
            else:
                for _ in range(self.start):
                    self.cacheused[_] += 1
                self.cacheused[index] = 0
                return 1
        else:
            if index == -1:
                self.cachestorage.addmemfromds(self.cacheused.index(max(self.cacheused)), adress)
                self.cacheused = [self.cacheused[_] + 1 for _ in range(len(self.cacheused))]
                self.cacheused[self.cacheused.index(max(self.cacheused))] = 0
                return 0
            else:
                self.cacheused = [self.cacheused[_] + 1 for _ in range(len(self.cacheused))]
                self.cacheused[index] = 0
                return 1