import lru
import numpy as np


class SLRU:
    def __init__(self, lencache):
        self.segment = [lru.LRU(lencache // 2), lru.LRU(lencache // 2)]

    def makestep(self, adress):
        index = [self.segment[0].cachestorage.findindexaddr(adress),
                 self.segment[1].cachestorage.findindexaddr(adress)]

        if index[0] == -1:
            if index[1] == -1:
                self.segment[0].makestep(adress)
                return 0
            elif index[1] != -1:
                self.segment[1].makestep(adress)
                return 1
        elif index[0] != -1:
            if index[1] == -1:
                tmp = self.segment[1].makestep(adress, 1)
                self.segment[0].cachestorage.memid[index[0]] = tmp
                self.segment[0].cacheused += 1
                if tmp == 0:
                    self.segment[0].cacheused[index[0]] = np.max(
                        self.segment[0].cacheused) + 1
                else:
                    self.segment[0].cacheused[index[0]] = 0
                return 1
