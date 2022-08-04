import db_sqlite as db


class Sale:
    def __init__(self):
        self.id = None
        self.datetime = None
        self.batchId = None
        self.price = None
        self.amount = None
        self.note = None


    def load_by_id(self, id):
        p = db.sale_select_by_id(id)
        self.id = p[0][0]
        self.datetime = p[0][1]
        self.batchId = p[0][2]
        self.price = p[0][3]
        self.amount = p[0][4]
        self.note = p[0][5]


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