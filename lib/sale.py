from . import db_sqlite as db
from decimal import *


class Sale:
    def __init__(self, id=None, datetime=None, batchId=None, price=None, amount=None, note=None):
        self.id = None
        self.datetime = None
        self.batchId = None
        self.price = None
        self.amount = None
        self.note = None

        if id is not None:
            self.load_by_id(id)
        else:
            self.setClass(datetime, batchId, price, amount, note)
            self.id = self.save()


    def save(self):
        ret = None
        if self.id is None:
            ret = db.sale_insert(self.datetime, self.batchId, self.price, self.amount, self.note)
        else:
            pass # update
        return ret


    def load_by_id(self, id):
        p = db.sale_select_by_id(id)
        if bool(p):
            p = p[0]
            id, datetime, batchId, price, amount, note = p
            self.id = id
            self.setClass(datetime, batchId, price, amount, note)


    def setClass(self, datetime, batchId, price, amount, note):
        self.datetime = datetime
        self.batchId = batchId
        self.price = Decimal(str(price))
        self.amount = Decimal(str(amount))
        self.note = note


    def getId(self):
        return self.id


    def getDatetime(self):
        return self.datetime


    def getBatchId(self):
        return self.batchId


    def getPrice(self):
        return self.price


    def getAmount(self):
        return self.amount


    def getNote(self):
        return self.note


    def getAsString(self):
        return f"{self.id} {self.datetime} {self.batchId} {self.price} {self.amount} {self.note}"


    def print(self):
        print(self.getAsString())