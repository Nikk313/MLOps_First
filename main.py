import pymongo

# provide the mongodb local host url to connect python to mongodb
client = pymongo.MongoClient('')

# database name
database = client['MyMongoDB']

# collection name
collection = database['Products']

# sample data
d = {'companyName': 'iNeuron', 'product': 'Affordable AI', 'courseOffered': 'Machine Learning'}

# Insert above records in the collection
rec = database.insert_one(d)

# Let's verify all the record at once
all_record = collection.find()

# printing all records present in the collection
for idx, record in enumerate(all_record):
    print(f"{idx} : {record}")

