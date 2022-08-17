from mongoengine import connect

class Mongo(object):
    def initialize(self):
        print("Se inicio mongo")
        connect(host="mongodb+srv://oscar:1234@cluster0.5telvkv.mongodb.net/etl_service?retryWrites=true&w=majority")