import db_sqlite as db


class Currency:
    def __init__(self, id=None, code=None, name=None, symbol=None):
        self.id = None
        self.code = None
        self.name = None
        self.symbol = None

        if id is not None:
            self.load_by_id(id)
        else:
            self.setClass(code, name, symbol)
            self.id = self.save()


    def save(self):
        ret = None
        if self.id is None:
            ret = db.currency_insert(self.code, self.name, self.symbol)
        else:
            pass # update
        return ret


    def load_by_id(self, id):
        p = db.currency_select_by_id(id)
        self.id = p[0][0]
        self.setClass(p[0][1], p[0][2], p[0][3])
        
        
    def setClass(self, code, name, symbol):
        self.code = code
        self.name = name
        self.symbol = symbol


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