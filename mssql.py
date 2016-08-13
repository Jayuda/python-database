import pyodbc

class koneksi:
    def __init__(self, sServer, sDatabase, sUser, sPass):
        self.sServer = sServer
        self.sDatabase = sDatabase
        self.sUser = sUser
        self.sPass = sPass

    def Hubungan(self):
        return pyodbc.connect(
            driver='/usr/local/Cellar/freetds/0.95.80/lib/libtdsodbc.so', # Change with your libtds locations
            TDS_Version='7.0',
            server=self.sServer,
            port=1433,
            database=self.sDatabase,
            uid=self.sUser,
            pwd=self.sPass)
