from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api
import db_config as database

from res.measurement import Measurement

app = Flask(__name__)
api=Api(app)
CORS(app)

hash_password = "ECF389B6DDCF5D10D1D494924300A2ADC23AFAFD03FE9669C27774ED2895B6EC"

@app.route("/option/<string:_hash>/", methods=['GET'])
def option(_hash):
    if _hash == hash_password:
        arduinoId = request.args.get("arduinoId")
        temp = request.args.get("temp")
        food = request.args.get("food")
        airQuality = request.args.get("airQuality")

        return jsonify({"arduinoId":arduinoId,"temp":temp,"food":food,"airQuality":airQuality})
    else:
        return jsonify({"500":"error"})

api.add_resource(Measurement,'/new/','/<string:by>:<string:data>/')

if __name__ == '__main__':
    app.run(load_dotenv=True)