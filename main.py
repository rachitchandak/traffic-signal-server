from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DURATION = {"green_time":0}

@app.route('/')
def signal_duration():
    return DURATION

@app.route('/data', methods=['POST'])
def update_duration():
    global DURATION
    new_data = request.json
    DURATION = new_data

@app.route('/latest_data', methods=['GET'])
def latest_duration():
    return jsonify(DURATION)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
