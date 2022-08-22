from . import db_sqlite as db
from . import provider, stock, sale, currency
import dateutil.parser as dtup
from decimal import *


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
        if bool(p):
            p = p[0]
            id, providerId, stockId, datetime, price, priceCurrencyId, amount, note = p
            self.id = id
            self.setClass(providerId, stockId, datetime, price, priceCurrencyId, amount, note)
            self.setObjects()


    def setClass(self, providerId, stockId, datetime, price, priceCurrencyId, amount, note=None):
        self.providerId = providerId
        self.stockId = stockId
        self.datetime = datetime
        self.price = Decimal(str(price).replace(',', '.'))
        self.priceCurrencyId = priceCurrencyId
        self.amount = Decimal(str(amount).replace(',', '.'))
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


    def getAsString(self):
        ret = ""
        note = ""
        if self.note is not None:
            note = self.note

        ret += f"Batch ID: {str(self.id)}\n"
        ret += f"Provider: {self.provider.getAsString()}\n"
        ret += f"Stock: {self.stock.getAsString()}\n"
        ret += f"Balance: {self.balance}\n"
        ret += f"Note: {note}\n\n"

        balance = self.amount
        batch_unit_price = self.price / self.amount
        profit = 0

        ret += f"{'Date':<19}|{'Price':>16}|{'Amount':>16}|{'Balance':>16}|{'Unit price':>16}|{'Unit profit':>16}|{'Line profit':>16}|{'Profit':>16}|{'Note':^35}\n"
        ret += f"{'':<19}|{self.priceCurrency.getSymbol():>16}|{'':>16}|{'':>16}|{self.priceCurrency.getSymbol():>16}|{self.priceCurrency.getSymbol():>16}|{self.priceCurrency.getSymbol():>16}|{self.priceCurrency.getSymbol():>16}|{'Note':^35}\n"
        ret += f"{'':=^170}\n"
        ret += f"{self.datetime:19}|{self.price:16,.2f}|{self.amount:16,.2f}|{balance:16,.2f}|{batch_unit_price:16,.2f}|{'':16}|{'':16}|{'':16}|{note:>35}\n".replace(",", " ")
        
        for s in self.sales:
            note = ""
            if s.getNote() is not None:
                note = s.getNote()
            balance -= s.getAmount()
            sale_unit_price = s.getPrice() / s.getAmount()
            unit_profit = sale_unit_price - batch_unit_price
            sale_profit = unit_profit * s.getAmount()
            profit += sale_profit
            
            ret += f"{s.getDatetime():19}|{s.getPrice():16,.2f}|{(s.getAmount() * -1):16,.2f}|{balance:16,.2f}|{sale_unit_price:16,.2f}|{unit_profit:16,.2f}|{sale_profit:16,.2f}|{profit:16,.2f}|{note:>35}\n".replace(",", " ")

        balance_string = f"{balance:,.2f}".replace(",", " ")
        profit_string = f"{profit:,.2f} {self.priceCurrency.getSymbol()}".replace(",", " ")

        ret += f"{'':=^170}\n"
        ret += f"{'':54}{balance_string:>16}{profit_string:>68}"

        return ret


    def print(self):
        print(self.getAsString())


def getAll():
    objects = {}
    elements = db.batch_select_all()
    for element in elements:
        id = element[0]
        obj = Batch(id)
        objects.update({obj.getId(): obj})
    return objects


def getByStock(stockId):
    objects = {}
    elements = db.batch_select_by_stockId(stockId)
    for element in elements:
        id = element[0]
        obj = Batch(id)
        objects.update({obj.getId(): obj})
    return objects


def getByStockWithBalance(stockId):
    objects = {}
    allObject = getByStock(stockId)
    for obj in allObject:
        obj = Batch(obj)
        if obj.getBalance() > 0.0:
            objects.update({obj.getId(): obj})
    return objects


def printStock(stockId):
    stockObj = stock.Stock(stockId)
    objects = getByStock(stockId)
    transactions = []
    for obj in objects:
        obj = Batch(obj)
        amount = obj.getAmount()
        price = obj.getPrice()
        currency = obj.getPriceCurrency()
        dateAndTime = obj.getDatetime()
        note = obj.getNote()
        buy_unit_price = price / amount
        transactionBuy = [dateAndTime, price, currency.getCode(), amount, note, None]
        transactions.append(transactionBuy)

        sales = obj.getSales()
        for saleObj in sales:
            if saleObj.getId() is not None:
                amount = saleObj.getAmount()
                price = (saleObj.getPrice() * -1.0)
                dateAndTime = saleObj.getDatetime()
                note = saleObj.getNote()
                transactionSell = [dateAndTime, price, currency.getCode(), (amount * -1), note, buy_unit_price]
                transactions.append(transactionSell)

    transactionsSorted = sorted(transactions, key=lambda x: (dtup.parse(x[0]), -x[3]))
    balance = 0
    profit = 0
    print(f"Stock: {stockObj.getAsString()}")
    print(f"{'Date':<19}|{'Price':>20}|{'Amount':>16}|{'Balance':>16}|{'Unit price':>16}|{'Line profit':>16}|{'Profit':>16}|{'Note':^35}")
    print(f"{'':=^170}")
    for tr in transactionsSorted:
        date, price, currency, amount, note, buy_unit_price = tr
        buy_price = 0.0
        line_profit = 0.0
        if buy_unit_price is not None:
            buy_price = buy_unit_price * amount
            line_profit = buy_price - price
            profit += line_profit
        if note is None:
            note = ""
        balance += amount
        price_string = f"{price:,.2f} {currency}".replace(",", " ")
        amount_string = f"{amount:,.2f}".replace(",", " ")
        balance_string = f"{balance:,.2f}".replace(",", " ")
        unit_price_string = f"{(price / amount):,.2f}".replace(",", " ")
        line_profit_string = f"{line_profit:,.2f}".replace(",", " ")
        profit_string = f"{profit:,.2f}".replace(",", " ")
        print(f"{date:19}|{price_string:>20}|{amount_string:>16}|{balance_string:>16}|{unit_price_string:>16}|{line_profit_string:>16}|{profit_string:>16}|{note:>35}")
    print(f"{'':=^170}")
    print(f"{'':58}{balance_string:>16}{'':35}{profit_string:>16}")