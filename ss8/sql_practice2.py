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
collection = db.get_collection('pollice_call')



cursor.execute('''
  CREATE TABLE IF NOT EXISTS sql_practice.police_call(
    id VARCHAR(255) PRIMARY KEY,
    recordid VARCHAR(255),
    callnumber VARCHAR(255),
    calldatetime VARCHAR(255),
    priority VARCHAR(255),
    district VARCHAR(255),
    description VARCHAR(255),
    incidentlocation VARCHAR(255),
    zipcode VARCHAR(255),
    neighborhood VARCHAR(255),
    policedistrict VARCHAR(255),
    policepost VARCHAR(255),
    councildistrict VARCHAR(255),
    sheriffdistricts VARCHAR(255),
    community_statistical_areas VARCHAR(255),
    census_tracts VARCHAR(255),
    vrizones VARCHAR(255)
  )
''')

police_call = collection.find()
for record in police_call:
    id = str(record['_id'])
    recordid = str(record['recordid'])
    callnumber = str(record['callnumber'])
    calldatetime = str(record['calldatetime'])
    priority = str(record['priority'])
    district = str(record['district'])
    description = str(record['description'])
    incidentlocation = str(record['incidentlocation'])
    zipcode = str(record['zipcode'])
    neighborhood = str(record['neighborhood'])
    policedistrict = str(record['policedistrict'])
    policepost = str(record['policepost'])
    councildistrict = str(record['councildistrict'])
    sheriffdistricts = str(record['sheriffdistricts'])
    community_statistical_areas = str(record['community_statistical_areas'])
    census_tracts = str(record['census_tracts'])
    vrizones = str(record['vrizones'])
    cursor.execute(f'''
        INSERT INTO sql_practice.police_call(id,recordid, callnumber, calldatetime, priority, district, description, incidentlocation, zipcode, neighborhood, policedistrict, policepost, councildistrict, sheriffdistricts, community_statistical_areas, census_tracts, vrizones)
        VALUES ("{id}","{recordid}", "{callnumber}", "{calldatetime}", "{priority}", "{district}", "{description}", "{incidentlocation}", "{zipcode}", "{neighborhood}", "{policedistrict}", "{policepost}", "{councildistrict}", "{sheriffdistricts}", "{community_statistical_areas}", "{census_tracts}", "{vrizones}")
    ''')
    mysql_client.commit()