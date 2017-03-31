### Checkpoint 4
```
import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.csci2963
definitions = db.definitions

print "Fetch all records"
for definition in definitions.find():
    pprint.pprint(definition)

print "\nFetch one record"
pprint.pprint(definitions.find_one())

print "\nFetch a specific record"
pprint.pprint(definitions.find_one({"word": "Recursive"}))

print "\nInsert a new record"
def_id = definitions.insert_one({"word":"Nugget","definition":"n. A morsel left behind or forgotten, perfect size for future sampling"}).inserted_id

print "\nFetch a record by object id"
pprint.pprint(definitions.find_one(def_id))
```
