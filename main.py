import datastorage
import cachestorage
import process
import processmanager
import process

#db.makedata(1005508)
#8 * 1024 * 128
db = datastorage.Datastorage()
#db.printstoragestat()

cm = cachestorage.Cachemem(6)
cm.addmem(4, db.returndata(5))
cm.addmemfromds(4, 5)
cm.printmem()
print(cm.findindexaddr(3))


# prmngr = processmanager.Processmanager(db.returnstoragelen(), 'lru', 128)
# prmngr.makestep()

