from . import db_sqlite as db


class Currency:
    def __init__(self, id=None, code=None, name=None, symbol=None):
        self.id = None
        self.code = None
        self.name = None
        self.symbol = None
        self.error = []

        if id is not None:
            self.load_by_id(id)
        else:
            self.setClass(code, name, symbol)
            self.id = self.save()


    def validate(self):
        valid = db.currency_validate(self.code, self.name, self.symbol)
        self.error = valid


    def save(self):
        ret = None
        self.validate()
        if self.id is None and len(self.error) == 0:
            ret = db.currency_insert(self.code, self.name, self.symbol)
        else:
            pass # update
        return ret


    def load_by_id(self, id):
        p = db.currency_select_by_id(id)
        if len(p) > 0:
            self.id = p[0][0]
            self.setClass(p[0][1], p[0][2], p[0][3])


    def setClass(self, code, name, symbol):
        self.code = code
        self.name = name
        self.symbol = symbol


    def getId(self):
        return self.id


    def getCode(self):
        return self.code


    def getName(self):
        return self.name


    def getSymbol(self):
        return self.symbol


    def getAsString(self):
        return f"{self.id} {self.code} {self.name} {self.symbol}"


    def print(self):
        print(self.getAsString())


def getCurrencyAll():
    objects = {}
    elements = db.currency_select_all()
    for element in elements:
        obj = Currency(element[0])
        objects.update({obj.getId(): obj})
    return objects