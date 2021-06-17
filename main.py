from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

hash_password = "ECF389B6DDCF5D10D1D494924300A2ADC23AFAFD03FE9669C27774ED2895B6EC"

@app.route("/option/<string:_hash>/", methods=['GET'])
def option(_hash):
    if _hash == hash_password:
        temp = request.args.get("temp")
        food = request.args.get("food")
        airQuality = request.args.get("airQuality")
        return jsonify({"temp":temp,"food":food,"airQuality":airQuality})
    else:
        return jsonify({"500":"error"})

if __name__ == '__main__':
    app.run(load_dotenv=True)