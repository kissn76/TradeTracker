import db_sqlite as db
import provider
import stock


class Batch:
    def __init__(self):
        self.id = None
        self.provider = None
        self.stock = None
        self.datetime = None
        self.price = None
        self.amount = None
        self.note = None


    def load_by_id(self, id):
        p = db.batch_select_by_id(id)
        self.id = p[0][0]
        providerId = p[0][1]
        stockId = p[0][2]
        self.datetime = p[0][3]
        self.price = p[0][4]
        self.amount = p[0][5]
        self.note = p[0][6]
        self.provider = provider.Provider()
        self.provider.load_by_id(providerId)
        self.stock = stock.Stock()
        self.stock.load_by_id(stockId)


    def getProvider(self):
        return self.provider


    def getStock(self):
        return self.stock


    def getDatetime(self):
        return self.datetime


    def getPrice(self):
        return self.price


    def getAmount(self):
        return self.amount


    def getNote(self):
        return self.note

