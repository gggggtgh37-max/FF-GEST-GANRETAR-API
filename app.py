"""Serverless-safe Flask API entrypoint for Vercel.

Third-party guest-account registration is intentionally not implemented.
"""
from datetime import datetime, timezone
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Cache-Control"] = "no-store"
    return response

@app.get("/")
def index():
    return jsonify({
        "name": "Guest Gen API",
        "status": "online",
        "message": "API service is running.",
        "endpoints": {
            "health": "/health",
            "generate": "/v3/generate"
        }
    })

@app.route("/health", methods=["GET", "OPTIONS"])
def health():
    if request.method == "OPTIONS":
        return ("", 204)
    return jsonify({
        "status": "healthy",
        "service": "guest-gen-api",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/v3/generate", methods=["GET", "OPTIONS", "POST"])
def generate():
    if request.method == "OPTIONS":
        return ("", 204)
    return jsonify({
        "success": False,
        "error": "This deployment does not implement third-party account registration.",
        "code": "FEATURE_NOT_AVAILABLE"
    }), 501

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
