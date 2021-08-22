from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Measurements(Resource):

    def get(self,data):
        response = self.abort_if_not_exist(data)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    ''' Delete all data from an arduino object '''
    def delete(self, data):
        response = self.abort_if_not_exist(data)
        database.db.db_iot.delete_one({'arduinoId':response['arduinoId']})
        
        return jsonify({"deleted ":data})

    ''' Checks if an arduino exists '''
    def check_if_arduino_exists(data):
        response = database.db.db_iot.find_one({'arduinoId':data})

        if response:
            return False
        else:
            return True

    def abort_if_not_exist(self,data):
        response = database.db.db_iot.find_one({'arduinoId':data})

        if response:
            return response
        else:
            abort(jsonify({'status':404,'Arduino':f'{data} not found'}))