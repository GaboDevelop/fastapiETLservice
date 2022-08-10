import pymongo


class Mongo(object):
    uri = None
    database = None

    def initialize(self, uri, database):
        print(uri)
        client = pymongo.MongoClient(uri)
        self.database = client[database]

    def insert(self, collection, data):
        self.database[collection].insert(data)

    def find(self, collection, query):
        return list(self.database[collection].find(query))

    def find_one(self, collection, query):
        return self.database[collection].find_one(query)

    def close(self):
        self.database.close()
