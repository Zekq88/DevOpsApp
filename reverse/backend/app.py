from flask import Flask
import socket
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")

@app.route("/")
def hello():
    return f"HeLLo fRoM Da oTherSide {socket.gethostname()}!\n"

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL: {version[0]}\n"
    except Exception as e:
        return f"Database connection failed: {str(e)}\n", 500

@app.route("/health")
def health():
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)