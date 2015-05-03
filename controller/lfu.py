import cachestorage
import random
import numpy as np


class LFU():
    def __init__(self, lencache):
        self.cachestorage = cachestorage.Cachemem(lencache)
        self.start, self.lencache = 0, lencache
        self.cachefreq = np.asarray([0 for _ in range(lencache)])

    def makestep(self, adress):
        index = self.cachestorage.findindexaddr(adress)
        if self.start < self.lencache:
            if index == -1:
                self.cachestorage.addmemfromds(self.start, adress)
                self.start += 1
                return 0
            else:
                self.cachefreq[index] += 1
                return 1
        else:
            if index == -1:
                ind = random.choice(np.where(self.cachefreq == np.min(self.cachefreq))[0])
                self.cachestorage.addmemfromds(ind, adress)
                self.cachefreq[ind] = 0
                return 0
            else:
                self.cachefreq[index] += 1
                return 1
