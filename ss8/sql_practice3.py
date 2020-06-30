import pymysql
mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Nsi668888',
    cursorclass = pymysql.cursors.DictCursor
)
cursor = mysql_client.cursor()

from pymongo import MongoClient
mg_client = MongoClient()
db = mg_client.get_database('mysqlex')
collection = db.get_collection('cakes')

query_topping = [
    {
        '$match': {
            'topping': {'$ne':'None'}
        }
    },
    {
        '$unwind': '$topping'
    },
        {
        '$group': {
            '_id': '$topping'
        }
    }
]

topping = collection.aggregate(query_topping)

for tp in topping:
    print(tp['_id'])