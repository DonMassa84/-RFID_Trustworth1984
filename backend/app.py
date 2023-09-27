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

# ... (Rest des Codes aus /backend/app.py)

