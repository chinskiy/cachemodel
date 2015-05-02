import datastorage


class Cachemem():
    def __init__(self, length):
        self.len = length
        self.memid, self.memdata = [0 for _ in range(length)], [0 for _ in range(length)]
        self.ds = datastorage.Datastorage()

    def addmem(self, index, adress):
        self.memid[index], self.memdata[index] = adress['id'], adress['data']

    def addmemfromds(self, index, adress):
        data = self.ds.returndata(adress)
        self.memid[index], self.memdata[index] = data['id'], data['data']

    def printmem(self):
        for _ in range(self.len):
            print(_, "", self.memid[_], "", self.memdata[_])

    def popmem(self, index):
        self.memid[index], self.memdata[index] = 0, 0

    def findindexaddr(self, adress):
        try:
            return self.memid.index(adress)
        except ValueError:
            return -1