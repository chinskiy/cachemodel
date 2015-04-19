import datastorage
import cachestorage

# ds = sqlite3.connect("data")
# sql = 'create table if not exists ' + "qq" + ' (id integer)'
# ds.execute(sql)
#
# ds.close()


# import dataset
#
# db = dataset.connect('sqlite:///Datastorage.db')
#
# table = db['sometable']
# table.insert({'name':'John Doe', 'age':37})
# table.insert(dict(name='John Doe1', age=36))
# table.insert(dict(name='Jane Doe', age=34, gender='female'))
#
# john = table.find_one(name='John Doe')
# print(john)
# print(john['id'], " ", john['name'])
# # al = table.find()
# # print(al['id'][0])
# for user in db['sometable']:
#    print(user['id'], "  ", user['age'])
#
# table.drop()

db = datastorage.Datastorage()
# db.makedata(884)
# db.printstorage()
print(db.returndata(3))

cm = cachestorage.Cachemem(5)
cm.addmem(3, db.returndata(3))

cm.printmem()