import pymysql
mysql_client = pymysql.connect(

    host = 'localhost',
    user = 'root',
    password = 'Nsi668888',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = mysql_client.cursor()

# cursor.execute('''
#   CREATE TABLE IF NOT EXISTS movies.movie(
#     id VARCHAR(255) PRIMARY KEY,
#     title VARCHAR(255),
#     writer VARCHAR(255),
#     year VARCHAR(255)
#   )
# ''')
# cursor.execute('''
#   CREATE TABLE IF NOT EXISTS movies.actor(
#     name VARCHAR(255) PRIMARY KEY
#   )
# ''')

# cursor.execute('''
#   CREATE TABLE IF NOT EXISTS movies.movie_actor(
#     movie_id VARCHAR(255),
#     actor_name VARCHAR(255),
#     PRIMARY KEY(movie_id, actor_name)
#   )
# ''')
# mysql_client.commit()

from pymongo import MongoClient
mg_client = MongoClient()
db = mg_client.get_database('d4e11')
collection = db.get_collection('movies')

query1 = {
    'title': {'$ne':None},
    'writer': {'$ne':None},
    'year': {'$ne':None},
    'actors': {'$ne':None}
}
movies = collection.find(query1) #extract

# for movie in movies: #LOAD
#     movie_id = str(movie['_id'])
#     movie_title = str(movie['title'])
#     movie_writer = str(movie['writer'])
#     movie_year = str(movie['year'])

#     cursor.execute(f'''
#         INSERT INTO movies.movie(id, title, writer, year)
#         VALUES ('{movie_id}','{movie_title}','{movie_writer}','{movie_year}')
#     ''')

#     mysql_client.commit()

query2 = [
 {
    '$match': {
        'actors': {'$ne': None}
    }
  },
  {
      '$unwind': '$actors'
  },
  {
    '$group': {
      '_id': '$actors' 
    }
  }
]
for actor in collection.aggregate(query2):
  print(actor)
  cursor.execute(f'''
    INSERT INTO movies.actor(name)
    VALUES('{actor['_id']}')
  ''')
  mysql_client.commit()

for movie in collection.find(query1):
    for actor in movie['actors']:
        print(movie['_id'],actor)
        cursor.execute(f'''
            INSERT INTO movies.movie_actor (movie_id, actor_name)
            VALUES ('{str(movie['_id'])}','{actor}')
        ''')
        mysql_client.commit()

# mongorestore -d mysqlex d4e11