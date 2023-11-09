from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['task_tracker']
tasks_collection = db['tasks']

# Routes
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find({}, {'_id': 0}))
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    if 'title' not in new_task or 'description' not in new_task or 'status' not in new_task:
        return jsonify({'error': 'Title, description, and status are required'}), 400

    tasks_collection.insert_one(new_task)
    return jsonify({'message': 'Task added successfully'})

if __name__ == '__main__':
    app.run(debug=True)




import pymongo# Connect to MongoDB 
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client[""] #desired database name
collection = database["tasks"]
def add_task(title, description, status="To Do"):
    pass
def list_tasks():
    pass
def update_task_status(task_id, new_status):
    pass
def delete_task(task_id):
    pass