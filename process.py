import numpy as np
import random


class Process():
    def __init__(self, memlimit):
        self.memlimit = memlimit
        self.adress = []
        magicnumber = 2
        # big - 2, medium - 4, small - 8
        adresscount = round(np.random.normal(self.memlimit / magicnumber, self.memlimit / (magicnumber * 6)))
        medium = random.randint(self.memlimit // (magicnumber * 4), self.memlimit - (self.memlimit // (magicnumber * 4)))
        for _ in range(adresscount):
            self.adress.append(round(np.random.normal(medium, self.memlimit / (magicnumber * 4 * 6))))

    def returnadressstat(self):
        print("adress count ", len(self.adress))
        print("min adress ", min(self.adress))
        print("max adress ", max(self.adress))
        print("average ", sum(self.adress)/len(self.adress))

    def popadress(self):
        return self.adress.pop()