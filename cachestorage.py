import datastorage
import numpy as np


class Cachemem():
    def __init__(self, length):
        self.len = length
        self.memid = np.asarray([0 for _ in range(length)], dtype=np.int)
        self.ds = datastorage.Datastorage()

    def addmem(self, index, adress):
        self.memid[index] = adress['id']

    def addmemfromds(self, index, adress):
        data = self.ds.returndata(adress)
        self.memid[index] = data[0]

    def printmem(self):
        for _ in range(self.len):
            print(_, "", self.memid[_])

    def popmem(self, index):
        self.memid[index] = 0

    def findindexaddr(self, adress):
        res = np.where(self.memid == adress)[0]
        return res[0] if len(res) != 0 else -1