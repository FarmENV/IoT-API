from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api
from werkzeug.wrappers import response
import db_config as database
from bson.json_util import ObjectId

from res.measurements import Measurements

app = Flask(__name__)
api=Api(app)
CORS(app)

""" In this endpoint the arduino object is created in the database
    if it does not exists """
@app.route("/arduinoPost/", methods=['GET'])
def insertArduino():

    arduinoId = request.args.get("arduinoId")
    flag = Measurements.check_if_arduino_exists(arduinoId)
    print(flag)
    if(flag):
        date = request.args.get("date")
        response = str(database.db.db_iot.insert_one(
                {
                    'arduinoId':arduinoId,
                    'airQuality':0,
                    'food':0,
                    'temp':0,
                    'lastUpdate':date,
                    'measurements':[]
                }
            ).inserted_id)

    if flag:
        return jsonify({"response":response, "arduinoId":arduinoId, "date":date})
    else:
        return jsonify({'message':'Arduino already exists'})

""" In this endpoint the arduino's data is updated
    and there is created a new object in the
    measurements array """
@app.route("/option/", methods=['GET'])
def insert():
    arduinoId = request.args.get("arduinoId")
    temp = request.args.get("temp")
    food = request.args.get("food")
    airQuality = request.args.get("airQuality")
    date = request.args.get("date")

    database.db.db_iot.update_one({'arduinoId':arduinoId},
        {
            '$push':{
            'measurements':{
                'airQuality':airQuality,
                'food':food,
                'temp':temp,
                'date':date,
            }},
            '$set':{
            'airQuality':airQuality,
            'food':food,
            'temp':temp,
            'lastUpdate':date,
            }
        })

    return jsonify({"arduinoId":arduinoId,"temp":temp,"food":food,"airQuality":airQuality, "date":date})

api.add_resource(Measurements, '/del/all/')

if __name__ == '__main__':
    app.run(load_dotenv=True)