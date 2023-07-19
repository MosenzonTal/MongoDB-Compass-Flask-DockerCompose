import traceback
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongoadmin:mongoadmin@mongo:27017/testDB"
mongo = PyMongo(app)

@app.route('/')
def root():
    description = """*Welcome to the API!* <br><br>

    CRUD Operations Available: <br><br>
    - Create (POST): /add - Create a new user. Send a POST request with JSON data containing 'name', 'email', and 'pwd' fields. <br>
    - Read (GET): <br>
        - Get all users: /users - Retrieve all users. <br>
        - Get a specific user: /user/<id> - Retrieve a user by their ID. <br>
    - Update (PUT): /update - Update a user. Send a PUT request with JSON data containing '_id', 'name', 'email', and 'pwd' fields. <br>
    - Delete (DELETE): /delete/<id> - Delete a user by their ID. <br><br>

    Please refer to the API documentation for detailed usage instructions."""
    return description

@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']
    # validate the received values
    if _name and _email and _password and request.method == 'POST':
        # save details
        id = mongo.db.users.insert_one({'name': _name, 'email': _email, 'pwd': _password}).inserted_id
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()
        
@app.route('/users')
def users():
    users = mongo.db.users.find()
    resp = dumps(users)
    return resp
        
@app.route('/user/<id>')
def user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        resp = dumps(user)
        return resp
    else:
        resp = jsonify('User not found!')
        resp.status_code = 404
        return resp

@app.route('/update', methods=['PUT'])
def update_user():
    _json = request.json
    _id = _json['_id']
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']        
    # validate the received values
    if _name and _email and _password and _id and request.method == 'PUT':
        # Check if the user exists
        existing_user = mongo.db.users.find_one({'_id': ObjectId(_id)})
        if existing_user:
            # Update the user
            mongo.db.users.update_one({'_id': ObjectId(_id)}, {'$set': {'name': _name, 'email': _email, 'pwd': _password}})
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return 'user not found';
    else:
        return not_found()

        
@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp
    
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    if error:
        message['exception'] = traceback.format_exc()
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
