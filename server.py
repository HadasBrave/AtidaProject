from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db_1 = client['personalInformation']
db_2 = client['corona_details']
personal_info = db_1['people']
corona = db_2['corona']

# Insert a new personal info record
@app.route('/personal-info_add', methods=['POST'])
def add_personal_info():
    data = request.get_json()
    if 'name' not in data or 'id' not in data or 'address' not in data or 'dob' not in data or 'phone' not in data:
        return {'error': 'Missing data field(s)'}, 400
    personal_info.insert_one(data)
    return {'message': 'Personal info added successfully'}, 201

# Retrieve all personal info records
@app.route('/personal-info_get', methods=['GET'])
def get_personal_info():
    personal_info_list = []
    for info in personal_info.find():
        info['_id'] = str(info['_id'])  # Convert ObjectId to string
        personal_info_list.append(info)
    return jsonify(personal_info_list), 200

# Retrieve a personal info record by ID
@app.route('/personal-info/<id>', methods=['GET'])
def get_personal_info_by_id(id):
    info = personal_info.find_one({'_id': ObjectId(id)})
    if info:
        info['_id'] = str(info['_id'])
        return jsonify(info), 200
    else:
        return {'error': 'Personal info not found'}, 404

# Insert a new corona record
@app.route('/corona_add', methods=['POST'])
def add_corona():
    data = request.get_json()
    if 'vaccine_dates' not in data or 'vaccine_manufacturer' not in data or 'positive_result_date' not in data:
        return {'error': 'Missing data field(s)'}, 400
    corona.insert_one(data)
    return {'message': 'Corona record added successfully'}, 201

# Retrieve all corona records
@app.route('/corona_get', methods=['GET'])
def get_corona():
    corona_list = []
    for c in corona.find():
        c['_id'] = str(c['_id'])  # Convert ObjectId to string
        corona_list.append(c)
    return jsonify(corona_list), 200

# Retrieve a corona record by ID
@app.route('/corona/<id>', methods=['GET'])
def get_corona_by_id(id):
    c = corona.find_one({'_id': ObjectId(id)})
    if c:
        c['_id'] = str(c['_id'])  # Convert ObjectId to string
        return jsonify(c), 200
    else:
        return {'error': 'Corona record not found'}, 404


if __name__ == '__main__':
    app.run(debug=True)
