import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return "Updated DevOps Project Running!"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})
@app.route("/env")
def env():
    return jsonify({"environment": os.getenv("ENV", "dev")})

@app.route("/metrics")
def metrics():
    return jsonify({"cpu": "25%", "memory": "40%"})

@app.route("/log")
def log():
    app.logger.info("Log endpoint triggered")
    return "Logged successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)