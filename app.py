from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from prediction import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/', methods=['POST'])
def get_prediction():
    record = json.loads(request.data)
    # print(record)
    result, proba, message = predict_sentiment(record['comment'], record['modelName'])

    return jsonify(message)