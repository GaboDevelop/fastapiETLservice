from mongoengine import *

class SaleOrder(Document):
    number_order = StringField()
    amount = FloatField()

