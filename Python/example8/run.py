import pymongo

config = {
    # "mongo" : "mongodb://usuario:pass@localhost/admin"
    # "mongo" : "mongodb://usuario:pass@localhost:27100/admin"
    "mongo" : "mongodb://localhost:27100/admin"
}
myclient = pymongo.MongoClient(config['mongo'])

print('bases de datos',myclient.list_database_names())

db = myclient["test"]

print('coleciones',db.list_collection_names())

coleccion = db['users']
usuario = { "name": "Juan", "city": "Lima" }
x = coleccion.insert_one(usuario)
print(x.inserted_id)

# usuarios
usuarios = [
  { "name": "Juan", "city": "Lima" },
  { "name": "Jorge", "city": "Callao" }
]
x = coleccion.insert_many(usuarios)
print(x.inserted_ids)

# find one
x = coleccion.find_one()
print(x)

#query
query = { "name": { "$regex": "^Ju" } }
xs = coleccion.find(query)
for x in xs:
  print(x)
