from sqlite_utils import Database

#```
db = Database('data/sample.db')
db['Table1'].create({"id":int,"name":str},pk='id')
db['Table2'].create({"id":int,"text":str,"created_by":int},pk='id'
                    ,foreign_keys=[('created_by','Table1','id')])
# ```
# But the below piece works
# ```
# db['Table1'].create(id=int,name=str,pk='int')
# db['Table2'].create(id=int,text=str,created_by=int,pk='id')
# db['Table2'].add_foreign_key('created_by','Table1','id')
# ```
