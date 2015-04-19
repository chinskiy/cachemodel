class Cachemem():
    def __init__(self, len):
        self.mem1 = [[[_], [0] * 2] for _ in range(len)]

    def addmem(self, index, adress):
        self.mem1[index][1] = [adress['id'], adress['data']]

    def printmem(self):
        print(self.mem1)
        for _ in range(len(self.mem1)):
            for __ in range(len(self.mem1[1])):
                print(self.mem1[_][__], end='  ')
            print('')

    def popmem(self, index):
        self.mem1[index][1] = [0, 0]