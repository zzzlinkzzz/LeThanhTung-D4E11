from pymongo import MongoClient
client = MongoClient()

db = client.get_database('d4e11')
collection = db.get_collection('candidate')
#collection.insert_many(candidate["data"]) # create

# candidate = collection.find() # read
# for member in candidate:
#     print(member)
# def find_by_jobs(job,not_this_job = True):
#     if not_this_job== True:
#         array = collection.find({
#         'hr.position': job
#         })
#     else:
#         array = collection.find({
#         'hr.position': {'$ne': job}
#         })
#     for i in array:
#         print(i)

# find_by_jobs('Accountant',False)

# def num_of_positions(job):
#     print(collection.count({'hr.position': job}))
# num_of_positions('Accountant')

# members = collection.find(
#     {}
# ).sort('name', -1)
# for member in members:
#     print(member)

query = {'name': 'Tiger Nixon'}
update = {
    '$set': {
        'hr.salary': '$400000'
    }
}
collection.update_one(query, update)


