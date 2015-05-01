import datastorage


class Cachemem():
    def __init__(self, len):
        self.mem = [[[_], [0] * 2] for _ in range(len)]
        self.ds = datastorage.Datastorage()

    def addmem(self, index, adress):
        self.mem[index][1] = [adress['id'], adress['data']]

    def addmemfromds(self, index, adress):
        data = self.ds.returndata(adress)
        self.mem[index][1] = [data['id'], data['data']]

    def printmem(self):
        for _ in range(len(self.mem)):
            for __ in range(len(self.mem[1])):
                print(self.mem[_][__], end='  ')
            print('')

    def popmem(self, index):
        self.mem[index][1] = [0, 0]

    def findindexaddr(self, adress):
        for _ in range(len(self.mem)):
            if self.mem[_][1][0] == adress:
                return _
        return -1