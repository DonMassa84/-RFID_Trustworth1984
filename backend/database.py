import sqlite3

DATABASE_NAME = 'rfid_db.sqlite'

def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            chip_id TEXT PRIMARY KEY,
            name TEXT NOT NULL
        );
        """)

        conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            chip_id TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            location TEXT
        );
        """)

def insert_user(chip_id, name):
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute("INSERT INTO users (chip_id, name) VALUES (?, ?)", (chip_id, name))

def log_scan(chip_id, location):
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute("INSERT INTO logs (chip_id, location) VALUES (?, ?)", (chip_id, location))

def get_all_users():
    with sqlite3.connect(DATABASE_NAME) as conn:
        return conn.execute("SELECT * FROM users").fetchall()

def get_all_logs():
    with sqlite3.connect(DATABASE_NAME) as conn:
        return conn.execute("SELECT * FROM logs").fetchall()
