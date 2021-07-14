""" Flask configuration to conenct to the Database """
from flask_pymongo import pymongo
import os

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


client = pymongo.MongoClient("mongodb+srv://dbUser:Ae7NVCawYOdA8iSI@iot.s54k2.mongodb.net/db_iot?retryWrites=true&w=majority")

# This is the db name
db = client.db_iot
