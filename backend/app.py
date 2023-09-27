from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE_NAME = 'rfid_db.sqlite'

@app.route('/get_users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@app.route('/get_logs', methods=['GET'])
def get_logs():
    logs = get_all_logs()
    return jsonify(logs)

@app.route('/get_last_locations', methods=['GET'])
def get_last_locations():
    with sqlite3.connect(DATABASE_NAME) as conn:
        result = conn.execute("""
        SELECT users.name, logs.location, logs.timestamp
        FROM logs
        JOIN users ON logs.chip_id = users.chip_id
        WHERE logs.timestamp = (SELECT MAX(timestamp) FROM logs WHERE chip_id = users.chip_id)
        """).fetchall()
    return jsonify(result)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    chip_id = data['chip_id']
    add_new_user(name, chip_id)
    return jsonify({"message": "User added successfully"})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500



# ... (Rest des Codes aus /backend/app.py)

