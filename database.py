from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://wolfjobs:W00FW00F@cluster0.uj4oftq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('WolfJobs_DB')
