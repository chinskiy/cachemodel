import time
import processmanager


def testall(datastoragelen, cachelen, number):
    t1 = time.time()
    print("lru")
    prmngr1 = processmanager.Processmanager(datastoragelen, "lru", cachelen)
    prmngr1.setcountmakestep(number)
    print(time.time() - t1)

    t1 = time.time()
    print("mru")
    prmngr2 = processmanager.Processmanager(datastoragelen, "mru", cachelen)
    prmngr2.setcountmakestep(number)
    print(time.time() - t1)

    t1 = time.time()
    print("lfu")
    prmngr3 = processmanager.Processmanager(datastoragelen, "lfu", cachelen)
    prmngr3.setcountmakestep(number)
    print(time.time() - t1)

    t1 = time.time()
    print("fifo")
    prmngr4 = processmanager.Processmanager(datastoragelen, "fifo", cachelen)
    prmngr4.setcountmakestep(number)
    print(time.time() - t1)

cach = 1000
numb = 1000000
dstg = 1049576
testall(dstg, cach, numb)