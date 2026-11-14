from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend API is running inside a Docker container."
    })

@app.get("/api/students")
def students():
    return jsonify({
        "status": "success",
        "application": "Docker Full-Stack Student Information System",
        "students": [
            {"id": 1, "name": "Adeline UMUTONI", "program": "Information Technology"},
            {"id": 2, "name": "Joseph MAHEREZO", "program": "Software Development"},
            {"id": 3, "name": "Diane UWAMAHORO", "program": "Networking"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
