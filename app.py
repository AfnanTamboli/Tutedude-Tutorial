from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

@app.route('/api', methods=['GET'])
def get_data():
    
    with open(DATA_FILE, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON data"})

    return jsonify(data)

if __name__ == '__main__':

    app.run(debug=True)