import cachestorage
import numpy as np


class LRU:
    def __init__(self, lencache):
        self.cachestorage = cachestorage.Cachemem(lencache)
        self.start, self.lencache = 0, lencache
        self.cacheused = np.asarray([0 for _ in range(lencache)])

    def makestep(self, adress, retmemid=0):
        index = self.cachestorage.findindexaddr(adress)
        if self.start < self.lencache:
            if index == -1:
                self.cachestorage.addmemfromds(self.start, adress)
                self.cacheused += 1
                self.cacheused[self.start] = 0
                self.start += 1
                return 0
            else:
                self.cacheused += 1
                self.cacheused[index] = 0
                return 1
        else:
            if index == -1:
                maxind = np.where(
                    self.cacheused == np.max(self.cacheused))[0][0]
                if retmemid == 0:
                    self.cachestorage.addmemfromds(maxind, adress)
                    self.cacheused += 1
                    self.cacheused[maxind] = 0
                    return 0
                else:
                    tmp = self.cachestorage.memid[maxind]
                    self.cachestorage.addmemfromds(maxind, adress)
                    self.cacheused += 1
                    self.cacheused[maxind] = 0
                    return tmp
            else:
                self.cacheused += 1
                self.cacheused[index] = 0
                return 1
