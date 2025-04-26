from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
user_data = {}

@app.route("/<name>/add", methods=["POST"])
def add_balance(name):
    data = request.get_json()
    amount = data.get("amount")

    if not isinstance(amount, int) or amount <= 0:
        return jsonify({"error": "Amount must be a positive integer"}), 400

    user_data[name] = user_data.get(name, 0) + amount
    return jsonify({"name": name, "new_balance": user_data[name]})

@app.route("/<name>/subtract", methods=["POST"])
def subtract_balance(name):
    data = request.get_json()
    amount = data.get("amount")

    if not isinstance(amount, int) or amount <= 0:
        return jsonify({"error": "Amount must be a positive integer"}), 400

    current = user_data.get(name, 0)
    if current < amount:
        return jsonify({"error": "Insufficient balance"}), 400

    user_data[name] = current - amount
    return jsonify({"name": name, "new_balance": user_data[name]})

@app.route("/<name>/balance", methods=["GET"])
def get_balance(name):
    if name not in user_data:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"name": name, "balance": user_data[name]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

