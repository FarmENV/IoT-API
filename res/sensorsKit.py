from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class SensorsKit(Resource):
  #One sensor at a time

  def get(self,by,data):
    response = self.abort_if_not_exists(by, data)
    response['_id'] = str(response['_id'])
    return jsonify(response)

  def post(self):
    _id = str(database.db.sensors.insert_one(
      {
        'name':request.json['name'],
        'description':request.json['description'],
        'img_url':request.json['img_url']
      }
    ).inserted_id)

    return jsonify({'_id':_id})

  def put(self,by,data):
    response = self.abort_if_not_exists(by,data)

    for key, value in request.json.items():
      response[key] = value

    database.db.sensors.update_one(
      {'_id':ObjectId(response['_id'])},
      {
        '$set':{
          'name':response['name'],
          'description':response['description'],
          'img_url':response['img_url']
        }
      }
    )

    response['_id'] = str(response['_id'])
    return jsonify(response)

  def delete(self,by,data):
    response = self.abort_if_not_exists(by, data)
    database.db.sensors.delete_one({'_id':response['_id']})
    response['_id'] = str(response['_id'])
    return jsonify({'Deleted sensor:':response})

  def abort_if_not_exists(self,by,data):
    if by == '_id':
      response = database.db.sensors.find_one({f'_id':ObjectId(data)})
    else:
      response = database.db.sensors.find_one({f'{by}':data})

    if response:
      return response
    else:
      abort(jsonify({'status':404,f'{by}':f'{data} was not found'}))
