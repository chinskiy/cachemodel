import datastorage
import cachestorage
import process
import processmanager
import process

db = datastorage.Datastorage()
#db.makedata(1005508)
#8 * 1024 * 128
#db.printstoragestat()
#print(db.returndata(3))
#
# cm = cachestorage.Cachemem(5)
# cm.addmem(3, db.returndata(3))
#
# cm.printmem()

prmngr = processmanager.Processmanager(db.returnstoragelen())
prmngr.create_process()
print(prmngr.memlimit)
prmngr.proc[0].returnadressstat()

# proc = process.Process(db.returnstoragelen())
# proc.returnadressstat()