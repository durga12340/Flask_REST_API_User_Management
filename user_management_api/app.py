from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = [{"id": "1","name": "John Doe"},
        {"id": "2","name": "Dinga"},
        {"id": "3","name": "Dingi"}
    ]

# GET route to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# POST route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    user_id = request.json.get('id')
    user_name = request.json.get('name')
    if user_id in users:
        return jsonify({"error": "User  already exists"}), 400
    users[user_id] = user_name
    return jsonify({"id": user_id, "name": user_name}), 201

# PUT route to update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User  not found"}), 404
    user_name = request.json.get('name')
    users[user_id] = user_name
    return jsonify({"id": user_id, "name": user_name}), 200

# DELETE route to remove a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User  not found"}), 404
    del users[user_id]
    return jsonify({"message": "User  deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
