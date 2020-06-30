from pymongo import MongoClient
client = MongoClient()
db = client.get_database('d4e11')
collection = db.get_collection('movies')

 

# cursor.execute('''
#     CREATE TABLE D4E11.movies (
#     id INT(11) AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255),
#     writer VARCHAR(255),
#     year INT(11)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE D4E11.actor (
#     id INT(11) AUTO_INCREMENT PRIMARY KEY,
#     actor_name VARCHAR(255)
#     )
# ''')

movies = collection.find()

# for movie in movies:
#     title = movie.get('title')
#     writer = movie.get('writer')
#     if writer == None:
#         writer = 'NULL'
#     else:
#         writer = f'\"{writer}\"'
#     year = movie.get('year')
#     if year == None:
#         year = 'NULL'
#     else:
#         year = f'\"{year}\"'

#     cursor.execute(f'''
#     INSERT INTO D4E11.movies (`title`,`writer`,`year`)
#     VALUES ("{title}",{writer},{year});
#     ''')
#     client.commit()

actors = []
for movie in movies:
    actor = movie.get('actors')
    try:
        actors.append(actor)
    except:
        pass

# actors = set(actors)

print(actors)

# for actor in actors:
#     cursor.execute(f'''
#     INSERT INTO D4E11.actor (`actor_name`)
#     VALUES ({actor});
#     ''')
#     client.commit()