from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Measurement(Resource):
    #One badge at a time
    
    def get(self,by,data):
        response = self.abort_if_not_exist(by, data)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    def post(self):
        _id = str(database.db.db_iot.insert_one(
            {
                'arduinoId':request.json['arduinoId'],
                'airQuality':request.json['airQuality'],
                'food':request.json['food'],
                'temp':request.json['temp'],
            }
        ).inserted_id)

        return jsonify({"_id":_id})

    def abort_if_not_exist(self,by,data):
        if by == '_id':
            response = database.db.db_iot.find_one({f'_id':ObjectId(data)})
        else:
            response = database.db.db_iot.find_one({f'{by}':data})

        if response:
            return response
        else:
            abort(jsonify({'status':404,f'{by}':f'{data} not found'}))