# python-database
This all python file to use in connections with many databases.

## USAGE
### Microsoft SQL Server 

```python
from msssql import koneksi

konek = koneksi("yourserver", "yourdatabase", "yourUID", "yourPASS")
conn = konek.Hubungan()
cursor = conn.cursor()

cursor.execute("Select Getdate()")
resultset = cursor.fetchall()
for row in resultset:
    print row
    
```    
