import db_sqlite as db
import provider
import stock
import sale
import currency


class Batch:
    def __init__(self):
        self.id = None
        self.provider = None
        self.stock = None
        self.datetime = None
        self.price = None
        self.priceCurrency = None
        self.amount = None
        self.note = None
        self.sales = []
        self.balance = 0


    def load_by_id(self, id):
        p = db.batch_select_by_id(id)
        self.id = p[0][0]
        providerId = p[0][1]
        stockId = p[0][2]
        self.datetime = p[0][3]
        self.price = p[0][4]
        priceCurrencyId = p[0][5]
        self.amount = p[0][6]
        self.note = p[0][7]
        self.provider = provider.Provider()
        self.provider.load_by_id(providerId)
        self.stock = stock.Stock()
        self.stock.load_by_id(stockId)
        self.priceCurrency = currency.Currency()
        self.priceCurrency.load_by_id(priceCurrencyId)
        self.balance = self.amount
        self.load_sales()


    def load_sales(self):
        sales = db.sale_select_by_batchId(self.id)
        for s in sales:
            obj = sale.Sale()
            obj.load_by_id(s[0])
            self.sales.append(obj)
            self.balance -= obj.getAmount()


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


def getBaches():
    baches = db.batch_select_all()
    ret = []

    for bach in baches:
        tmp = Batch()
        tmp.load_by_id(bach[0])
        ret.append(tmp)

    return ret