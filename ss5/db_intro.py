# from pymongo import MongoClient
# client = MongoClient()

# db = client.get_database('d4e11')
# collection = db.get_collection('members')
# # collection.insert_one({
# #     'name': 'Dat',
# #     'age': 24,
# #     'gender': True
# # })
# collection.insert_many(
#     [
#         {
#             'name': 'Dat1',
#             'age': 24,
#             'gender': True
#         },
#         {
#             'name': 'Dat2',
#             'age': 24,
#             'gender': True
#         },
#                 {
#             'name': 'Dat3',
#             'age': 24,
#             'gender': True
#         },
#                 {
#             'name': 'Dat4',
#             'age': 24,
#             'gender': True
#         },

#     ])


from datetime import date
import requests
import pandas as pd
url = "https://s.cafef.vn/TraCuuLichSu2/1/HASTC/28/05/2020.chn"
r = requests.get(url)

table = pd.read_html(r.text)
for i in range(len(table)):
    print(i, table[i].head(2))

# table0 = table[1].transpose().head(1)
# print(table0)
# print(len(table0))
# table1 = table[4]
# print(table1.head(5))
# print(len(table1))