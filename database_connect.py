import json

import pymongo

MONGO_CLIENT_URL = 'localhost'
MONGO_CLIENT_PORT = 27017

# client = pymongo.MongoClient(host=MONGO_CLIENT_URL, port=MONGO_CLIENT_PORT, username="admin",password="123456")
client = pymongo.MongoClient(host=MONGO_CLIENT_URL, port=MONGO_CLIENT_PORT)
db = client['test']
collection = db['test']


def insert_one(col, line):
    db[col].insert_one(line)


def insert_many(col, list):
    db[col].insert_many(list)


def find_first(col):
    return db[col].find_one()

def find_all(col):
    list = []
    for item in db[col].find():
        list.append(item)
    return list

def

if __name__ == '__main__':
    print(collection)
    data = {'name': 'hello', 'url': 'hello'}
    insert_one('test',data)
    print(find_all('test'))
