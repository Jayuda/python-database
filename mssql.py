import pyodbc

class MSSQL:
    def __init__(self, sServer, sPort, sDatabase, sUser, sPass):
        self.sServer = sServer
        self.sPort = sPort
        self.sDatabase = sDatabase
        self.sUser = sUser
        self.sPass = sPass

    def conn(self):
        try:
            print "Try to connecting MSSQL Server. . ."
            conn = pyodbc.connect(
                driver='/usr/local/Cellar/freetds/0.95.80/lib/libtdsodbc.so',  # Change with your libtds locations
                TDS_Version='7.0',
                server=self.sServer,
                port=self.sPort,
                database=self.sDatabase,
                uid=self.sUser,
                pwd=self.sPass)
        except Exception as ex:
            print "Error:", ex
            exit('Failed to connect, terminating.')

        return conn

    def select(self, oCollections, oWhere, oOptions):
        return oCollections.find(oWhere, oOptions)


    def select(self, sQuery):
        conMSSQL = MSSQL(self.sServer, self.sPort, self.sDatabase, self.sUser, self.sPass)
        conn = conMSSQL.conn()
        cursor = conn.cursor()
        cursor.execute(sQuery)
        resultset = cursor.fetchall()

        return resultset

    def getColumn(self, sTable):
        conMSSQL = MSSQL(self.sServer, self.sPort, self.sDatabase, self.sUser, self.sPass)
        conn = conMSSQL.conn()
        cursor = conn.cursor()

        sSQL =  "Select A.Name " \
                "From pondasi.sys.columns A " \
                "JOIN pondasi.sys.objects B On A.object_id = B.Object_id " \
                "Where B.Name = '%s'" % sTable

        cursor.execute(sSQL)
        resultset = cursor.fetchall()

        sKolom2 = ""
        for row in resultset:
            if sKolom2 == "":
                sKolom2 = "%s" % (row[0])
            else:
                sKolom2 = "%s, %s" % (sKolom2, row[0])
        return sKolom2
