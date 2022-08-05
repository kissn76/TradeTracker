from . import db_sqlite as db


class Stock:
    def __init__(self, id=None, code=None, name=None):
        self.id = None
        self.code = None
        self.name = None

        if id is not None:
            self.load_by_id(id)
        else:
            self.setClass(code, name)
            if self.code is not None:
                self.id = self.save()


    def save(self):
        ret = None
        if self.id is None:
            ret = db.stock_insert(self.code, self.name)
        else:
            pass # update
        return ret


    def load_by_id(self, id):
        p = db.stock_select_by_id(id)
        if len(p) > 0:
            self.id = p[0][0]
            self.setClass(p[0][1], p[0][2])


    def setClass(self, code, name):
        self.code = code
        self.name = name


    def getId(self):
        return self.id


    def getCode(self):
        return self.code


    def getName(self):
        return self.name


    def getAsString(self):
        return f"{self.id} {self.code} {self.name}"


    def print(self):
        print(self.getAsString())