from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS extension
import get_gemini_response

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in your Flask app

# Your Gemini-related imports and configuration here

class HealthInfo:
    Pedometer: int
    CalorieBurnt: int
    WaterCount: int
    HeartRate: int
    currWgt: int
    tgWgt: int
    Question: str

@app.route('/get_response', methods=['GET'])
def get_response():
    response = {"response": get_gemini_response.rs()}
    return jsonify(response)

@app.route('/ai/questions', methods=['POST'])
def receiveReq():
    data = request.json  # Get JSON data from the request
    # Access data attributes as needed
    response = {"response": get_gemini_response.rs(data.get('Pedometer'), data.get('CalorieBurnt'), data.get('WaterCount'), data.get('HeartRate'), data.get('currWgt'), data.get('tgWgt'), data.get('Question'))}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

