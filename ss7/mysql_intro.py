import pymysql

client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Nsi668888',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = client.cursor()

# cursor.execute('CREATE DATABASE D4E11')

# cursor.execute('''
#     CREATE TABLE D4E11.user (
#     id INT(11) AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(255),
#     age INT(11)
#     )
# ''')

# cursor.execute('''
#     INSERT INTO D4E11.user (`username`,`age`)
#     VALUES ('dat',96),('tada',98);
# ''')
# client.commit()

# cursor.execute('''
#     SELECT COUNT(id) FROM D4E11.user AS count
# ''')
# data = cursor.fetchall()
# print(data)

# cursor.execute('''
#     SELECT *  FROM D4E11.user
# ''')
# data = cursor.fetchone()
# print(data)

# cursor.execute('''
#     UPDATE D4E11.user SET age = 1 WHERE age = 96
# ''')
# client.commit()

# cursor.execute('''
#     DELETE FROM D4E11.user WHERE age = 1
# ''')
# client.commit()

# cursor.execute('''
#     CREATE TABLE D4E11.centre (
#         id VARCHAR(255) UNIQUE PRIMARY KEY,
#         name VARCHAR(255) UNIQUE

#     )
# ''')

# cursor.execute('''

#     CREATE TABLE D4E11.saleman(
#         username VARCHAR(255) PRIMARY KEY,
#         centre_id VARCHAR(255) REFERENCES D4E11.centre(id),
#         email VARCHAR(255),
#         name VARCHAR(255)

#     )
# ''')

# cursor.execute('''
#     INSERT INTO D4E11.centre (`id`,`name`)
#     VALUES ('1', 'Anh'), ('2', 'Phap'), ('3','Nga'), ('4','Duc'), ('5','viet nam vo dich');
# ''')

# centre_name = 'Phap'

# cursor.execute(f'''
#     SELECT id FROM  D4E11.CENTRE WHERE name = '{centre_name}'
# ''')

# centre_found = cursor.fetchone()

# cursor.execute(f'''
#     INSERT INTO D4E11.saleman (`username`,`centre_id`,`email`,`name`)
#     VALUES ('best saleman','{centre_found['id']}','BS@snail.com','dollar man');
# ''')
# client.commit()
