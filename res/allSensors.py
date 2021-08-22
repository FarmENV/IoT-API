from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Sensors(Resource):
  ''' Get all the sensors '''
  def get(self):
    response = list(database.db.sensors.find())
    for doc in response:
      doc['_id'] = str(doc['_id'])

    return jsonify(response)