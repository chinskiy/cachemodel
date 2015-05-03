import datastorage
import time
import processmanager


def testall(cach, numb):
    t1 = time.time()
    print("lru")
    prmngr1 = processmanager.Processmanager(dstg, "lru", cach)
    prmngr1.setcountmakestep(numb)
    print(time.time() - t1)

    t1 = time.time()
    print("mru")
    prmngr2 = processmanager.Processmanager(dstg, "mru", cach)
    prmngr2.setcountmakestep(numb)
    print(time.time() - t1)

    t1 = time.time()
    print("lfu")
    prmngr3 = processmanager.Processmanager(dstg, "lfu", cach)
    prmngr3.setcountmakestep(numb)
    print(time.time() - t1)

    t1 = time.time()
    print("fifo")
    prmngr4 = processmanager.Processmanager(dstg, "fifo", cach)
    prmngr4.setcountmakestep(numb)
    print(time.time() - t1)


# 8 * 1024 * 128
db = datastorage.Datastorage()
# db.printstoragestat()

cach = 1000
numb = 1000000
dstg = 100000000
testall(cach, numb)