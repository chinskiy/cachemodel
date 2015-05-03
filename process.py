import numpy as np
import matplotlib.pyplot as plt
import random


class Process():
    def __init__(self, memlimit):
        random.seed(1)
        np.random.seed(1)
        self.memlimit = memlimit
        self.adress = []
        magicnumber = 8
        # big - 2, medium - 4, small - 8
        adresscount = round(np.random.normal(self.memlimit / magicnumber, self.memlimit / (magicnumber * 6)))
        medium = random.randint(self.memlimit // (magicnumber * 4),
                                self.memlimit - (self.memlimit // (magicnumber * 4)))
        for _ in range(adresscount):
            self.adress.append(round(np.random.normal(medium, self.memlimit / (magicnumber * 4 * 6))))

    def returnadressstat(self):
        print("adress count ", len(self.adress))
        print("min adress ", min(self.adress))
        print("max adress ", max(self.adress))
        print("average ", round(sum(self.adress) / len(self.adress)))

    def plotprocesshist(self):
        plt.hist(self.adress, bins=self.memlimit / 100, range=(0, self.memlimit))
        plt.show()

    def popadress(self):
        try:
            return self.adress.pop()
        except IndexError:
            return -1