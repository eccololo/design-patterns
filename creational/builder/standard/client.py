from sql_query import SQLQuery
from mongodb_query import MongoDBQuery

xfrom = "Client table"
xwhere = "client name = ..."


sql_query = SQLQuery(xfrom, xwhere)
sql_query.execute()


sql_query = MongoDBQuery(xfrom, xwhere)
sql_query.execute()