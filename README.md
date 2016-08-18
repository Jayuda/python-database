# python-database
This all python file to use in connections with many databases.

## USAGE
### Microsoft SQL Server 
```python
from mssql import MSSQL

conMSSQL = MSSQL("SERVER", "PORT", "DATABASE", "USER", "PASSWORD")
conn = conMSSQL.conn()
cursor = conn.cursor()
resultset = conMSSQL.select("Select Getdate()")
for row in resultset:
    print row
    
```    

### MongoDB
```python
from mongodb import MONGODB

conMONGO = MONGODB("SERVER", "PORT", "DATABASE", "USER", "PASSWORD")
conn = conMONGO.conn()
db = conn.admin
collection = db.absen
resultset = conMONGO.select(collection, {"absenName" : "NURITA"}, {"absenName":1, "absenNIP" : 1})
for doc in resultset:
    print doc
    for key in doc.keys():
        print doc[key]
    
```    
