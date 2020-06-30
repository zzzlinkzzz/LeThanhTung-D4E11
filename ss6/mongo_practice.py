
import json
from pymongo import MongoClient
from pymongo import TEXT
client = MongoClient()
db = client.get_database('d4e11')
collection = db.get_collection('movies')
# for d in data:
#     collection.insert_one(d)
# collection = db.get_collection('restaurants')
# file = open("C:/Users/Tung Linh/Desktop/data.txt","r")
# l =[]
# for line in file:
#     l.append(json.loads(line))
# print(l[0])
# movies = (collection.find())
# for movie in movies:
#     print(movie)

# Quentin_tarantino = collection.find({'writer': 'Quentin Tarantino'})
# for writer in Quentin_tarantino:
#     print(writer)

# brad_pitt = collection.find({'actors':'Brad Pitt'})
# for actor in brad_pitt:
#     print(actor)

# the_hobbit = collection.find({'franchise':'The Hobbit'})
# for f in the_hobbit:
#     print(f)

# for year in range(1990,2000,1):
#     in90s = collection.find({'year': year})
#     for i in in90s:
#         print(i)

# in90s = collection.find({
#     '$and' :
#     [
#         {'year' : {'$gt' : 1990}},
#         {'year' : {'$lt' : 2000}}
#     ]
# })
# for i in in90s:
#     print(i)

# query = {'title': 'Pulp Fiction'}
# update = {
#     '$set': {
#         'actors': 'Samuel L. Jackson'
#     }
# }
# collection.update_one(query, update)
# collection.create_index( [('brief', TEXT )])
# Bilbo = collection.find({
#     '$text':
#     {
#         '$search' : 'Bilbo'
#     }
# })
# for i in Bilbo:
#     print(i)

users = db.get_collection('users')
posts = db.get_collection('posts')
comments = db.get_collection('comments')

U = [
        {
            'username' : 'GoodGuyGreg',
            'first_name' : 'Good Guy',
            'last_name' : 'Greg'
        },
        {
            'username' : 'ScumbagSteve',
            'full_name' :{
                'first' : "Scumbag",
                'last' : "Steve"
            }
        }
    ]

p = [
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Passes out at party',
        'body' : 'Wakes up early and cleans house'},
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Steals your identity',
        'body' : 'Raises your credit score'},
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Reports a bug in your code',
        'body' : 'Sends you a Pull Request'},
    {
        'username' : 'ScumbagSteve',
        'title' : 'Borrows something',
        'body' : 'Sells it'},
    {
        'username' : 'ScumbagSteve',
        'title' : 'Borrows everything',
        'body' : 'The end'},
    {
        'username' : 'ScumbagSteve',
        'title' : 'Forks your repo on github',
        'body' : 'Sets to private'}
]

