import db_sqlite as db

class Provider:
    def __init__(self):
        self.id = None
        self.code = None
        self.name = None


    def load_by_id(self, id):
        p = db.provider_select_by_id(id)
        self.id = p[0][0]
        self.code = p[0][1]
        self.name = p[0][2]


    def getCode(self):
        return self.code


    def getName(self):
        return self.name