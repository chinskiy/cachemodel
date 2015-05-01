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

    def makestep(self):
        self.controller.makestep(self.proc[0].popadress())