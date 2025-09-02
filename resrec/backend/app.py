from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

# serve frontend
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# serve dataset
@app.route("/data")
def data():
    json_path = os.path.join(BASE_DIR, "indian_restaurants_realistic.json")
    with open(json_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)
    return jsonify(dataset)

if __name__ == "__main__":
    app.run(debug=True)
