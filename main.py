from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api
from werkzeug.wrappers import response
import db_config as database
from bson.json_util import ObjectId

app = Flask(__name__)
api=Api(app)
CORS(app)

@app.route("/option/", methods=['GET'])
def insert():
    arduinoId = request.args.get("arduinoId")
    temp = request.args.get("temp")
    food = request.args.get("food")
    airQuality = request.args.get("airQuality")

    response = str(database.db.db_iot.insert_one(
            {
                'arduinoId':arduinoId,
                'airQuality':airQuality,
                'food':food,
                'temp':temp,
            }
        ).inserted_id)

    if response:
        return jsonify({"response":response})
    else:
        return jsonify({'message':'Error insert'})

if __name__ == '__main__':
    app.run(load_dotenv=True)