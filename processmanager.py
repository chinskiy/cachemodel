import process
from controller import lru, mru


class Processmanager():
    # only 1 process
    def __init__(self, memlimit, controller, lencache):
        self.memlimit = memlimit
        self.proc = []
        if controller == "lru":
            self.controller = lru.LRU(lencache)
        elif controller == "mru":
            self.controller = mru.MRU(lencache)
        else:
            print("Choose alg")
        self.create_process()

    def create_process(self):
        self.proc.append(process.Process(self.memlimit))
        print("new proc")

    def makestep(self):
        addr = self.proc[0].popadress()
        if addr == -1:
            self.proc.pop()
            self.create_process()
            addr = self.proc[0].popadress()
        return self.controller.makestep(addr)

    def setcountmakestep(self, count):
        cachehit = 0
        for _ in range(count):
            cachehit += self.makestep()
        print("Cachehit =", str(cachehit).rjust(7), str(round(cachehit * 100 / count, 2)).rjust(8) + "%")
        print("Cachemiss =", str(count - cachehit).rjust(6))