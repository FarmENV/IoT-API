from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Measurements(Resource):

    ''' Delete all data '''
    def delete(self):
        return database.db.db_iot.delete_many({}).deleted_count

    ''' Checks if an arduino exists '''
    def check_if_arduino_exists(data):
        response = database.db.db_iot.find_one({'arduinoId':data})

        if response:
            return False
        else:
            return True