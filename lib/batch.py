from . import db_sqlite as db
from . import provider, stock, sale, currency


class Batch:
    def __init__(self, id=None, providerId=None, stockId=None, datetime=None, price=None, priceCurrencyId=None, amount=None, note=None):
        self.id = None
        self.providerId = None
        self.provider = None
        self.stockId = None
        self.stock = None
        self.datetime = None
        self.price = None
        self.priceCurrencyId = None
        self.priceCurrency = None
        self.amount = None
        self.note = None
        self.sales = []
        self.balance = 0
        self.error = {}

        if id is not None:
            self.load_by_id(id)
            self.load_sales()
        else:
            self.setClass(providerId, stockId, datetime, price, priceCurrencyId, amount, note)
            self.id = self.save()
            self.setObjects()


    def validate(self):
        valid = db.batch_validate(self.providerId, self.stockId, self.datetime, self.price, self.priceCurrencyId, self.amount, self.note)
        self.error = valid


    def save(self):
        ret = None
        self.validate()
        if self.id is None and len(self.error) == 0:
            ret = db.batch_insert(self.providerId, self.stockId, self.datetime, self.price, self.priceCurrencyId, self.amount, self.note)
        else:
            pass # update
        return ret


    def load_by_id(self, id):
        p = db.batch_select_by_id(id)
        self.id = p[0][0]
        self.setClass(p[0][1], p[0][2], p[0][3], p[0][4], p[0][5], p[0][6], p[0][7])
        self.setObjects()


    def setClass(self, providerId, stockId, datetime, price, priceCurrencyId, amount, note=None):
        self.providerId = providerId
        self.stockId = stockId
        self.datetime = datetime
        self.price = price
        self.priceCurrencyId = priceCurrencyId
        self.amount = amount
        self.note = note
        self.balance = self.amount


    def setObjects(self):
        self.provider = provider.Provider(self.providerId)
        self.stock = stock.Stock(self.stockId)
        self.priceCurrency = currency.Currency(self.priceCurrencyId)


    def load_sales(self):
        self.sales.clear()
        self.balance = self.amount
        sales = db.sale_select_id_by_batchId(self.id)
        for s in sales:
            obj = sale.Sale(s[0])
            self.sales.append(obj)
            self.balance -= obj.getAmount()


    def sell(self, datetime, price, amount, note):
        obj = sale.Sale(None, datetime, self.id, price, amount, note)
        if obj.getId() is not None:
            self.sales.append(obj)
            self.balance -= obj.getAmount()


    def getId(self):
        return self.id


    def getProvider(self):
        return self.provider


    def getStock(self):
        return self.stock


    def getDatetime(self):
        return self.datetime


    def getPrice(self):
        return self.price


    def getPriceCurrency(self):
        return self.priceCurrency


    def getAmount(self):
        return self.amount


    def getNote(self):
        return self.note


    def getSales(self):
        return self.sales


    def getBalance(self):
        return self.balance


    def print(self):
        note = ""
        if self.note is not None:
            note = self.note

        print(f"Batch ID: {str(self.id)}")
        print(f"Provider: {self.provider.getAsString()}")
        print(f"Stock: {self.stock.getAsString()}")
        print(f"Balance: {self.balance}")
        print(f"Note: {note}\n")

        balance = self.amount
        batch_unit_price = self.price / self.amount
        profit = 0
        print(f"{'Date':<19}|{'Price':>16}|{'Amount':>16}|{'Balance':>16}|{'Unit price':>16}|{'Unit profit':>16}|{'Line profit':>16}|{'Profit':>16}|{'Note':^35}")
        print(f"{'':<19}|{self.priceCurrency.getSymbol():>16}|{'':>16}|{'':>16}|{self.priceCurrency.getSymbol():>16}|{self.priceCurrency.getSymbol():>16}|{self.priceCurrency.getSymbol():>16}|{self.priceCurrency.getSymbol():>16}|{'Note':^35}")
        print(f"{'':=^170}")
        print(f"{self.datetime:19}|{self.price:16,.2f}|{self.amount:16,.2f}|{balance:16,.2f}|{batch_unit_price:16,.2f}|{'':16}|{'':16}|{'':16}|{note:>35}".replace(",", " "))
        for s in self.sales:
            note = ""
            if s.getNote() is not None:
                note = s.getNote()
            balance -= s.getAmount()
            sale_unit_price = s.getPrice() / s.getAmount()
            unit_profit = sale_unit_price - batch_unit_price
            sale_profit = unit_profit * s.getAmount()
            profit += sale_profit
            print(f"{s.getDatetime():19}|{s.getPrice():16,.2f}|{(s.getAmount() * -1):16,.2f}|{balance:16,.2f}|{sale_unit_price:16,.2f}|{unit_profit:16,.2f}|{sale_profit:16,.2f}|{profit:16,.2f}|{note:>35}".replace(",", " "))

        print(f"{'':=^170}")
        print(f"{'':54}{balance:16,.2f}{profit:68,.2f} {self.priceCurrency.getSymbol()}".replace(",", " "))


def getAll():
    objects = {}
    elements = db.batch_select_all()
    for element in elements:
        obj = Batch(element[0])
        objects.update({obj.getId(): obj})
    return objects