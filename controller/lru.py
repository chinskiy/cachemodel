import cachestorage


class LRU():
    def __init__(self, lencache):
        self.cachestorage = cachestorage.Cachemem(lencache)
        self.start, self.lencache = 0, lencache
        self.cachefreq = [0 for _ in range(lencache)]

    def makestep(self, adress):
        index = self.cachestorage.findindexaddr(adress)
        if self.start < self.lencache:
            if index == -1:
                self.cachestorage.addmemfromds(self.start, adress)
                self.cachefreq[self.start] = 0
                for _ in range(self.start):
                    self.cachefreq[_] += 1
                self.start += 1
                return 0
            else:
                for _ in range(self.start):
                    self.cachefreq[_] += 1
                self.cachefreq[index] = 0
                return 1
        else:
            if index == -1:
                self.cachestorage.addmemfromds(self.cachefreq.index(max(self.cachefreq)), adress)
                self.cachefreq = [self.cachefreq[_] + 1 for _ in range(len(self.cachefreq))]
                self.cachefreq[self.cachefreq.index(max(self.cachefreq))] = 0
                return 0
            else:
                self.cachefreq = [self.cachefreq[_] + 1 for _ in range(len(self.cachefreq))]
                self.cachefreq[index] = 0
                return 1