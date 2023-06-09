from query import Query


class MongoDBQuery(Query):

    def __init__(self, my_from, my_where):
        self.xwhere = my_where
        self.xfrom = my_from

    def execute(self):
        print(f"Executing MongoDB from: {self.xfrom}, where: {self.xwhere}")

    def set_from(self, my_from):
        self.xfrom = my_from

    def set_where(self, my_where):
        self.xwhere = my_where
