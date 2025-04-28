from flask import Flask, jsonify, request, render_template, redirect
from dotenv import load_dotenv
import json
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db=client.GitTutorial

collection = db['todo-list']
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

@app.route('/todopage', methods=['GET'])
def todo():
    return render_template('todopage.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():

    Item_Name = request.form['Item_Name']
    Item_Description = request.form['Item_Description']

    if not Item_Name or not Item_Description:
        return jsonify({"error": "Item_Name and Item_Description are required"}), 400

    collection.insert_one({
        "Item_Name": Item_Name,
        "Item_Description": Item_Description
    })
    return "Todo item submitted successfully"

if __name__ == '__main__':

    app.run(debug=True)