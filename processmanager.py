import numpy as np
import process


class Processmanager():
    # only 1 process
    def __init__(self, memlimit):
        self.memlimit = memlimit
        self.proc = []
        # var = np.random.poisson(0.1,1000000)
        # print(min(var))
        # print(sum(var)/len(var))
        # print(max(var))

    def create_process(self):
        self.proc.append(process.Process(self.memlimit))
