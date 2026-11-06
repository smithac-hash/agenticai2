from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from career_engine import analyze_student

app = Flask(__name__, static_folder="static", static_url_path="/static")
CORS(app)

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}
    required = ["name", "skills", "interests", "goal"]
    missing = [field for field in required if not data.get(field)]

    if missing:
        return jsonify({
            "success": False,
            "message": f"Please provide: {', '.join(missing)}"
        }), 400

    try:
        result = analyze_student(data)
        return jsonify({"success": True, "data": result})
    except Exception as exc:
        return jsonify({"success": False, "message": str(exc)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
