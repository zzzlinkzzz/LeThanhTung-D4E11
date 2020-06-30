import requests
from pymongo import MongoClient
client = MongoClient()
db = client.get_database('d4e11')
collection = db.get_collection('police_call')
# client = requests.get ('https://data.baltimorecity.gov/resource/xviu-ezkt.json')
# data = client.json()
# print(data[0])
# collection.insert_many(data)

# print(collection.find({"priority" : "Non-Emergency"}).count())

# district = collection.distinct('district')
# l = []
# for dc in district:
#     l.append(collection.find({"district" : dc}).count())
# print(district[l.index(max(l))],str(max(l)))

