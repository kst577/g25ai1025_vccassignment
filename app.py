from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>LOCAL SERVER: RUNNING</h1><p>Status: Healthy</p>"

if __name__ == "__main__":
    # Runs on Port 5000 by default
    app.run(host='0.0.0.0', port=5000)
