from . import db_sqlite as db


class Stock:
    def __init__(self, id=None, code=None, name=None):
        self.id = None
        self.code = None
        self.name = None
        self.error = {}

        if id is not None:
            self.load_by_id(id)
        else:
            self.setClass(code, name)
            self.id = self.save()


    def validate(self):
        valid = db.stock_validate(self.code, self.name)
        self.error = valid


    def save(self):
        ret = None
        self.validate()
        if self.id is None and len(self.error) == 0:
            ret = db.stock_insert(self.code, self.name)
        else:
            pass # update
        return ret


    def load_by_id(self, id):
        p = db.stock_select_by_id(id)
        if bool(p):
            p = p[0]
            id, code, name = p
            self.id = id
            self.setClass(code, name)


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


def getAll():
    objects = {}
    elements = db.stock_select_all()
    for element in elements:
        id = element[0]
        obj = Stock(id)
        objects.update({obj.getId(): obj})
    return objects


def printAll():
    objects = getAll()
    for objId in objects:
        objects[objId].print()