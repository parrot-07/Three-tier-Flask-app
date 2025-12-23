from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def index():
  try:
    conn = mysql.connector.connect(host = os.getenv("DB_HOST"),
                                   user = os.getenv("DB_USER"),
                                   password = os.getenv("DB_PASSWORD"),
                                   database = os.getenv("DB_NAME"))
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from Flask to Mysql to Nginx!'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

  except Exception as e:
    return f"Database connection error: {str(e)}", 500

if __name__ == "__main__" : app.run(host="0.0.0.0", port=5000)
