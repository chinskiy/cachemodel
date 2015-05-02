import random
import sqlite3


class Datastorage():
    def __init__(self):
        self.conn = sqlite3.connect('Datastorage.db')
        self.cursor = self.conn.cursor()

    def createstorage(self):
        self.cursor.execute('CREATE TABLE Datastorage (ID INTEGER PRIMARY KEY AUTOINCREMENT, DATA TEXT)')
        self.conn.commit()

    def makedata(self, length):
        f = lambda: ''.join([random.choice('0123456789ABCDEF') for _ in range(4)])
        for i in range(length):
            self.cursor.execute("INSERT INTO Datastorage(DATA)  VALUES('" + f() + "')")
        self.conn.commit()
        print(self.returnstoragelen())

    def printstorage(self):
        for _ in self.cursor.execute('SELECT * FROM Datastorage'):
            print(_[0], "  ", _[1])

    def returndata(self, adress):
        return self.cursor.execute('SELECT * FROM Datastorage WHERE ID=' + str(adress) + ' ').fetchall()[0]

    def printstoragestat(self):
        self.cursor.execute('SELECT * FROM Datastorage')
        print("cols: ", end="")
        for colinfo in self.cursor.description:
            print(colinfo, end=" ")
        print("")
        self.cursor.execute('SELECT COUNT(*) FROM Datastorage')
        print("dblen: ", self.cursor.fetchall()[0][0])

    def returnstoragelen(self):
        self.cursor.execute('SELECT COUNT(*) FROM Datastorage')
        return self.cursor.fetchall()[0][0]

    def dropstorage(self):
        self.cursor.execute('Drop TABLE IF EXISTS Datastorage')
        self.conn.commit()

    def __del__(self):
        self.conn.close()