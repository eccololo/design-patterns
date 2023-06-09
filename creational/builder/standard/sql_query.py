from query import Query


class SQLQuery(Query):

    def __init__(self, my_from, my_where):
        self.xwhere = my_where
        self.xfrom = my_from

    def execute(self):
        print(f"Executing SQLQuery from: {self.xfrom}, where: {self.xwhere}")

    def set_from(self, my_from):
        self.xfrom = my_from

    def set_where(self, my_where):
        self.xwhere = my_where
