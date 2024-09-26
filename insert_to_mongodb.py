import urllib.parse
from pymongo import MongoClient

# 將帳號密碼改成MongoDB URI可以認得的格式
username = urllib.parse.quote_plus('mongodb')
password = urllib.parse.quote_plus('mongodb')
# 登入
client = MongoClient(f'mongodb://{username}:{username}@localhost:27017')
# 取得資料庫
db = client.test_pymongo_databass
# 取得collection
coll = db.test

data = {"name": "Peter", "job": "Data Engineer"}
# 加入一筆資料，接收一個dict
coll.insert_one(data)

datas = [
    {
        "author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
    },
    {
        "author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
    },
]
# 加入多筆資料，接收一個list
coll.insert_many(datas)
