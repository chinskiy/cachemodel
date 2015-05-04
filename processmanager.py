import process
from controller import lru, mru, lfu, slru, fifo, rl


class Processmanager():
    # only 1 process
    def __init__(self, memlimit, controller, lencache):
        self.memlimit, self.lencache = memlimit, lencache
        self.proc = []
        try:
            self.controller = eval(controller + "." + controller.upper() + "(self.lencache)")
            self.create_process()
        except NameError:
            print("Wrong controller name")
            quit()

    def create_process(self):
        self.proc.append(process.Process(self.memlimit))

    def makestep(self):
        addr = self.proc[0].popadress()
        if addr == -1:
            self.proc.pop()
            self.create_process()
            addr = self.proc[0].popadress()
        return self.controller.makestep(addr)

    def setcountmakestepstat(self, count):
        cachehit = 0
        for _ in range(count):
            cachehit += self.makestep()
        print("Cachehit =", str(cachehit).rjust(7), str(round(cachehit * 100 / count, 2)).rjust(8) + "%")
        print("Cachemiss =", str(count - cachehit).rjust(7), str(round((count-cachehit) * 100/count, 2)).rjust(8) + "%")

    def setcountmakestephit(self, count):
        cachehit = 0
        for _ in range(count):
            cachehit += self.makestep()
        return cachehit