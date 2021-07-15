from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Measurements(Resource):

    def delete(self):
        return database.db.db_iot.delete_many({}).deleted_count