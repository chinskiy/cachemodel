import dataset
import random


class Datastorage():
    def __init__(self):
        self.db = dataset.connect('sqlite:///Datastorage.db')
        self.memory = self.db['Datastorage']

    def makedata(self, length):
        f = lambda: ''.join([random.choice('0123456789ABCDEF') for _ in range(4)])
        for i in range(length):
            self.memory.insert({'data': f()})
    #        self.printstoragestat()

    def printstorage(self):
        for _ in self.memory:
            print(_['id'], "  ", _['data'])

    def returndata(self, adress):
        return self.memory.find_one(id=adress)

    def printstoragestat(self):
        print("cols: ", self.memory.columns)
        print("dblen: ", len(self.memory))

    def returnstoragelen(self):
        return len(self.memory)

    def dropstorage(self):
        self.memory.drop()