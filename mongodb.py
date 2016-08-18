import pymongo

class MONGODB:
    def __init__(self, sServer, sPort, sDatabase, sUser, sPass):
        self.sServer = sServer
        self.sPort = sPort
        self.sDatabase = sDatabase
        self.sUser = sUser
        self.sPass = sPass
        self.settings = {
            'host': sServer,
            'port' : sPort,
            'database': sDatabase,
            'username': sUser,
            'password': sPass,
            'options': 'w=1'
        }

    def conn(self):
        try:
            print "Try to connecting MongoDB Server. . ."
            conn = pymongo.MongoClient("mongodb://{username}:{password}@{host}:{port}/{database}".format(**self.settings))
        except Exception as ex:
            print "Error:", ex
            exit('Failed to connect, terminating.')

        return conn

    def select(self, oCollections, oWhere, oOptions):
        return oCollections.find(oWhere, oOptions)


    def update(self, oCollections, oWhere, oSet):
        return oCollections.update(oWhere, oSet)


    def delete(self, oCollections, oWhere):
        return oCollections.delete(oWhere)


    def insert(self, oCollections, oNewDocument):
        return oCollections.insert(oNewDocument).inserted_id
