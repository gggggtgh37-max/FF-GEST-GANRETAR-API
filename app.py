from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({
        "name": "Guest Gen API",
        "status": "online",
        "health": "/health",
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
