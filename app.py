from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {}
next_id = 1

# Create a user
@app.route("/users", methods=["POST"])
def create_user():
    global next_id
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    users[next_id] = {"name": data["name"]}
    response = {"id": next_id, "user": users[next_id]}
    next_id += 1
    return jsonify(response), 201

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    all_users = [{"id": uid, "user": info} for uid, info in users.items()]
    return jsonify(all_users)

# Get a single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user_id, "user": users[user_id]})

# Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    users[user_id]["name"] = data["name"]
    return jsonify({"id": user_id, "user": users[user_id]})

# Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "id": user_id, "user": deleted_user})

if __name__ == "__main__":
    app.run(debug=True)
